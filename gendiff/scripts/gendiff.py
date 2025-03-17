from gendiff.formatter import stylish
from gendiff.generate_diff_tree import generate_diff_tree
from gendiff.parser import parsing


def main():
    args = parsing()
    diff_tree = generate_diff_tree(args.first_file, args.second_file, args.format)
    print(stylish(diff_tree))
    

if __name__ == '__main()__':
    main()
