import json

import allure
import pytest

from utils.checking import Checking

from utils.reqres_api import HosterAPI

"""Create, edit and delete a new user"""


@allure.feature('Test Hoster')
class TestHoster:

    @allure.step('test_create_new_user')
    @pytest.fixture()
    def test_create_new_user(self):
        print('\nMethod POST')
        result_post = HosterAPI.create_new_user()
        result_new_user = json.loads(result_post.text)
        user_id = result_new_user['id']
        Checking.check_json_token(result_post, ['name', 'job', 'id', 'createdAt'])
        Checking.check_status_code(result_post, 201)
        Checking.check_json_value(result_post, 'name', "lambotik")
        Checking.check_json_search_word_in_value(result_post, 'id', user_id)
        Checking.check_json_search_word_in_value(result_post, 'job', 'qa')
        return user_id

    @allure.step('test_info_user')
    @pytest.mark.xfail
    def test_info_user(self, test_create_new_user):
        print('\nMethod GET')
        result_get = HosterAPI.checking_new_user(test_create_new_user)
        result_get_new_user = json.loads(result_get.text)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['data', 'support'])
        Checking.check_json_many_tokens(result_get, 'data', ['id', 'email', 'first_name', 'last_name', 'avatar'])
        Checking.check_json_many_tokens(result_get, 'support', ['url', 'text'])
        Checking.check_json_search_word_in_values(result_get_new_user['support'], 'url',
                                                  "https://reqres.in/#support-heading")
        Checking.check_json_search_word_in_values(result_get_new_user['data'], 'id', test_create_new_user)

    @allure.step('test_update_user_info')
    def test_update_user_info(self, test_create_new_user):
        print('\nMethod PUT')
        result_put = HosterAPI.put_new_user(test_create_new_user)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['name', 'job', 'updatedAt'])
        Checking.check_json_value(result_put, 'name', 'HOSTER')
        Checking.check_json_value(result_put, 'job', 'Hoster.by')

    @allure.step('test_delete_user')
    def test_delete_user(self, test_create_new_user):
        print('\nMethod DELETE')
        result_delete = HosterAPI.delete_new_user(test_create_new_user)
        Checking.check_status_code(result_delete, 204)
