import json

import yaml


def get_value_str(dict, key):
    if dict.get(key) is True:
        return 'true'
    if dict.get(key) is False:
        return 'false'
    if dict.get(key) is None:
        return 'null'
    return str(dict.get(key))


def open_json_file(file_path) -> dict:
    json_dict = json.load(open(file_path))
    return json_dict


def open_yml_file(file_path) -> dict:
    yml_dict = yaml.load(open(file_path), yaml.CLoader)
    return yml_dict


def check_file_extension(path: str) -> str:
    extension = path.split('.')[-1].lower()
    return extension


def generate_diff_tree(file_path1: str, file_path2: str) -> str:
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

    def inner(first_file, second_file):
        first_keys = list(first_file)
        second_keys = list(second_file)
        all_keys = list(set(first_keys + second_keys))
        all_keys.sort()

        res = {}
        for key in all_keys:
            if key in first_keys and key in second_keys:
                if get_value_str(first_file, key) == get_value_str(second_file, key):
                    res[key] = {
                        'type': 'unchanged',
                        'value': get_value_str(first_file, key)                
                    }
                elif type(first_file[key]) == dict and type(second_file[key]) == dict:
                    res[key] = {
                    'type': 'nested',
                    'value': inner(first_file.get(key), second_file.get(key))
                    }
                else:
                    res[key] = {
                    'type': 'changed',
                    'old_value': get_value_str(first_file, key),    
                    'new_value': get_value_str(second_file, key)
                    }
                
            elif key in first_keys:
                res[key] = {
                'type': 'deleted',
                'value': get_value_str(first_file, key)
                }
            else:
                res[key] = {
                'type': 'added',
                'value': get_value_str(second_file, key)
                }
        return res

    return inner(first_file, second_file)
