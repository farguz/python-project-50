def check_type(element):
    if isinstance(element, (dict, list, set)):
        res = '[complex value]'
        
    if isinstance(element, str):
        res = f"'{str(element)}'"
        
    if isinstance(element, bool):
        return f"{str(element).lower()}"
        
    if element is None:
        res = 'null'
        
    if isinstance(element, (int, float)):
        res = f"{element}"
        
    return res


def format_added(v, new_path):
    return (f"Property '{new_path}' was added " + 
            f"with value: {check_type(v['value'])}\n")


def format_deleted(v, new_path):
    return (f"Property '{new_path}' was removed\n")


def format_changed(v, new_path):
    return (f"Property '{new_path}' was updated. From " + 
            f"{check_type(v['old_value'])} to " + 
            f"{check_type(v['new_value'])}\n")


def recurse_nested(v, new_path):
    inner_res = ''
    for child in v['children']:
        inner_res += walk_tree(child, new_path)
    return inner_res

def formatting_all_labels(res, k, v, path):
    new_path = path + '.' + str(k) if path else str(k)
    
    if v['type'] == 'added':
        res += format_added(v, new_path)
    elif v['type'] == 'deleted':
        res += format_deleted(v, new_path)
    elif v['type'] == 'changed':
        res += format_changed(v, new_path)
    elif v['type'] == 'nested':
        res += recurse_nested(v, new_path)
        '''elif v['type'] == 'unchanged':
            pass'''
    return res

def walk_tree(element, path=''):
    res = ''
    for k, v in element.items():
        res = formatting_all_labels(res, k, v, path)

    return res


def plain(diff_tree: dict) -> str:
    if diff_tree == {}:
        return ''

    return walk_tree(diff_tree).strip('\n')
