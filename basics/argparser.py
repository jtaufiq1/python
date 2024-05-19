#!/usr/bin/python3

from argparse import *

# Create Argumentparser object
desc = "Command line script with arguments"
parser = ArgumentParser(description = desc)

# Define command line arguments
parser.add_argument('positional_arg', type=int, help='Positional Argument')
parser.add_argument('--optional_arg', type=str, help='Optional Argument')

# Parse the command line arguments
args = parser.parse_args()

# Access the arguments
print("Positional argument value:", args.positional_arg)
print("Optional argument value:", args.optional_arg)
