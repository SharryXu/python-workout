#!/usr/bin/env python3

import random

answer_dict = [
    'a',
    'abc',
    'happy',
    'sharry',
]

def guessing_game():
    answer = answer_dict[random.randint(0, len(answer_dict))]

    while True:
        user_guess = input('What\'s your guess?\n')
        user_guess = user_guess.strip()

        if user_guess > answer:
            print(f'Your guess {user_guess} is too big!')
        elif user_guess < answer:
            print(f'Your guess {user_guess} is too low!')
        else:
            print('Congratulation!')
            break

if __name__ == '__main__':
    guessing_game()