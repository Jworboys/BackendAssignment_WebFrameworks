import sqlite3
from models.replies import RepliesModel
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
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="Every reply needs a user_id."
    )


    def post(self):
        data = replyPost.parser.parse_args()
        post = RepliesModel(**data)
        post.save_to_db()
        return{"message": "Reply created successfully."}, 201


#Obatin a reply by its' ID.
class obtainReply(Resource):
    def get(self, reply_id):
        reply = RepliesModel.find_by_id(reply_id)
        if reply:
            return reply.json()
        return {"message": "Reply not found."}, 404

#Obtain all replies linked to a post_id.
class replyList_byPost(Resource):
    def get(self, post_id):
        return {'replies' : [reply.json() for reply in RepliesModel.query.filter_by(post_id=post_id).all()]}


#Obtain all replies linked to a user_id.
class replyList_byUser(Resource):
    def get(self, user_id):
        return {'reply' : [reply.json() for reply in RepliesModel.query.filter_by(user_id=user_id).all()]}