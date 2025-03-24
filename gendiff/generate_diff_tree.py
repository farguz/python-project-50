import json

import yaml


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


def generate_diff_tree(file_path1, file_path2, format='stylish') -> str:
    
    first_file = open_file(file_path1)
    second_file = open_file(file_path2)

    def inner(first_file, second_file):
        first_keys = list(first_file)
        second_keys = list(second_file)
        all_keys = list(set(first_keys + second_keys))
        all_keys.sort()

        res = {}
        for key in all_keys:
            if key in first_keys and key in second_keys:
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
                                 inner(first_file.get(key), 
                                       second_file.get(key)).items()]
                    }
                else:
                    res[key] = {
                    'type': 'changed',
                    'old_value': get_value(first_file, key), 
                    'new_value': get_value(second_file, key)
                    }
                
            elif key in first_keys:
                res[key] = {
                'type': 'deleted',
                'value': get_value(first_file, key)
                }
            else:
                res[key] = {
                'type': 'added',
                'value': get_value(second_file, key)
                }
        return res

    return inner(first_file, second_file)
