#!/usr/bin/python3
import random

def validate_input(user_input):
    if (len(user_input) != 1 or user_input.isnumeric()):
        print("Oops! That is not a valid input.")
        return True
    else:
        print("Good Guess!")
        return False


def main():
    word_list = ['oranges', 'banana', 'apple', 'pear', 'peach']
    word = random.choice(word_list)
    input_check = True
    while input_check == True:
        guess = input("Please enter a single letter: ")
        input_check = validate_input(guess)

if __name__ == "__main__":
    main()

