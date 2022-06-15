#!/usr/bin/env python3

import random
from audioop import reverse
from math import pow


def guessing_game():
    answer = random.randint(1, 30)
    guess_count = 0
    max_guess_count = 5

    while guess_count < max_guess_count:
        user_guess = int(input("What's your guess?\n"))

        user_guess_list = dict(
            {
                10: user_guess,
                16: base16_to_base10(user_guess),
                8: base8_to_base10(user_guess),
            }
        )

        for base, value in user_guess_list.items():
            if value > answer:
                print(f"You guess {value}:{base} is too big!")
            elif value < answer:
                print(f"You guess {value}:{base} is too low!")
            else:
                print(f"Congratulation! The answer is {answer}!")
                return

        guess_count += 1

    if guess_count == max_guess_count:
        print("You are out of chance!")


def baseN_to_base10(a, n):
    raw = custom_reverse_str(str(a))
    amount = 0
    for i in range(len(raw)):
        num = int(raw[i])
        if num >= n:
            return -1
        amount += num * (n**i)
    return amount


def base16_to_base10(a):
    return baseN_to_base10(a, 16)


def base8_to_base10(a):
    return baseN_to_base10(a, 8)


def custom_reverse_str(str):
    return str[-1 : -len(str) : -1] + str[0]


if __name__ == "__main__":
    guessing_game()
