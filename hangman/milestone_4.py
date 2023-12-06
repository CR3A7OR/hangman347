#!/usr/bin/python3
import random


'''
This class is used for the hangman game.

    Attributes:
        word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
        word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        num_lives: int - The number of lives the player has at the start of the game.
        word_list: list - A list of words
        list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

'''
class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self,user_input):
        '''
        This function checks the user's guess

        This will check if the user's guess is 
        within the word chosen for hangman and 
        handles the life counter
        '''
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

    def __validate_input(self,user_input):
        '''
        This function validates the user input

        This will take the user's input and check
        for two things. If it is a single letter
        and it hasn't already been guessed
        '''
        user_input = user_input.lower()
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
        '''
        This function asks for the user's input
        '''
        guess = input("Please enter a single letter: ")
        if self.__validate_input(guess):   
            self.check_guess(guess)
        else:
            pass
    
    def play_game(self):
        '''
        This function lets the user play the game
        '''
        while True:
            if (self.num_lives > 0 and self.num_letters > 0):
                self.ask_for_input()
            elif(self.num_lives > 0 and self.num_letters == 0 ):
                print("Won")
                break
            else:
                print("You lose")
                break


def main():
    word_list = ['oranges', 'banana', 'apple', 'pear', 'peach']
    num_lives = 5
    game = Hangman(word_list,num_lives)
    game.play_game()

if __name__ == "__main__":
    main()