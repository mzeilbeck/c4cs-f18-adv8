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
def LOL():
    print("Hey did you see the video of the Uber driver who had several Ottawa Senators as passengers?")
    print("The players were trash talking their organization. It's sooooo funny. What a dumpster fire of an organization.")
    print("I think Matt Duchene said something about how he doesn't pay attention to team meatings and that their coach doesn't teach them anything.")
    print(calculate("6 7 *")
    print("Even the Senators' own players know their team and organization suck.")
def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
    LOL()
