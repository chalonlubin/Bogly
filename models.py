"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "Users"

    id = db.Column(db.Ineger,
         primary_key=True,
         autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.Text, nullable=True,
                          default='https://ichef.bbci.co.uk/news/976/cpsprodpb/3497/production/_108636431_one.jpg.webp')
