import sqlite3
from db import db


class userPosts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(250))

    replies = db.relationship('postReplies', lazy='dynamic')


    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {'title': self.title, 'content': self.content, 'replies' : [reply.json() for reply in self.replies.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

