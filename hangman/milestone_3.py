#!/usr/bin/python3
import random

def validate_input(user_input):
    if (len(user_input) == 1 and user_input.isalpha()):
        print("Good Guess!")
        return True
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return False


def check_guess(user_input,word):
    user_input = user_input.lower() 
    if user_input in word:
        print(f"Good guess! {user_input} is in the word")
    else:
        print(f"Sorry, {user_input} is not in the word. Try again.")


def ask_for_input():
    word_list = ['oranges', 'banana', 'apple', 'pear', 'peach']
    word = random.choice(word_list)
    input_check = True
    while True:
        guess = input("Please enter a single letter: ")
        if validate_input(guess):   
            check_guess(guess,word)
        else:
            pass

if __name__ == "__main__":
    ask_for_input()
