#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', metavar='FORMAT', help='set format of output')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    print(first_file, second_file)


if __name__ == '__main__':
    main()
