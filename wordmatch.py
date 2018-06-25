
import random
from random import choice

# Boolean
answer = 0

# Attempts
attempts = 0

# Hint
hint = 0

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


# TODO Pick out random characters from wordListed and store them in a separate string
# First Hint
hintOne = wordLenght / 4
hintOneInt = int(hintOne)
print(hintOneInt)

# TODO Combine each of theese into on hint wich gradually increases
# Second Hint
hintTwo = wordLenght / 2
hintTwoInt = int(hintTwo)
print(hintTwoInt)

# Third Hint
hintThree = wordLenght - 1
hintThreeInt = int(hintThree)
hintThreeTempInt = hintThreeInt
hintThreeTemp = list(word)

while hintThreeTempInt > 0:
    # Remove 1 point each run
    hintThreeTempInt = hintThreeTempInt - 1
    print(hintThreeTempInt)
    # Pick out random letters and remove them from an array
    randomThreeTemp = random.choice(hintThreeTemp)
    hintThreeTemp.remove(randomThreeTemp)

    print(hintThreeTemp)



print(hintThreeInt)

print("wordlisted: " + str(wordListed))
print("temp wordlisted: " + str(hintThreeTemp))

while answer < wordLenght:

    userInput = input()

    if userInput != "" and len(userInput) == 1 and userInput in word:
        print("nice")
        # if input success
        answer = answer + 1
        wordListed.remove(userInput)
        print(wordListed)

    # TODO 3 diffrent hints with random characters
    elif userInput == "hint":
        hint = hint + 1

    elif hint == 1:
        print()
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
