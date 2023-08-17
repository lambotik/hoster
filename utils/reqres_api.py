from utils.http_methods import HTTP_Methods

base_url = 'https://reqres.in/'  # Base url



class HosterAPI:

    @staticmethod
    def create_new_user():
        """
        Method for create new user
        :return: JSON Response
        """
        json_for_create_new_user = {
            "name": "lambotik",
            "job": "qa"
        }

        post_resource = 'api/users'  # Resource for method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = HTTP_Methods.post(post_url, json_for_create_new_user)
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def checking_new_user(user_id):
        """
        Method checking user info
        :param user_id: str
        :return: JSON Response
        """
        get_resource = 'api/users/'  # Resource for method GET
        get_url = base_url + get_resource + user_id
        print(get_url)
        result_get = HTTP_Methods.get(get_url)
        print('Response body: ', result_get.text)
        return result_get

    @staticmethod
    def put_new_user(user_id):
        """
        Method for changing new location
        :param user_id: int
        :return: JSON Response
        """
        put_resource = 'api/users/'  # Resource for method PUT
        put_url = base_url + put_resource + user_id
        print(put_url)
        json_for_update_new_place = {
            "name": 'morpheus',
            "job": "zion resident"
        }
        result_put = HTTP_Methods.put(put_url, json_for_update_new_place)
        print('Response body: ', result_put.text)
        return result_put

    @staticmethod
    def delete_new_user(user_id):
        """
        Method delete user
        :param user_id:
        :return: JSON Response
        """
        delete_resource = 'api/users/'  # Resource for method DELETE
        delete_url = base_url + delete_resource + user_id
        print('Url: ', delete_url)
        json_for_delete_new_user = {"id": user_id}
        result_delete = HTTP_Methods.delete(delete_url, json_for_delete_new_user)
        print('Response body: ', result_delete.text)
        return result_delete

    @staticmethod
    def checking_unknown_user(user_id):
        get_resource = 'api/unknown/'  # Resource for method GET
        get_url = base_url + get_resource + user_id
        print(get_url)
        result_get = HTTP_Methods.get(get_url)
        print(result_get.text)
        return result_get
