# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

This is my first proper project and I learned how to use Classes.  Particularly understood how to pass variables in and out of the class using "instance of the object" (here game."variable").  The challenge for me was understanding what variables get passed into a Class from the input function and which variables are defined within the Class body.

My observation is that it is easier to program "linearly", ie. using a stream of functions that follow a stream of logic than create Classes.  Classes seem to be like constructions or "objects" that get used often but you have to know how to address them so you get required inputs and outputs from them.  And they are not "linear".

## Table of Contents

- Not required

## Installation instructions

origin is https://github.com/Kenard4/hangman.git

The code is contained in the milestone_5.py file.

## Usage instructions

Prepare a word list for the game to choose from (called "word_list") containing a list of strings.

Enter the whole list (here "word_list") and the number of lives (here "num_lives") as parameters into the instance of the class Hangman by creating a variable (here "game") with these parameters (like this game = Hangman(word_list, num_lives).

play_game is the function which is defined to call the game instance within the Hangman Class.

## File structure of the project

Nested within the Hangman Class are 2 functions: One to ask for the input letter (ask_for_input) and the other to check if the inputted letter is in the random word (check_guess).

## License information

I imported the "random" module
