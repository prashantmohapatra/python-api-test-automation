from api import getapi


def test_get_user_posts():
    response = getapi.GetApi.get_user_posts()
    assert response.status_code == 200

    getapi.GetApi.get_user_post(1)


def test_get_user_post():
    response = getapi.GetApi.get_user_post(1)
    assert response.status_code == 200