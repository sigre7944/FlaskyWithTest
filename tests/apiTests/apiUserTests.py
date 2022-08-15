import requests
import string
import random

host_url = 'http://10.0.0.7:8080'
headers = {
    'Content-Type': 'application/json',
    'Token': 'MjQ1NzQ0MzYwNzI5MzI1Nzk3MzYzMzI2NTQ1MDM3MzE5OTM2MzQ2'
}
allowed_fields = (
    'firstname',
    'lastname',
    'phone'
)


def test_get_all_user_list():
    url = host_url + '/api/users'
    response = requests.request('GET', url, headers=headers)
    json_response = response.json()

    expected_users = ['LaFcfoOYp', 'ODgaJNsbh', 'YemveIoox', 'crPKHznIS', 'dHVsFjfwL',
                      'hunter', 'ipiKbSraL', 'nLhJefyws', 'ogoLbyVui', 'rkdFURvfi']
    assert json_response['status'] == 'SUCCESS'
    for username in expected_users:
        assert username in json_response['payload']


def test_get_user_info_by_username():
    test_user = 'hunter'
    url = host_url + '/api/users/' + test_user
    response = requests.request('GET', url, headers=headers)
    json_response = response.json()

    assert json_response['status'] == 'SUCCESS'
    for field in allowed_fields:
        assert field in json_response['payload']


def test_post_register_new_user():
    url = host_url + '/api/users'
    random_string = ''.join((random.choice(string.ascii_lowercase) for x in range(8)))
    new_user = {'username': random_string,
                'password': random_string,
                'firstname': random_string,
                'lastname': random_string,
                'phone': random_string}
    response = requests.request('POST', url, json=new_user, headers=headers)
    assert_request_response_success(response)

    response = requests.request('GET', url, headers=headers)
    json_response = response.json()
    assert random_string in json_response['payload']


def test_put_update_user_info():
    test_user = 'hunter'
    old_value = 'hunter'
    new_value = 'hunter01'
    url = host_url + '/api/users/' + test_user

    new_field_values = {
        'firstname': new_value,
        'lastname': new_value,
        'phone': new_value
    }
    response = requests.request('PUT', url, json=new_field_values, headers=headers)
    assert_request_response_success(response)

    response = requests.request('GET', url, headers=headers)
    assert_field_values_from_response(response, new_value)

    old_field_values = {
        'firstname': old_value,
        'lastname': old_value,
        'phone': old_value
    }
    response = requests.request('PUT', url, json=old_field_values, headers=headers)
    assert_request_response_success(response)

    response = requests.request('GET', url, headers=headers)
    assert_field_values_from_response(response, old_value)


def assert_field_values_from_response(response, value):
    json_response = response.json()
    for field in allowed_fields:
        assert json_response['payload'][field] == value


def assert_request_response_success(response):
    json_response = response.json()
    assert json_response['status'] == 'SUCCESS'
