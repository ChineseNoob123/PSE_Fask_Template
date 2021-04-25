# Get Database object from __init__.py
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text())
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # Bind User to Note with foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    firstName = db.Column(db.String(100))
    password = db.Column(db.String(100))

    # Cross Relation to Notes
    notes = db.relationship('Note')
