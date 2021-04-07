import sqlite3
from models.likes import LikesModel
from flask_restful import Resource, reqparse

class likePost(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('post_id',
        type=int,
        required=True,
        help="Every like needs a post."
    )


    def post(self):
        data = likePost.parser.parse_args()
        post = LikesModel(**data)
        post.save_to_db()
        return{"message": "Post liked successfully."}, 201