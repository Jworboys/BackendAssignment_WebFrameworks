import sqlite3
from models.userReplies import postReplies
from flask_restful import Resource, reqparse

class replyPost(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('content',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = postReplies.parser.parse_args()
        post = postReplies(**data)
        post.save_to_db()
        return{"message": "Reply created successfully."}, 201