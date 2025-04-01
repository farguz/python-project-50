def recurse_dict(value, depth):
    res = '{\n'
    for k, v in value.items(): 
        res += f'{indent * (depth)}{k}: {dict_check(v, depth + 1)}\n'
    res += f'{indent * (depth - 1)}}}'
    return res


def dict_check(value, depth):
    if isinstance(value, dict):
        res = recurse_dict(value, depth)
    elif isinstance(value, bool):
        res = str(value).lower()
    elif value is None:
        res = 'null'
    else:
        res = str(value)
    return res


def format_added(k, v, depth):
    return (f"{indent * (depth - 1)}  + " + 
            f"{k}: {dict_check(v['value'], depth + 1)}\n")


def format_deleted(k, v, depth):
    return (f"{indent * (depth - 1)}  - " + 
            f"{k}: {dict_check(v['value'], depth + 1)}\n")


def format_changed(k, v, depth):
    old_value = (f"{indent * (depth - 1)}  - " + 
                 f"{k}: {dict_check(v['old_value'], depth + 1)}\n")
    new_value = (f"{indent * (depth - 1)}  + " + 
                 f"{k}: {dict_check(v['new_value'], depth + 1)}\n")
    return old_value, new_value


def format_unchanged(k, v, depth):
    return (f"{indent * (depth - 1)}    " + 
            f"{k}: {dict_check(v['value'], depth + 1)}\n")


def format_nested(k, v, depth):
    return (f"{indent * (depth - 1)}    " + 
            f"{k}: {{\n")


def walk(element, depth):
    res = ''
    for k, v in element.items():
        if v['type'] == 'added':
            res += format_added(k, v, depth)
        elif v['type'] == 'deleted':
            res += format_deleted(k, v, depth)
        elif v['type'] == 'changed':
            res += format_changed(k, v, depth)[0]
            res += format_changed(k, v, depth)[1]
        elif v['type'] == 'unchanged':
            res += format_unchanged(k, v, depth)
        elif v['type'] == 'nested':
            res += format_nested(k, v, depth)
            for child in v['children']:
                res += walk(child, depth + 1)
            res += f'{indent * (depth)}}}\n'
    return res


def stylish(diff_tree: dict) -> str:
    depth = 1
    global indent
    indent = '    '
    
    if diff_tree == {}:
        return ''

    return '{\n' + walk(diff_tree, depth) + '}'
