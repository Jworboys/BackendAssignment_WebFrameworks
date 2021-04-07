import sqlite3
from models.userPosts import userPosts
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


    def post(self):
        data = createPost.parser.parse_args()
        post = userPosts(**data)
        post.save_to_db()
        return{"message": "Post created successfully."}, 201