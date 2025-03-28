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
