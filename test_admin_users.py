import yaml
import json
from schema import Schema, And, Use, Optional, SchemaError

with open(r'./users files/admin_users.yaml') as admin_users_file:
    admin_users_yaml = yaml.full_load(admin_users_file)
with open(r'./users files/admin_users.json') as admin_users_file:
    admin_users_json = json.load(admin_users_file)

schema = Schema([{'id': Use(int), 'name': Use(str),}])


def test_type_admin_users_yaml():
    """Check if the file contains data of type"""
    assert type(admin_users_yaml) is list


def test_type_admin_users_json():
    """Check if the file contains data of type"""
    assert type(admin_users_json) is list


def test_format_admin_users():
    for user in admin_users_yaml:
        assert schema.validate(user)
