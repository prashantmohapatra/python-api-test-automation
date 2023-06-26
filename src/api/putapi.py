from api.apimanager import ApiExecutor
from environment import ENV


POSTS_URL = f'{ENV["BASE_URL"]}/posts'
headers = {'custom-header': 'patch-test'}


class PutApi:

    @staticmethod
    def put_user_post(post_id, body):
        """
        PUT /posts/{:id}
        
                Parameters:
                        post_id: Post ID
                        body: request body

                Returns:
                        Response
        """
        return ApiExecutor.send("PUT", f'{POSTS_URL}/{post_id}', headers, body)

