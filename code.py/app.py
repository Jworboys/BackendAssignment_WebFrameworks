from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.posts import createPost
from resources.replies import replyPost, replyList_byPost, obtainReply, replyList_byUser
from resources.likes import likePost

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jordan'
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(createPost,'/new_post' )
api.add_resource(replyPost,'/reply_post' )
api.add_resource(obtainReply,'/reply/<int:reply_id>')
api.add_resource(replyList_byPost, '/replies_post/<int:post_id>')
api.add_resource(replyList_byUser, '/replies_user/<int:user_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)