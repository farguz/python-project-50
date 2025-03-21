from gendiff.formatter import choose_format
from gendiff.generate_diff_tree import generate_diff_tree
from gendiff.parser import parsing


def generate_diff(format):
    
    diff_tree = generate_diff_tree(args.first_file, args.second_file)
    print(choose_format(diff_tree, format))


def main():
    global args
    args = parsing()
    generate_diff(args.format)
    

if __name__ == '__main()__':
    main()
