import argparse
import json
from collections import OrderedDict


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)
    
    

def generate_diff(file_path1: str, file_path2: str) -> str:
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))

    res = {}

    for k1 in first_file.keys():
        if k1 in second_file.keys():
            if first_file[k1] == second_file[k1]:
                res['  ' + k1] = first_file[k1]
            else:
                res['- ' + k1] = first_file[k1]
                res['+ ' + k1] = second_file[k1]
        else:
            res['- ' + k1] = first_file[k1]

    for k2, v2 in second_file.items():
        if k2 not in first_file.keys():
            res['+ ' + k2] = second_file[k2]

    res_sorted = dict(sorted(res.items(), key=lambda x: x[0][2:]))
    res_sorted_json = json.dumps(res_sorted)
    print(res_sorted_json)
    return res_sorted_json

if __name__ == '__main()__':
    main()
