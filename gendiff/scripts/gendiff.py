#!/usr/bin/env python3
import sys
from gendiff.cli import run


def main():
    res = run(sys.argv[1:])
    print(res)
