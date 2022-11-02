import yaml
import json


def test_type_regular_users_yaml():
    """Check if the file contains data of type"""
    with open(r'./users files/regular_users.yaml') as regular_users_file:
        regular_users = yaml.full_load(regular_users_file)
        assert type(regular_users) is list


def test_type_regular_users_json():
    """Check if the file contains data of type"""
    with open(r'./users files/regular_users.json') as regular_users_file:
        regular_users = json.load(regular_users_file)
        assert type(regular_users) is list
