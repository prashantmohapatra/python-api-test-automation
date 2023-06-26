from api import postapi
import json


def test_post_user_post():

    body = json.dumps({
        "title": "Just an edited title",
        "body": "This is a new post",
        "userId": 1
    })
    
    response = postapi.PostApi.post_user_post(body)
    assert response.status_code == 201
