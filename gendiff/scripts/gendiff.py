import argparse


def main():
    #print('line 1')

    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()

    #print('line 2')


if __name__ == '__main()__':
    main()
