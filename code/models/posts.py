import sqlite3
from db import db


class PostsModel(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    users_posts = db.relationship('UserModel')
    replies = db.relationship('RepliesModel')
    likes = db.relationship('LikesModel')


    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id


    @classmethod
    def find_by_id(cls, post_id):
        return cls.query.filter_by(id=post_id).first()

        
    def json(self):
        return {'id':self.id, 'user_id': self.user_id, 'title': self.title, 'content': self.content, 'replies' : [reply.json() for reply in self.replies], 'likes': [like.json() for like in self.likes] }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

