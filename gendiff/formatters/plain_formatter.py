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
