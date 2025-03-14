# from generate_diff_tree import generate_diff_tree, get_value_str 


def stylish(diff_tree: dict) -> str:
    def walk(element):
        for k, v in element.items():
            if v['type'] == 'added':
                print(f' + {k}: {v['value']}')
            elif v['type'] == 'deleted':
                print(f' - {k}: {v['value']}')
            elif v['type'] == 'changed':
                print(f' - {k}: {v['old_value']}')
                print(f' + {k}: {v['new_value']}')
            elif v['type'] == 'unchanged':
                print(f' * {k}: {v['value']}')
            elif v['type'] == 'nested':
                print(f' * {k}: {walk(v['value'])}')

    return walk(diff_tree)

'''for key in all_keys:
        if get_value_str(first_file, key) == get_value_str(second_file, key):
            res += ('    ' + key + ': ' + 
                    get_value_str(first_file, key) + '\n')
        else:
            if key in first_keys and key in second_keys:
                res += ('  - ' + key + ': ' + 
                        get_value_str(first_file, key) + '\n')
                res += ('  + ' + key + ': ' + 
                get_value_str(second_file, key) + '\n')            
            elif key in first_keys:
                res += ('  - ' + key + ': ' + 
                        get_value_str(first_file, key) + '\n')        
            else:
                res += ('  + ' + key + ': ' + 
                        get_value_str(second_file, key) + '\n')

    res = '{\n' + res + '}'
    return res'''
