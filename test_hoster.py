import json

import allure
import pytest

from utils.checking import Checking

from utils.reqres_api import HosterAPI

"""Create, edit and delete a new user"""
user_id = '2'  # default value


@allure.feature('Test Hoster')
class TestHoster:
    @pytest.fixture()
    @allure.step('test_create_new_user')
    def test_create_new_user(self):
        print('\n\nMethod POST: Create User')
        result_post = HosterAPI.create_new_user()
        new_id = json.loads(result_post.text)['id']
        Checking.check_json_token(result_post, ['name', 'job', 'id', 'createdAt'])
        Checking.check_status_code(result_post, 201)
        Checking.check_json_value(result_post, 'name', "lambotik")
        Checking.check_json_search_word_in_value(result_post, 'id', new_id)
        Checking.check_json_search_word_in_value(result_post, 'job', 'qa')
        return new_id

    @allure.step('test_info_user')
    # @pytest.mark.xfail
    def test_info_new_user(self, test_create_new_user):
        print('\n\nMethod GET: Check user info new user')
        result_get = HosterAPI.checking_new_user(test_create_new_user)
        result_get_new_user = json.loads(result_get.text)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['data', 'support'])
        Checking.check_json_many_tokens(result_get, 'data', ['id', 'email', 'first_name', 'last_name', 'avatar'])
        Checking.check_json_many_tokens(result_get, 'support', ['url', 'text'])
        Checking.check_json_search_word_in_values(result_get_new_user['support'], 'url',
                                                  "https://reqres.in/#support-heading")
        Checking.check_json_search_word_in_value(result_get_new_user['data'], 'id', test_create_new_user)

    # @pytest.mark.xfail
    @allure.step('test_info_user')
    # @pytest.mark.xfail
    def test_info_default_user(self):
        print('\n\nMethod GET: Check user info default user')
        result_get = HosterAPI.checking_new_user(user_id)
        result_get_user = json.loads(result_get.text)
        user_email = result_get_user['data']['email']
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['data', 'support'])
        Checking.check_json_many_tokens(result_get, 'data', ['id', 'email', 'first_name', 'last_name', 'avatar'])
        Checking.check_json_search_word_in_values(result_get_user['data'], 'email', user_email)
        Checking.check_json_many_tokens(result_get, 'support', ['url', 'text'])
        Checking.check_json_search_word_in_values(result_get_user['support'], 'url',
                                                  "https://reqres.in/#support-heading")
        Checking.check_json_search_word_in_values(result_get_user['data'], 'id', user_id)

    @allure.step('test_update_user_info')
    def test_update_new_user_info(self, test_create_new_user):
        print('\n\nMethod PUT: Update new user data')
        result_put = HosterAPI.put_new_user(test_create_new_user)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['name', 'job', 'updatedAt'])
        Checking.check_json_value(result_put, 'name', 'HOSTER')
        Checking.check_json_value(result_put, 'job', 'QA')

    @allure.step('test_update_user_info')
    def test_update_default_user_info(self):
        print('\n\nMethod PUT: Update default user data')
        result_put = HosterAPI.put_default_user(user_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['name', 'job', 'updatedAt'])
        Checking.check_json_value(result_put, 'name', 'morpheus')
        Checking.check_json_value(result_put, 'job', 'zion resident')

    @allure.step('test_delete_user')
    def test_delete_default_user(self):
        print('\n\nMethod DELETE: Delete default user data')
        result_delete = HosterAPI.delete_new_user(user_id)
        Checking.check_status_code(result_delete, 204)

    @allure.step('test_delete_user')
    def test_delete_new_user(self, test_create_new_user):
        print('\n\nMethod DELETE: Delete new user data')
        result_delete = HosterAPI.delete_new_user(test_create_new_user)
        Checking.check_status_code(result_delete, 204)
