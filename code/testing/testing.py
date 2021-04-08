import requests




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

# Testing creating a post with/without good data.
def test_create_a_post():
    myobj = {"title": "Bob", "content": "Testing Content", "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/new_post", data=myobj)
    assert response.status_code == 201

def test_creating_post_with_false_data():
    response = requests.post("http://127.0.0.1:5000/new_post")
    assert response.status_code == 400





# --- REPLY TESTING ---
# Reply to post
def test_create_a_reply():
    myobj = {"content": "Testing Reply", "post_id": 2, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/reply_post", data=myobj)
    assert response.status_code == 201

# Looking up the reply just made.
def test_get_existing_reply():
    response = requests.get("http://127.0.0.1:5000/reply/6")
    assert response.status_code == 200





# --- LIKE TESTING ---
# Liking a post
def test_liking_a_post():
    myobj = {"post_id": 4, "user_id": 1}
    response = requests.post("http://127.0.0.1:5000/like_post",  data=myobj)
    assert response.status_code == 201






# -- REMOVE TESTING ---
# Removing like
def test_removing_a_like():
    response = requests.delete("http://127.0.0.1:5000/remove/like/2")
    assert response.status_code == 201


# Removing Reply
def test_delete_a_reply():
    response = requests.delete("http://127.0.0.1:5000/reply/delete/1")
    assert response.status_code == 201



#Removing Post
def test_delete_a_reply():
    response = requests.delete("http://127.0.0.1:5000/post/delete/6")
    assert response.status_code == 201
# Trying to delete the already removed post
def test_delete_a_reply():
    response = requests.delete("http://127.0.0.1:5000/post/delete/6")
    assert response.status_code == 400

