from api import patchapi
import json


def test_patch_user_post():

    body = json.dumps({
        "title": "Just an edited title"
    })
    
    response = patchapi.PatchApi.patch_user_post(1, body)
    assert response.status_code == 200
