import random

class Hangman:
   
    def __init__ (self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # random selection from imported list of words
        self.word_guessed = ["_"] * len(self.word) # initially _ equal to number of letters in the random word
        self.num_letters = len(set(self.word)) # The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives # The number of lives the player has at the start of the game.  Default = 5
        self.word_list = word_list # A list of words imported from function call
        self.list_of_guesses = [] # A list of the guesses that have already been tried. Set this to an empty list initially
        #global list_of_guesses
    
    def check_guess(self, guess):
        guess = guess.lower()   # makes the letter lower case
        if guess in self.word:    # checks if letter is in generated random word
            print(f"Good guess! {guess} is in the word.") # ends with correct guess
            for x in range(len(self.word)): # now looking to see where the correctly guessed letter is in the random word
                if self.word[x] == guess: # if the letter in the index (looping from 0 to length of random word) is equal to the correctly guessed letter,
                    self.word_guessed[x] = guess # then enter the correctly guessed character instead of "_" at the index of word_guessed
            print(self.word_guessed) # show how many letters have been guessed in the set of "_"'s
            self.num_letters -= 1 # reduce number of letters left to guess by 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.") # ends with incorrect guess
            self.num_lives -= 1 # lose a life
            print(f"You have {self.num_lives} lives left") # lives left counter
        
    def ask_for_input(self):
        while True: # infinitely loops until it breaks to run check_guess or prints invalid message and comes back here
            guess = input("Please enter a single letter: " )
            if len(guess) != 1 and guess.isalpha():   # checks if the letter is NOT a single character AND an actual letter
                print("Invalid letter. Please, enter a single alphabetical character.") # goes back to while and repeats
            elif guess in self.list_of_guesses: # if it is a viable entry, has it been used before?
                print("You already tried that letter!") # if so, go back to while and ask for another letter
            else:
                Hangman.check_guess(self, guess) # if it has got this far, call check_guess function with new letter
                self.list_of_guesses.append(guess) # add the guessed letter to the list of letters that have been tried
                print(self.list_of_guesses) # show the player what letters they have tried
       
hang = Hangman(["banana", "apple", "plum", "grapefruit", "orange"], 3)
hang.ask_for_input()