#!/bin/python3
#https://docs.python.org/3/howto/argparse.html

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", help="Set verbosity [1/0]", action="store_true")
parser.add_argument("-s", "--set", help="Set N value", type=int)

args = parser.parse_args()
print(args.verbose)
print(args.set)
