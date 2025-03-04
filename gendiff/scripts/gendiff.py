from gendiff.generate_diff_tree import generate_diff_json
from gendiff.parser import parsing


def main():
    args = parsing()
    generate_diff_json(args.first_file, args.second_file)
    

if __name__ == '__main()__':
    main()
