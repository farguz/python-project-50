import json

import yaml

from gendiff.formatter import plain


def open_json_file(file_path) -> dict:
    json_dict = json.load(open(file_path))
    return json_dict


def open_yml_file(file_path) -> dict:
    yml_dict = yaml.load(open(file_path), yaml.CLoader)
    return yml_dict


def check_file_extension(path: str) -> str:
    extension = path.split('.')[-1].lower()
    return extension


def generate_diff_json(file_path1: str, file_path2: str) -> str:
    first_file_extension = check_file_extension(file_path1)
    second_file_extension = check_file_extension(file_path2)

    if first_file_extension == 'json':
        first_file = open_json_file(file_path1)
    elif first_file_extension == 'yml' or first_file_extension == 'yaml':
        first_file = open_yml_file(file_path1)
    if second_file_extension == 'json':
        second_file = open_json_file(file_path2)
    elif second_file_extension == 'yml' or second_file_extension == 'yaml':
        second_file = open_yml_file(file_path2)

    res = plain(first_file, second_file)
    print(res)
    return res
    
