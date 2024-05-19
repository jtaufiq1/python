#!/usr/bin/python3

import argparse

# Argument parser
desc = "A basic command line calculator"
parser = argparse.ArgumentParser(description=desc)

# Define Arguments and operations
operations = ['add', 'sub', 'mult', 'exp', 'div', 'rem', 'quot']

parser.add_argument('oper', choices=operations, help="Operation to perform")
parser.add_argument('operand1', type=float, help="Perform operation on two operands")
parser.add_argument('operand2', type=float, help="Perform operation on two operands")

# Parse the arguments
args = parser.parse_args()

# Perform operations and store results
result = None
operation = ''
if args.oper == 'add':
    result = args.operand1 + args.operand2
    operation = "addition"
elif args.oper == 'sub':
    result = args.operand1 - args.operand2
    operation = "subtraction"
elif args.oper == 'mult':
    result = args.operand1 * args.operand2
    operation = "multiplication"
elif args.oper == 'exp':
    result = args.operand1 ** args.operand2
    operation = "exponentiation"
elif args.oper == 'div':
    if args.operand2 == 0:
        print("[ERROR] Division by zero is not allowed")
    else:
        result = args.operand1 / args.operand2
        operation = "division"
elif args.oper == 'rem':
    if args.operand2 == 0:
        print("[ERROR] Division by zero is not allowed")
    else:
        result = args.operand1 % args.operand2
        operation = "remainder"
elif args.oper == 'quot':
    if args.operand2 == 0:
        print("[ERROR] Division by zero is not allowed")
    else:
        result = args.operand1 // args.operand2
        operation = "quotient"
else:
    parser.print_help()

if result is not None:
    print(f"Result of {args.oper} is: {result}")
