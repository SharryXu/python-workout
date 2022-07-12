#!/usr/bin/env python3
'''
Write a custom sum function.
sum([1, 2, 3])
sum(1, 2, 3)
sum(10, 20, 30)
'''


def sum(*args):
    amount = 0
    if len(args) > 1:
        for item in args:
            amount += item
    elif type(args) is tuple:
        for item in args[0]:
            amount += item

    return amount

if __name__ == "__main__":
    print(sum([1, 2, 3]))
    print(sum(1, 2, 3))
    print(sum(*[1, 2, 3]))



