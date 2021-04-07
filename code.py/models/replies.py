import sqlite3
from db import db


class Replies(db.Model):
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    post = db.relationship('userPosts')

    def __init__(self, content, post_id):
        self.content = content
        self.post_id = post_id

    
    def json(self):
        return {'content': self.content}

    @classmethod
    def find_by_id(cls, reply_id):
        return cls.query.filter_by(id=reply_id).first()

    @classmethod
    def find_replys_by_post_id(cls, post_id):
        return cls.query.filter_by(post_id=post_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
