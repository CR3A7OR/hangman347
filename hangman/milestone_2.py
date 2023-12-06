#!/usr/bin/python3
import random

def main():
    word_list = ['oranges', 'banana', 'apple', 'pear', 'peach']
    word = random.choice(word_list)
    print(word)
    guess = input("Please enter a single letter: ")
    if (len(user_input) == 1 and user_input.isalpha()):
        print("Good Guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()

