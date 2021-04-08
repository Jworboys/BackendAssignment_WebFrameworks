import sqlite3
from db import db


class LikesModel(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    posts = db.relationship('PostsModel')

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id


    @classmethod
    def find_by_id(cls, like_id):
        return cls.query.filter_by(id=like_id).first()

    def json(self):
        return {'user': self.user_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()