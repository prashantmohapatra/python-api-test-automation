from api import putapi
import json


def test_put_user_post():

    body = json.dumps({
        "id": 1,
        "title": "Existing post",
        "body": "This is a post",
        "userId": 1
    })
    
    response = putapi.PutApi.put_user_post(1, body)
    assert response.status_code == 200
