import sqlite3
from models.replies import Replies
from flask_restful import Resource, reqparse

class replyPost(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('content',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('post_id',
        type=int,
        required=True,
        help="Every reply needs a post_ID."
    )


    def post(self):
        data = replyPost.parser.parse_args()
        post = Replies(**data)
        post.save_to_db()
        return{"message": "Reply created successfully."}, 201

class obtainReply(Resource):
    def get(self, reply_id):
        reply = Replies.find_by_id(reply_id)
        if reply:
            return reply.json()
        return {"message": "Reply not found."}, 404

class replyList_byPost(Resource):
    def get(self, post_id):
        reply = Replies.find_replys_by_post_id(post_id)
        return {'replies' : [reply.json() for reply in Replies.query.all()]}

