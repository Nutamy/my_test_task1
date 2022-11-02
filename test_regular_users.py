import yaml
import json

with open(r'./users files/regular_users.yaml') as regular_users_file:
    regular_users_yaml = yaml.full_load(regular_users_file)
with open(r'./users files/regular_users.json') as regular_users_file:
    regular_users_json = json.load(regular_users_file)


def test_type_regular_users_yaml():
    """Check if the file contains data of type list"""
    assert type(regular_users_yaml) is list


def test_type_regular_users_json():
    """Check if the file contains data of type list"""
    assert type(regular_users_json) is list


def test_consist_id_and_name_regular_users():
    for user in regular_users_yaml:
        if len(user) == 2:
            assert 'id' in user and 'name' in user
        else:
            assert 'id' in user and 'name' in user and 'address' in user
