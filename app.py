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
    """ Displays the Users on the homepage """

    return render_template("users.html", users=User.query.all())

@app.get("/add-user")
def add_user():
    """ Add user page """
    return render_template("add-user.html")


@app.post("/add-new-user")
def add_new_user():
    """ Add new user and route to homepage """

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