from api.apimanager import ApiExecutor
from environment import ENV


POSTS_URL = f'{ENV["BASE_URL"]}/posts'
headers = {'custom-header': 'post-test'}


class PostApi:

    @staticmethod
    def post_user_post(body):
        """
        POST /posts
        
                Parameters:
                        body: request body

                Returns:
                        Response
        """
        return ApiExecutor.send("POST", f'{POSTS_URL}', headers, body)

