from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.posts import CreatePost, DeletePost, PostList_byUser, ObtainPost, PostList_All, EditPost
from resources.replies import ReplyPost, ReplyList_byPost, ObtainReply, ReplyList_byUser, DeleteReply, EditReply
from resources.likes import LikePost, RemoveLike

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jordan'
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)

# User routes.
api.add_resource(UserRegister, '/register')

# Post routes, user_id must be passed in the body.
api.add_resource(CreatePost,'/new_post' )
api.add_resource(DeletePost, '/post/delete/<int:post_id>')
api.add_resource(ObtainPost,'/post/<int:post_id>')
api.add_resource(PostList_byUser, '/posts/users/<int:user_id>')
api.add_resource(EditPost, '/posts/update/<int:post_id>')
api.add_resource(PostList_All, '/posts/all')

# Reply routes, user_id, post_id must be passed in the body.
api.add_resource(ReplyPost,'/reply_post')
api.add_resource(ObtainReply,'/reply/<int:reply_id>')
api.add_resource(ReplyList_byPost, '/replies_post/<int:post_id>')
api.add_resource(ReplyList_byUser, '/replies_user/<int:user_id>')
api.add_resource(DeleteReply, '/reply/delete/<int:reply_id>')
api.add_resource(EditReply, '/reply/update/<int:reply_id>')

# Like routes, user_id, post_id must be passed in the body.
api.add_resource(LikePost, '/like_post')
api.add_resource(RemoveLike, '/remove/like/<int:like_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)