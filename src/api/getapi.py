from api.apimanager import ApiExecutor
from environment import ENV


POSTS_URL = ENV["BASE_URL"] + "/posts"
headers = {'custom-header': 'get-test'}


class GetApi:
    @staticmethod
    def get_user_posts():
        """
        GET /posts
    
                Returns:
                        Response
        """
        return ApiExecutor.send("GET", POSTS_URL, headers)

    @staticmethod
    def get_user_post(post_id):
        """
        GET /post/:id
    
                Parameters:
                        post_id: Post ID
    
                Returns:
                        Response
        """
        return ApiExecutor.send("GET", f'{POSTS_URL}/{post_id}', headers)

