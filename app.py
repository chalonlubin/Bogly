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

    # just a quick way to make sure our view worked
    # test_user = User(first_name='Kadeem', last_name='Best')
    # db.session.add(test_user)
    # db.session.commit()

    return render_template("users.html", users=User.query.all())

@app.get("/add-user")
def add_user():
    """ Add user page """
    return render_template("add-user.html")





