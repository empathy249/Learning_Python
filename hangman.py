import random

word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
def arrayToString(array): 
    word = ""
    for letter in array: 
        word += letter
    return word

def stringToArray(string):
    array = []
    for letter in string:
        array.append(letter)
    return array

def createOutputArrayContainer(count, text):
    array = []
    i = 0 
    for i in range(0, count):
        array.append(text)
    return array


#Todo-1 randomly choose a word for the game 
count = len(word_list) - 1
randomNumber = random.randint(0, count)
gameWord = word_list[randomNumber]
gameWordArray = stringToArray(gameWord)
gameWordCount = len(gameWord)
print(f"Answer is {gameWord}")
# easy way to do it => chosen_word = random.choice(word_list)|

gameOutputArray = createOutputArrayContainer(gameWordCount, "_")
gameOutput = arrayToString(gameOutputArray)
print(f"Guess the Word:\n{gameOutput}\n")

#Todo-2 - Ask the user to guess a letter
#Todo-3 - Check if the letter the user guessed
#Todo-4 For each letter in the chosen_word, add a "_" to display
currentStage = ""
guess = ""
i = 0 
gameAns = gameOutputArray
lives = 7
while gameAns != gameWordArray and lives != 1:
    guess = input("Guess a letter: ").lower()
    b = 0 
    if gameWordArray.__contains__(guess):
        print (gameWordArray.__contains__(guess))
        for character in gameWordArray:
            if character == guess:  
                gameAns[b] = gameWordArray[b]
                b += 1
            else:
                b += 1
    else: 
            print (gameWordArray.__contains__(guess))
            lives -= 1
            print (lives)

    if lives != 1:
        gameOutput = arrayToString(gameAns)
        print(stages[lives-1])
        print(gameOutput)
    else: 
        gameOutput = arrayToString(gameAns)
        print(stages[lives-1])
        print(gameOutput)
        print("Sorry you lost!")


        


