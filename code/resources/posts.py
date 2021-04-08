import sqlite3
from models.posts import PostsModel
from flask_restful import Resource, reqparse

class CreatePost(Resource):

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
        data = CreatePost.parser.parse_args()
        post = PostsModel(**data)
        post.save_to_db()
        return{"message": "Post created successfully."}, 201


#Delete a reply by it's Id.
class DeletePost(Resource):
    def delete(self, post_id):
        post = PostsModel.find_by_id(post_id)
        if post:
            post.delete_from_db()
            return {'message' : 'Post deleted'}, 201
        return {'message' : 'Post not found'}, 400


#Edit post by ID.
class EditPost(Resource):
    def post(self, post_id):
        data = CreatePost.parser.parse_args()
        post = PostsModel.find_by_id(post_id)

        if post is None:
            return {'message' : 'Post does not exist'}, 200
        else: 
            post.title = data['title']
            post.content = data['content'] 
            post.user_id = data['user_id']
        post.save_to_db()
        return {'message': 'Post updated'}, 201


#Obatin a post by its' ID.
class ObtainPost(Resource):
    def get(self, post_id):
        post = PostsModel.find_by_id(post_id)
        if post:
            return post.json(), 200
        return {"message": "post not found."}, 404

#Obtain all posts linked to a user_id.
class PostList_byUser(Resource):
    def get(self, user_id):
        return {'User_posts' : [post.json() for post in PostsModel.query.filter_by(user_id=user_id).all()]}, 200

#Obtain all posts.
class PostList_All(Resource):
    def get(self):
        return {'User_posts' : [post.json() for post in PostsModel.query.all()]}, 200