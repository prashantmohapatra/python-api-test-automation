from api.apimanager import ApiExecutor
from environment import ENV


POSTS_URL = ENV["BASE_URL"] + "/posts"
headers = {'custom-header': 'patch-test'}


class PatchApi:

    @staticmethod
    def patch_user_post(post_id, body):
        """
        PATCH /posts/{:id}
        
                Parameters:
                        post_id: Post ID
                        body: request body

                Returns:
                        Response
        """
        return ApiExecutor.send("PATCH", f'{POSTS_URL}/{post_id}', headers, body)

