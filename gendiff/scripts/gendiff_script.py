#!/usr/bin/env python3
import argparse
from gendiff.engine.compare_files import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', metavar='FORMAT', help='set format of output')
    args = parser.parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)
