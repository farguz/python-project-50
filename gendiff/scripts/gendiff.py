from gendiff.parser import parsing
from gendiff.generate_diff_tree import generate_diff
import json


def main():
    args = parsing()
    generate_diff(args.first_file, args.second_file)
    

if __name__ == '__main()__':
    main()
