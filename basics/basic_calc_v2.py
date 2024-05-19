#!/usr/bin/python3

import argparse

# Argument parser
desc = "A basic command line calculator"
parser = argparse.ArgumentParser(description=desc)

# Define Arguments
parser.add_argument('--add', nargs=2, type=int, metavar=('NUM1','NUM2'), help="Add two numbers")
parser.add_argument('--sub', nargs=2, type=int, metavar=('NUM1','NUM2'), help="perform subtraction")
parser.add_argument('--mult', nargs=2, type=int, metavar=('NUM1','NUM2'), help="perform multiplication")
parser.add_argument('--div', nargs=2, type=float, metavar=('NUM1','NUM2'), help="perform division")
parser.add_argument('--exp', nargs=2, type=int, metavar=('NUM', 'EXPONENT'), help="")
parser.add_argument('--rem', nargs=2, type=float, metavar=('NUM1', 'NUM2'), help="")
parser.add_argument('--quot', nargs=2, type=float, metavar=('NUM1', 'NUM2'), help="")

# Parse the arguments
args = parser.parse_args()

# Perform operations and store results
result = None
operation = ''
if args.add:
    result = args.add[0] + args.add[1]
    operation = "addition"
elif args.sub:
    result = args.sub[0] - args.sub[1]
    operation = "subtraction"
elif args.mult:
    result = args.mult[0] * args.mult[1]
    operation = "multiplication"
elif args.exp:
    result = args.exp[0] ** args.exp[1]
    operation = "exponentiation"
elif args.div:
    if args.div[1] == 0:
        print("[ERROR] Division by zero is allowed")
    else:
        result = args.div[0] / args.div[1]
        operation = "division"
elif args.rem:
    if args.rem[1] == 0:
        print("[ERROR] Division by zero is not allowed")
    else:
        result = args.rem[0] % args.rem[1]
        operation = "remainder"
elif args.quot:
    if args.quot[1] == 0:
        print("[ERROR] Division by zero is not allowed")
    else:
        result = args.quot[0] // args.quot[1]
        operation = "quotient"
else:
    parser.print_help()

if result is not None:
    print(f"Result of {operation} is: {result}")
