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


def plain(diff_tree: dict) -> str:
    if diff_tree == {}:
        return ''

    def walk(element, path=''):
        res = ''
        for k, v in element.items():
            new_path = path + '.' + str(k) if path else str(k)

            if v['type'] == 'added':
                res += format_added(v, new_path)
            elif v['type'] == 'deleted':
                res += format_deleted(v, new_path)
            elif v['type'] == 'changed':
                res += format_changed(v, new_path)
            elif v['type'] == 'unchanged':
                pass
            elif v['type'] == 'nested':
                for child in v['children']:
                    res += walk(child, new_path)

        return res
    return walk(diff_tree).strip('\n')
