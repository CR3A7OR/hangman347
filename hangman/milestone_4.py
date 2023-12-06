#!/usr/bin/python3
import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self,user_input):
        user_input = user_input.lower() 
        if user_input in self.word:
            print(f"Good guess! {user_input} is in the word")
            for index,letter in enumerate(self.word):
                if (letter == user_input):
                    self.word_guessed[index] = letter
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            print(f"Sorry, {user_input} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def validate_input(self,user_input):
        if (len(user_input) == 1 and user_input.isalpha() and user_input not in self.list_of_guesses):
            print("Good Guess!")
            self.list_of_guesses.append(user_input)
            return True
        elif (user_input in self.list_of_guesses):
            print("You already tried that letter!")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            if self.validate_input(guess):   
                self.check_guess(guess)
            else:
                pass




def main():
    word_list = ['oranges', 'banana', 'apple', 'pear', 'peach']
    num_lives = 3
    player = Hangman(word_list,num_lives)
    player.ask_for_input()

if __name__ == "__main__":
    main()