# from generate_diff_tree import generate_diff_tree, get_value_str 


def stylish(diff_tree: dict) -> str:
    depth = 1
    replacer = '===='
    def walk(element, depth):
        res = '{'
        for k, v in element.items():
            if v['type'] == 'added':
                res += (f'\n {replacer * depth} + {k}: {v['value']}')
            elif v['type'] == 'deleted':
                res += (f'\n {replacer * depth} - {k}: {v['value']}')
            elif v['type'] == 'changed':
                res += (f'\n {replacer * depth} - {k}: {v['old_value']}')
                res += (f'\n {replacer * depth} + {k}: {v['new_value']}')
            elif v['type'] == 'unchanged':
                res += (f'\n {replacer * depth} * {k}: {v['value']}')
            elif v['type'] == 'nested':
                res += (f'\n {replacer * depth} * {k}: {walk(v['value'], depth + 1)}')
        return res

    return walk(diff_tree, depth)

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
