def get_value_str(dict, key):
    if dict.get(key) is True:
        return 'true'
    if dict.get(key) is False:
        return 'false'
    return str(dict.get(key))
    
    
def plain(first_file, second_file):
    first_keys = list(first_file)
    second_keys = list(second_file)
    all_keys = list(set(first_keys + second_keys))
    all_keys.sort()
    
    res = ''

    for key in all_keys:
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

    return res
