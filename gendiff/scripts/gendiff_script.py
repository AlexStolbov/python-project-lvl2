#!/usr/bin/env python3
import sys
import argparse
from gendiff.engine.compare_files import generate_diff


def main():
    parse_args(sys.argv[1:])


def parse_args(args):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f',
                        metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args(args)
    res = generate_diff(args.first_file, args.second_file, args.f)
    print(res)


if __name__ == '__main__':
    parse_args(['-f', 'format', 'file1', 'file2'])
    # parse_args(['format', 'file1'])
