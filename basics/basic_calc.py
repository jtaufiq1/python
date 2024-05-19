#!/usr/bin/python3

import argparse

# Argument parser
desc = "A basic command line calculator"
parser = argparse.ArgumentParser(description=desc)

# Define Arguments
parser.add_argument('oper1', type=int, help="First operand (integer)")
parser.add_argument('oper2', type=int, help="Second operand (integer)")
parser.add_argument('--add', action="store_true", help="perform addition")
parser.add_argument('--subtract', action="store_true", help="perform subtraction")
parser.add_argument('--multiply', action="store_true", help="perform multiplication")
parser.add_argument('--divide', action="store_true", help="perform division")

# Parse the arguments
args = parser.parse_args()

# Perform operations and store results
result = None
operation = ''
if args.add:
    result = args.oper1 + args.oper2
    operation = "addition"
elif args.subtract:
    result = args.oper1 - args.oper2
    operation = "subtraction"
elif args.multiply:
    result = args.oper1 * args.oper2
    operation = "multiplication"
elif args.divide:
    if args.oper2 == 0:
        print("Division by zero is allowed")
        result = None
    else:
        result = args.oper1 / args.oper2
        operation = "division"

if result is not None:
    print(f"Result of {operation} is: {result}")
