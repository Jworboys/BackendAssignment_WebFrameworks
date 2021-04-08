import requests

# -- Creating starting users ---
# -- This user will have userID 1 if starting with fresh database.
def test_create_user():
    myobj = {"username": "Bob", "password": "4321"}
    response = requests.post("http://127.0.0.1:5000/register", data=myobj)
    assert response.status_code == 201

# -- Creating Some starting posts --
def test_create_a_post():
    myobj = {"title": "Bob", "content": "Testing Content", "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/new_post", data=myobj)
    assert response.status_code == 201

#Creating a 2nd post because the first will be deleted soon after and will not be able to be 
#obsereved from within the database.
def test_create_a_2ndpost():
    myobj = {"title": "Bob", "content": "Testing Content", "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/new_post", data=myobj)
    assert response.status_code == 201

#Testing to make sure data must be present and formatted correctly.
def test_create_a_badpost():
    response = requests.post("http://127.0.0.1:5000/new_post")
    assert response.status_code == 400





# --- POST TESTING ---
# Testing obtaining a post.
def test_get_existing_post_by_id():
    response = requests.get("http://127.0.0.1:5000/post/2")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

def test_get_nonexisting_post_by_id():
    response = requests.get("http://127.0.0.1:5000/post/9009")
    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"

def test_creating_post_with_false_data():
    response = requests.post("http://127.0.0.1:5000/new_post")
    assert response.status_code == 400

def test_editing_existing_post():
    myobj = {"title": "New Title", "content": "JR", "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/posts/update/2", data=myobj)
    assert response.status_code == 201

def test_editing_nonexisting_post():
    myobj = {"title": "New Title", "content": "JR", "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/posts/update/1000", data=myobj)
    assert response.status_code == 200  # sending back 200 beacause it still recoginzes and 
                                        # informs user that reply dosent exist.





# --- REPLY TESTING ---
# Reply to post
def test_create_a_reply():
    myobj = {"content": "Testing Reply", "post_id": 2, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/reply_post", data=myobj)
    assert response.status_code == 201

#Creating a 2nd reply because the first will be deleted soon after and will not be able to be 
#obsereved from within the database.
def test_create_a_2ndreply():
    myobj = {"content": "Testing Reply", "post_id": 2, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/reply_post", data=myobj)
    assert response.status_code == 201

# Looking up the reply just made.
def test_get_existing_reply():
    response = requests.get("http://127.0.0.1:5000/reply/1")
    assert response.status_code == 200

# Editing Reply
def test_editing_existing_reply():
    myobj = {"content": "JR", "post_id": 1, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/reply/update/1", data=myobj)
    assert response.status_code == 201

# Editing Reply
def test_editing_nonexisting_reply():
    myobj = {"content": "JR", "post_id": 1, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/reply/update/2021", data=myobj)
    assert response.status_code == 200  # sending back 200 beacause it still recoginzes and 
                                        # informs user that reply dosent exist.






# --- LIKE TESTING ---
# Liking a post
def test_liking_a_post():
    myobj = {"post_id": 1, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/like_post",  data=myobj)
    assert response.status_code == 201







# -- REMOVE TESTING ---
# Removing like
def test_removing_a_like():
    response = requests.delete("http://127.0.0.1:5000/remove/like/1")
    assert response.status_code == 201

# Removing Reply
def test_delete_a_reply():
    response = requests.delete("http://127.0.0.1:5000/reply/delete/1")
    assert response.status_code == 201

#Removing Post
def test_delete_a_post():
    response = requests.delete("http://127.0.0.1:5000/post/delete/1")
    assert response.status_code == 201


