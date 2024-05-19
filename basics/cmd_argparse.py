#!/usr/bin/python3

import argparse

desc = "A script that takes commandline arguments."
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('arg1', type=int, help="First Argument")
parser.add_argument('arg2', type=str, help="File name")

args = parser.parse_args()

print("Argument 1: {}", args.arg1)
print("Argument 2: {}", args.arg2)
