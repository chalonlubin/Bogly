"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "nicki_minaj_x_kadeem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# Seed
# danny = User(first_name="Daniel", last_name="Zeljko")
# chalon = User(first_name="Chalon", last_name="Lubin")
# db.session.add_all([danny, chalon])
# db.session.commit()

# post1 = Post(title="My first post", content="Hello", user_id=1)
# post2 = Post(title="My second post", content="123", user_id=1)
# post3 = Post(title="My first post", content="4444", user_id=2)
# db.session.add_all([post1, post2, post3])
# db.session.commit()


@app.get("/")
def home():
    """ Redirect to list of users. """
    return redirect("/users")


@app.get("/users")
def list_users():
    """ Show all users. """
    return render_template("users.html", users=User.query.all())


@app.route("/users/new", methods=['GET', 'POST'])
def add_user():
    """
    GET:  Show an add form for users
    POST: Process the add form, adding a new user and going back to /users
    """

    if request.method == "POST":
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        img_url = request.form["image"]

        #TODO: make sure all these fields exist b4 image url

        new_user = User(
                first_name=first_name,
                last_name=last_name
            )
        if img_url:
            new_user.image_url=img_url

        db.session.add(new_user)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add-user.html")


@app.get("/users/<id>")
def user_detail_view(id):
    """ Show information about the given user. """
    user = User.query.get_or_404(int(id))
    return render_template("user-detail.html", user=user)


@app.get("/posts/<int:id>")
def user_post_detail_view(id):
    """ Show information about the given user. """
    post = Post.query.get_or_404(id)
    return render_template("post-detail.html", post=post)

@app.get("/posts/<int:id>/edit")
def edit_user_post_view(id):
    """Show page allowing user to edit post."""
    post = Post.query.get_or_404(id)

    return render_template("edit-post.html", post=post)

@app.post("/posts/<int:id>/edit")
def edit_post(id):
    """Edit posts."""

    post = Post.query.get_or_404(id)

    title = request.form["title"]
    content = request.form["content"]

    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()

    return redirect(f"/posts/{post.id}")

@app.post("/posts/<int:id>/delete")
def delete_post(id):
    """Delete posts."""

    post = Post.query.get_or_404(id)
    author_id = post.author.id

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{author_id}" )

@app.route("/users/<id>/edit", methods=['GET', 'POST'])
def edit_user(id):
    """ Process the edit form, returning the user to the /users page. """

    user = User.query.get_or_404(int(id))

    if request.method == "POST":
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        img_url = request.form["image"]

        user.first_name = first_name
        user.last_name = last_name
        user.img_url = img_url

        db.session.add(user)
        db.session.commit()

        return redirect("/users")

    else:
        return render_template("edit-user.html", user=user)


@app.post("/users/<id>/delete")
def delete_user(id):
    """ Delete the user. """
    user = User.query.get_or_404(int(id))
    db.session.delete(user)
    db.session.commit()
    return redirect("/users")


@app.route("/users/<id>/posts/new", methods=['GET', 'POST'])
def add_post(id):
    """
    GET:    Show form to add a post for that user.
    POST:   Handle add form; add post and redirect to the user detail page.
    """
    user = User.query.get_or_404(int(id))

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        new_post = Post(
            title=title,
            content=content
        )
        new_post.user_id = user.id
        db.session.add(new_post)
        db.session.commit()

        return redirect(f"/users/{user.id}")

    else:
        return render_template("add-post.html", user=user)


