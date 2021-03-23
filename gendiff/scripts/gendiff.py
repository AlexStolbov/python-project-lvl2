#!/usr/bin/env python3
import sys
from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff


def main():
    parsed_args = parse_args(sys.argv[1:])
    res = generate_diff(parsed_args.first_file,
                        parsed_args.second_file,
                        parsed_args.format)
    print(res)
