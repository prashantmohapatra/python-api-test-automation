from api.apimanager import ApiExecutor
from environment import ENV


POSTS_URL = ENV["BASE_URL"] + "/posts"
headers = {'custom-header': 'delete-test'}


class DeleteApi:

    @staticmethod
    def delete_user_post(post_id):
        """
        DELETE /posts/:id
    
                Parameters:
                        post_id: Post ID
    
                Returns:
                        Response
        """
        return ApiExecutor.send("DELETE", f'{POSTS_URL}/{post_id}', headers)

