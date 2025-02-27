import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    first_file = json.load(open('gendiff/test_files/file1.json'))
    second_file = json.load(open('gendiff/test_files/file2.json'))
    print(first_file, second_file, sep='\n')

if __name__ == '__main()__':
    main()
