import json

import yaml

from gendiff.formatters.json_formatter import json_format
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.stylish_formatter import stylish


def get_value(dict, key):
    return dict.get(key)


def open_json_file(file_path) -> dict:
    if file_path == '':
        return None
    json_dict = json.load(open(file_path))
    return json_dict


def open_yml_file(file_path) -> dict:
    if file_path == '':
        return None
    yml_dict = yaml.load(open(file_path), yaml.CLoader)
    return yml_dict


def check_file_extension(path: str) -> str:
    if path == '':
        return None
    extension = path.split('.')[-1].lower()
    return extension


def open_file(path: str):
    file_extension = check_file_extension(path)

    if file_extension == 'json':
        return open_json_file(path)
    elif file_extension in ['yml', 'yaml']:
        return open_yml_file(path)


def get_all_keys_sorted(first_file, second_file):
    first_keys = list(first_file)
    second_keys = list(second_file)
    all_keys = list(set(first_keys + second_keys))
    all_keys.sort()
    return first_keys, second_keys, all_keys


def both_keys_exist(res, key, first_file, second_file):
    if get_value(first_file, key) == get_value(second_file, key):
        res[key] = {
            'type': 'unchanged',
            'value': get_value(first_file, key)
            }
    elif (isinstance(first_file[key], dict) and 
          isinstance(second_file[key], dict)):
        res[key] = {
            'type': 'nested',
            'children': [{k: v} for k, v in
                         create_tree(first_file.get(key),
                               second_file.get(key)).items()]
                               }
    else:
        res[key] = {
            'type': 'changed',
            'old_value': get_value(first_file, key),
            'new_value': get_value(second_file, key)
            }


def add_label_deleted(res, key, first_file):
    res[key] = {
        'type': 'deleted',
        'value': get_value(first_file, key)
        }
    

def add_label_added(res, key, second_file):
    res[key] = {
        'type': 'added',
        'value': get_value(second_file, key)
        }
    

def walk_tree(first_file, second_file, key, res):
    first_keys, second_keys = (
        get_all_keys_sorted(first_file, second_file)[0],
        get_all_keys_sorted(first_file, second_file)[1]
        )
    
    if key in first_keys and key in second_keys:
        both_keys_exist(res, key, first_file, second_file)
                
    elif key in first_keys:
        add_label_deleted(res, key, first_file)

    else:
        add_label_added(res, key, second_file)

    return res


def create_tree(first_file,
                second_file):
    
    all_keys = (
        get_all_keys_sorted(first_file, second_file)[2]
        )
    
    res = {}
    for key in all_keys:
        res = walk_tree(first_file, second_file, key, res)

    return res


def generate_diff_tree(file_path1, file_path2, format='stylish') -> str:
    
    first_file = open_file(file_path1)
    second_file = open_file(file_path2)

    return create_tree(first_file, second_file)


def choose_format(diff_tree: dict, format: str = 'stylish'):
    if format == 'plain':
        return plain(diff_tree)
    elif format == 'stylish':
        return stylish(diff_tree)
    elif format == 'json':
        return json_format(diff_tree)
