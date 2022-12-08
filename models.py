"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from datetime import datetime

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

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} id={self.id}>"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
         primary_key=True,
         autoincrement=True)
    title = db.Column(
        db.String(150),
        nullable=False)
    content = db.Column(
        db.Text,
        nullable=False)

    # ProgrammingError: (psycopg2.ProgrammingError) can't adapt type 'now'
    # [SQL: INSERT INTO posts (title, content, created_at, user_id) VALUES (%(title)s, %(content)s, %(created_at)s, %(user_id)s) RETURNING posts.id]
    # [parameters: {'title': 'My first post', 'content': 'Hello', 'created_at': <sqlalchemy.sql.functions.now at 0x7fcb78a8d840; now>, 'user_id': 1}]
    # (Background on this error at: https://sqlalche.me/e/14/f405)
    # created_at = db.Column(
    #     db.DateTime,
    #     nullable=False,
    #     default=db.func.now())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'))

    # post instance .author --> user
    author = db.relationship(
        "User",
        backref='posts')


