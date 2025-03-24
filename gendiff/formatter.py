import json


def choose_format(diff_tree: dict, format: str = 'stylish'):
    if format == 'plain':
        return plain(diff_tree)
    elif format == 'stylish':
        return stylish(diff_tree)
    elif format == 'json':
        return json_format(diff_tree)
    

def check_type(element):
    if (isinstance(element, dict) or 
        isinstance(element, list) or 
        isinstance(element, set)):
        return '[complex value]'
        
    if isinstance(element, bool):
        return f"{str(element).lower()}"
        
    if element is None:
        return 'null'
        
    if isinstance(element, int):
        return f"{element}"
        
    return f"'{str(element)}'"


def is_dict(value, depth):
    if isinstance(value, dict):
        res = '{\n'
        for k, v in value.items(): 
            res += f'{replacer * (depth)}{k}: {is_dict(v, depth + 1)}\n'
        res += f'{replacer * (depth - 1)}}}'
        return res
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish(diff_tree: dict) -> str:
    depth = 1
    global replacer
    replacer = '    '
    
    if diff_tree == {}:
        return ''

    def walk(element, depth):
        res = ''
        for k, v in element.items():
            if v['type'] == 'added':
                res += (f"{replacer * (depth - 1)}  + " + 
                        f"{k}: {is_dict(v['value'], depth + 1)}\n")
            elif v['type'] == 'deleted':
                res += (f"{replacer * (depth - 1)}  - " + 
                         f"{k}: {is_dict(v['value'], depth + 1)}\n")
            elif v['type'] == 'changed':
                res += (f"{replacer * (depth - 1)}  - " + 
                        f"{k}: {is_dict(v['old_value'], depth + 1)}\n")
                res += (f"{replacer * (depth - 1)}  + " + 
                        f"{k}: {is_dict(v['new_value'], depth + 1)}\n")
            elif v['type'] == 'unchanged':
                res += (f"{replacer * (depth - 1)}    " + 
                        f"{k}: {is_dict(v['value'], depth + 1)}\n")
            elif v['type'] == 'nested':
                res += (f"{replacer * (depth - 1)}    " + 
                        f"{k}: {{\n")
                for child in v['children']:
                    res += walk(child, depth + 1)
                res += f'{replacer * (depth)}}}\n'
        return res

    return '{\n' + walk(diff_tree, depth) + '}'


def plain(diff_tree: dict) -> str:
    if diff_tree == {}:
        return ''

    def walk(element, path=''):
        res = ''
        for k, v in element.items():
            new_path = path + '.' + str(k) if path else str(k)

            if v['type'] == 'added':
                res += (f"Property '{new_path}' was added " + 
                        f"with value: {check_type(v['value'])}\n")
            elif v['type'] == 'deleted':
                res += (f"Property '{new_path}' was removed\n")
            elif v['type'] == 'changed':
                res += (f"Property '{new_path}' was updated. From " + 
                        f"{check_type(v['old_value'])} to " + 
                        f"{check_type(v['new_value'])}\n")
            elif v['type'] == 'unchanged':
                pass
            elif v['type'] == 'nested':
                for child in v['children']:
                    res += walk(child, new_path)

        return res
    return walk(diff_tree).strip('\n')


def json_format(diff_tree: dict) -> str:
    return json.dumps(diff_tree)
