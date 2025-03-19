from gendiff.formatter import choose_format
from gendiff.generate_diff_tree import generate_diff_tree
from gendiff.parser import parsing


def main():
    args = parsing()
    diff_tree = generate_diff_tree(args.first_file, args.second_file,
                                   args.format)

    print(choose_format(diff_tree, args.format))
    

if __name__ == '__main()__':
    main()
