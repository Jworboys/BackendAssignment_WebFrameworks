import sqlite3
from db import db


class userPosts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    users_posts = db.relationship('UserModel', lazy='dynamic')
    replies = db.relationship('postReplies', lazy='dynamic')


    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def json(self):
        return {'title': self.title, 'content': self.content, 'replies' : [reply.json() for reply in self.replies.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

