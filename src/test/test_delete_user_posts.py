from api import deleteapi


def test_delete_user_post():
    response = deleteapi.DeleteApi.delete_user_post(1)
    assert response.status_code == 200
