import argparse
from gendiff.gen_diff import generate_diff


def run(args):
    parsed_args = parse_args(args)
    res = generate_diff(parsed_args.first_file,
                        parsed_args.second_file,
                        parsed_args.format)
    return res


def parse_args(args):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args(args)
