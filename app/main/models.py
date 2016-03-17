# Flask stuff
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin.contrib import sqla

# SQLAlchemy stuff
import sqlalchemy as sql
from sqlalchemy import ForeignKey
from app.database import db

# Create additional tables
user_tags_table = db.Table('user_tags',
                  db.Column('user_id', db.Integer, ForeignKey('user.id')),
                  db.Column('tag_id', db.Integer, ForeignKey('tag.id'))
)


class User(db.Model):
    """ Represents an user """
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Text, unique = True)
    password = db.Column(db.Text)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Tag(db.Model):
    """ Table for tags """
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    desc = db.Column(db.Text)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
