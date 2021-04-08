import sqlite3
from models.likes import LikesModel
from flask_restful import Resource, reqparse

class LikePost(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('post_id',
        type=int,
        required=True,
        help="Every like needs a post."
    )
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="Every like needs a user."
    )


    def post(self):
        data = LikePost.parser.parse_args()
        post = LikesModel(**data)
        post.save_to_db()
        return{"message": "Post liked successfully."}, 201


#Delete a like by it's Id.
class RemoveLike(Resource):
    def delete(self, like_id):
        like = LikesModel.find_by_id(like_id)
        if like:
            like.delete_from_db()
        return {'message' : 'Like removed'}, 201
