#Password Generator Project

import random

# arrays 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

userPasswordLength = int(input("How many letters would you like in your password?"))
userNumber = int(input("How many numbers would you like in your password?"))
userSymbol = int(input("How many symbols would you like in your password?"))

# count - 1 for the arrays 
arrayCountLetters = len(letters) - 1 
arrayCountNumbers = len(numbers) - 1 
arrayCountSymbols = len(symbols) - 1 
userLetter = userPasswordLength - userNumber - userSymbol
# userLetterCount = userLetter - 1
# userNumberCount = userNumber - 1
# userSymbolCount = userSymbol - 1 

password = []
strongPassword = ""

for count in range(0, userLetter):
    randomNumberLetters = random.randint(0, arrayCountLetters)
    character = letters[randomNumberLetters]
    password.append(character)

for count2 in range(0, userNumber):
    randomNumber = random.randint(0, arrayCountNumbers)
    character = numbers[randomNumber]
    index = len(password) - 1
    randomNumberInsert = random.randint(0, index)
    password.insert(randomNumberInsert, character)

for count3 in range(0, userSymbol):
    randomNumberSymbols = random.randint(0, arrayCountSymbols)
    character = symbols[randomNumberSymbols]
    index = len(password) - 1
    randomSymbolInsert = random.randint(0, index)
    password.insert(randomSymbolInsert, character)

for character in password:
    strongPassword += character

print(strongPassword)

#easy method using shuffle 
print(password)
random.shuffle(password)
shuffle = random.shuffle(password) # will return None because you cannot store it in a new variable; it shuffles the password array itself 
print(password)
shuffle2 = random.sample(password,len(password)) # to create the shuffle and store it into a new variable using this 
print (shuffle2)