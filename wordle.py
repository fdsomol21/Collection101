#wordle
#Create a wordle-like game that allows the user to guess the seceret word
#init
import random
possible = ["apple", "brush", "grape", "cigar", "fresh",
            "adobe", "floss", "helix", "flesh", "linen", "forth", "first", "stand", "ivory"]
word = random.choice(possible)
#func
def check(guess, word):
    outcome = ["◻️"]*5
    letters = list(word)
    for i in range(5):
        if guess[i] == word[i]:
            outcome[i] = "🟩"
    for i in range(5):
         if outcome[i] == "◻️" and guess [i] in letters:
              outcome[i] = "🟨"
              letters[letters.index(guess[i])] = None
    return"".join(outcome)
#main
print("Welcome to Wordle!!")
print("You have 6 tries to guess the 5 letter seceret word:")
print("A green box means the letter is in the right place, a yellow box indicates the correct letter in the wrong spot, and a white box means that letter is not in the word...\nBe careful, a letter may be used more than once!")
attempts = 6 #gives the user 6 attempts
win = False # this identifies that they have not guessed the word, and when they do guess it, it goes to true
while attempts > 0 and not win: #this means that while they still have attempts and have not guessed the word, the program will run
    guess = input("Enter your five letter word guess: ").lower()
    if len(guess) != 5: # if the length is not 5, they get a message stating that they must enter a five letter word.
        print("Your guess must be five letters!")
        continue
    returned = check(guess, word)
    print(f"Result: {returned}")
    attempts -= 1
    if guess == word:
        print(f"You won the game! The word was {word}")
        win = True
if not win:
        print(f"You lost, the word was {word}")
# Sources
# All emojis (the colored squares) from:
# Emojipedia.org
# https://emojipedia.org/
