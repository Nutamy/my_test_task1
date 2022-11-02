import yaml
import json

with open(r'./users files/admin_users.yaml') as admin_users_file:
    admin_users_yaml = yaml.full_load(admin_users_file)
with open(r'./users files/admin_users.json') as admin_users_file:
    admin_users_json = json.load(admin_users_file)


def test_type_admin_users_yaml():
    """Check if the file contains data of type list"""
    assert type(admin_users_yaml) is list


def test_type_admin_users_json():
    """Check if the file contains data of type list"""
    assert type(admin_users_json) is list


def test_consist_id_admin_users():
    for user in admin_users_yaml:
        if len(user) == 2:
            assert 'id' in user and 'name' in user
        else:
            assert 'id' in user and 'name' in user and 'address' in user

