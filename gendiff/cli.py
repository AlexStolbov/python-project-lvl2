import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args(args)
