import random
word_list = ["banana", "apple", "plum", "grapefruit", "orange"]
print(word_list)
word = random.choice(word_list)
print(word)

def check_guess(guess): # checks if the letter is in the word
    guess = guess.lower()   # makes the letter lower case
    if guess in word:    # checks if letter is in word
        print(f"Good guess! {guess} is in the word.") # ends with correct guess
    else:
        print(f"Sorry, {guess} is not in the word. Try again.") # ends with incorrect guess

def ask_for_input():    # requires user to enter a letter
    while True: # infinitely loops until it breaks to run check_guess or prints invalid message and comes back here
        user_input = input("Please enter a single letter: " )
        if len(user_input) == 1 and user_input.isalpha():   # checks if the letter is a single character and an actual letter
             break  # if it is, breaks out of while loop and jumps to check_guess function
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") # if not, goes back to while and repeats
    check_guess(user_input) # takes the single character into the check_guess function
        
ask_for_input()

# initial code:
# while True:
#     guess = input("Please enter a single letter: " )
#     if len(guess) == 1 and guess.isalpha():
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")
# if guess in "apple":
#     print(f"Good guess! {guess} is in the word.")
# else:
#     print(f"Sorry, {guess} is not in the word. Try again.")