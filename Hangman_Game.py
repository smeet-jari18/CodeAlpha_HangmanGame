'''

TASK 2: Hangman Game

Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
Simplified Scope:
. Use a small list of 5 predefined words (no need to use a file or API).
. Limit incorrect guesses to 6.
. Basic console input/output - no graphics or audio.
Key Concepts Used: random, while loop, if-else, strings, lists.

'''


import random

words = ["python", "computer", "apple", "program", "student", "hello"]

select_word = random.choice(words)

guesses_letter = []

wronge_guesses = 0

max_guesses = 6

print("============================================")
print("         Welcome To Hangman          ")
print("============================================")

while wronge_guesses < max_guesses:
    display_word = ""

    for letter in select_word:
        if letter in guesses_letter:
            display_word += letter + " "
    else:
        display_word += "_"

    print("\n word :",display_word)
    print("Wronge guesses: ",wronge_guesses,"/",max_guesses)

    if all(letter in guesses_letter for letter in select_word):
        print("Congratulation! You guess the word.")
        break

    guess = input("Guess one letter : ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please Enter Only One alphabet letter.")
        continue

    if guess in guesses_letter:
        print("you already guessed this letter.")
        continue
    
    guesses_letter.append(guess)

    if guess in select_word:
        print("Correct word")
    else:
        print("wronge guess")
        wronge_guesses +=1

else:
    print("\n You lost game.")
    print("The correct word was : ",select_word)
