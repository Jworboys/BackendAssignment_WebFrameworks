import sqlite3
from models.replies import RepliesModel
from flask_restful import Resource, reqparse


class ReplyPost(Resource):

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
        data = ReplyPost.parser.parse_args()
        post = RepliesModel(**data)
        post.save_to_db()
        return{"message": "Reply created successfully."}, 201


#Delete a reply by it's Id.
class DeleteReply(Resource):
    def delete(self, reply_id):
        reply = RepliesModel.find_by_id(reply_id)
        if reply:
            reply.delete_from_db()
        return {'message' : 'Reply deleted'}, 201

#Gives capability to edit a reply.
class EditReply(Resource):
    def post(self, reply_id):
        data = ReplyPost.parser.parse_args()
        reply = RepliesModel.find_by_id(reply_id)

        if reply is None:
            return {'message' : 'Reply does not exist'}, 200
        else: 
            reply.user_id = data['user_id']
            reply.post_id = data['post_id']
            reply.content = data['content'] 
        reply.save_to_db()
        return {'message': 'Reply updated'}, 201
        

#Obatin a reply by its' ID.
class ObtainReply(Resource):
    def get(self, reply_id):
        reply = RepliesModel.find_by_id(reply_id)
        if reply:
            return reply.json(), 200
        return {"message": "Reply not found."}, 404

#Obtain all replies linked to a post_id.
class ReplyList_byPost(Resource):
    def get(self, post_id):
        return {'replies' : [reply.json() for reply in RepliesModel.query.filter_by(post_id=post_id).all()]}, 200


#Obtain all replies linked to a user_id.
class ReplyList_byUser(Resource):
    def get(self, user_id):
        return {'reply' : [reply.json() for reply in RepliesModel.query.filter_by(user_id=user_id).all()]}, 200