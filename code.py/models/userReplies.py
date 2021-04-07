import sqlite3
from db import db


class postReplies(db.Model):
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    post = db.relationship('userPosts')

    def __init__(self, content, post_id):
        self.content = content

    
    def json(self):
        return {'content': self.content}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
