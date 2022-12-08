"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://ichef.bbci.co.uk/news/976/cpsprodpb/3497/production/_108636431_one.jpg.webp'

def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
         primary_key=True,
         autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.Text, nullable=True,
                          default=DEFAULT_IMAGE_URL)


class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
         primary_key=True,
         autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    author = db.relationship("User", backref='posts')


