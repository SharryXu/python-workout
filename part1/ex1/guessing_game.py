#!/usr/bin/env python3

import random


def guessing_game():
    answer = random.randint(1, 30)

    while True:
        user_guess = int(input("What's your guess?\n"))

        if user_guess > answer:
            print(f"You guess {user_guess} is too big!")
        elif user_guess < answer:
            print(f"You guess {user_guess} is too low!")
        else:
            print(f"Congratulation! The answer is {answer}!")
            break


if __name__ == "__main__":
    guessing_game()
