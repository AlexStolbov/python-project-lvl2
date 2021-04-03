#!/usr/bin/env python3
import sys
from gen_diff.cli import run


def main():
    res = run(sys.argv[1:])
    print(res)
