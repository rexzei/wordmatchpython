import random
from random import choice

# Boolean
answer = 0

# Attempts
attempts = 0

# Hint
hint = 0
hintNegative = 3


# Array of Words
wordArray = ["book", "orange", "plant", "house", "computer", "grass"]

# Random Word
arrayLenght = len(wordArray)
wordNumber = random.randrange(0, arrayLenght)
word = wordArray[wordNumber]

# Get lenght of random word
wordLenght = len(word)

# List the word in a list
wordListed = list(word)


# Hint
def hintFunction(int):
    # Get 25%, 50%, 75% of letters
    if hint < 4:
        print("You got: " + str(hintNegative) + " left")
        lenghtHint = wordLenght / 4 * int
        print(lenghtHint)
    else:
        print("You are out of hints")

while answer < wordLenght:

    userInput = input()

    if userInput != "" and len(userInput) == 1 and userInput in word:
        print("nice")
        # if input success
        answer = answer + 1
        wordListed.remove(userInput)
        print(wordListed)a

    # TODO 3 diffrent hints with random characters
    elif userInput == "hint":
        hint = hint + 1
        hintNegative = hintNegative - 1
        hintFunction(hint)

    elif userInput == word:
        break

    elif userInput == "":
        print("type something")
        # if no input

    elif len(userInput) > 1:
        print("only one character at a time")
        # if more than 1 character

    else:
        print("try again")
        # if wrong input

print("Congratulations!, the word was: " + word)
