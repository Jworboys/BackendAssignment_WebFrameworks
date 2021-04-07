import sqlite3
from models.posts import Posts
from flask_restful import Resource, reqparse

class createPost(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('content',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="Every post needs a user_ID."
    )


    def post(self):
        data = createPost.parser.parse_args()
        post = Posts(**data)
        post.save_to_db()
        return{"message": "Post created successfully."}, 201