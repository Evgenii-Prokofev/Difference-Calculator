#!/usr/bin/env python3

import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()  # noqa: F841
    diff = generate_diff('gendiff/file1.json', 'gendiff/file2.json')
    print(diff)


if __name__ == "__name__":
    main()
