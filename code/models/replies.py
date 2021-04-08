import sqlite3
from db import db


class RepliesModel(db.Model):
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    posts = db.relationship('PostsModel')

    def __init__(self, content, post_id, user_id):
        self.content = content
        self.post_id = post_id
        self.user_id = user_id

    
    def json(self):
        return {'reply_id': self.id, 'content': self.content, 'post_id': self.post_id, 'user_id': self.user_id}

    @classmethod
    def find_by_id(cls, reply_id):
        return cls.query.filter_by(id=reply_id).first()

    @classmethod
    def find_replys_by_post_id(cls, post_id):
        return cls.query.filter_by(post_id=post_id).all()
        
    @classmethod
    def find_replys_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
