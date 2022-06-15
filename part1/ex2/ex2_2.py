#!/usr/bin/env python3

def average(*args):
    amount, count = 0, 0

    for i in args:
        amount += i
        count += 1
    
    return amount / count