from gendiff.formatter import choose_format
from gendiff.generate_diff_tree import generate_diff_tree
from gendiff.parser import parsing


def generate_diff(first_file: str, second_file: str, format: str = 'stylish'):
    
    diff_tree = generate_diff_tree(first_file, second_file, format)
    return choose_format(diff_tree, format)


def main():
    args = parsing()
    print(generate_diff(args.first_file, args.second_file, args.format))
    

if __name__ == '__main()__':
    main()
