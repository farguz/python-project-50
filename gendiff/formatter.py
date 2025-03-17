# from generate_diff_tree import generate_diff_tree, get_value 


def stylish(diff_tree: dict) -> str:
    depth = 1
    replacer = '    '
    
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

    def walk(element, depth):
        res = ''
        for k, v in element.items():
            if v['type'] == 'added':
                res += (f'{replacer * (depth - 1)}  + {k}: {is_dict(v["value"], depth + 1)}\n')
            elif v['type'] == 'deleted':
                res += (f'{replacer * (depth - 1)}  - {k}: {is_dict(v["value"], depth + 1)}\n')
            elif v['type'] == 'changed':
                res += (f'{replacer * (depth - 1)}  - {k}: {is_dict(v["old_value"], depth + 1)}\n')
                res += (f'{replacer * (depth - 1)}  + {k}: {is_dict(v["new_value"], depth + 1)}\n')
            elif v['type'] == 'unchanged':
                res += (f'{replacer * (depth - 1)}    {k}: {is_dict(v["value"], depth + 1)}\n')
            elif v['type'] == 'nested':
                res += (f'{replacer * (depth - 1)}    {k}: {{\n')
                for child in v['children']:
                    res += walk(child, depth + 1)
                res += f'{replacer * (depth)}}}\n'
        return res

    return '{\n' + walk(diff_tree, depth) + '}'
