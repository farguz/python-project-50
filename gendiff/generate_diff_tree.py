import json


def open_json_file(file_path) -> dict:
    json_dict = json.load(open(file_path))
    return json_dict


def get_value_str(dict, key):
    return str(dict.get(key, None))


def generate_diff_json(file_path1: str, file_path2: str) -> str:
    first_file = open_json_file(file_path1)
    second_file = open_json_file(file_path2)

    first_keys = list(first_file)
    second_keys = list(second_file)
    all_keys = list(set(first_keys + second_keys))
    all_keys.sort()
    
    res = ''

    for key in all_keys:
        if get_value_str(first_file, key) == get_value_str(second_file, key):
            res += '    ' + key + ': ' + get_value_str(first_file, key) + '\n'
        else:
            if key in first_keys and key in second_keys:
                res += '  - ' + key + ': ' + get_value_str(first_file, key) + '\n'
                res += '  + ' + key + ': ' + get_value_str(second_file, key) + '\n'              
            elif key in first_keys:
                res += '  - ' + key + ': ' + get_value_str(first_file, key) + '\n'           
            else:
                res += '  + ' + key + ': ' + get_value_str(second_file, key) + '\n'

    res = '{\n' + res + '}'
    print(res)
    return res
