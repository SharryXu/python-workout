#!/usr/bin/env python3


def sum(l=None, *args):
    amount = 0
    if type(l) is list:
        for item in l:
            amount += item
    if type(l) is int:
        amount += l

    if type(args) is int:
        amount += args
    elif args is not None:
        if len(args) > 1:
            for item in args:
                if type(item) is int:
                    amount += item
                elif type(item) is list:
                    for item_level_2 in item:
                        amount += item_level_2
        elif type(args) is tuple and len(args) > 0:
            if type(args[0]) is int:
                amount += args[0]
            else:
                for item in args[0]:
                    amount += item

    return amount
