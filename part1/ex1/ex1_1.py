#!/usr/bin/env python3

import random


def guessing_game():
    answer = random.randint(1, 30)
    guess_count = 0
    max_guess_count = 5

    while guess_count < max_guess_count:
        user_guess = int(input("What's your guess?\n"))

        if user_guess > answer:
            print(f"You guess {user_guess} is too big!")
        elif user_guess < answer:
            print(f"You guess {user_guess} is too low!")
        else:
            print(f"Congratulation! The answer is {answer}!")
            return

        guess_count += 1

    if guess_count == max_guess_count:
        print("You are out of chance!")


if __name__ == "__main__":
    guessing_game()
