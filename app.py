"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "nicki_minaj_x_kadeem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

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

# TODO: Fix route
# @app.post("/add-new-user")
# def add_new_user():
#     """ Add new user and route to homepage """

#     first_name = request.form["firstName"]
#     last_name = request.form["lastName"]
#     img_url = request.form["image"]

#     #TODO: make sure all these fields exist b4 image url

#     new_user = User(
#             first_name=first_name,
#             last_name=last_name
#         )
#     if img_url:
#         new_user.image_url=img_url

    # db.session.add(new_user)
    # db.session.commit()

#     return redirect("/")

    # if img_url:
    #     new_user = User(
    #         first_name=first_name,
    #         last_name=last_name,
    #         image_url=img_url
    #     )
    # else:
    #     new_user = User(
    #         first_name=first_name,
    #         last_name=last_name
    #     )


# TODO int conversion in decorator

