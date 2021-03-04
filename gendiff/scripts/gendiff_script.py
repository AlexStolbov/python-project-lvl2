#!/usr/bin/env python3
import sys
import argparse
from gendiff.engine.compare_files import generate_diff


def main():
    args = parse_args(sys.argv[1:])
    res = generate_diff(args.first_file, args.second_file, args.format)
    print(res)


def parse_args(args):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args(args)
