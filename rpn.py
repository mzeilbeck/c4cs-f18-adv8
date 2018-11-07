#!/usr/bin/env python3
import operator

op = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
        }
def calculate(arg):
    # stack for calculator
    # tokenize input
    tokens = arg.split()
    stack = []
    # do tokens
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()

            # Look up function in table
            func = op[token]
            result = func(val1, val2)
            stack.append(result)
    return stack[-1]

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
