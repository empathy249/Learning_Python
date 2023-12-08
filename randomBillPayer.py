import random 

names = input("Names of the individuals separated by comma: ")
array = names.split(", ")
print (array)

#len function counts the items in array
partyOf = len(array)
print (partyOf)

#or you can run a for loop to count items in array
i = 0 
for name in array:
    i += 1

print (i)
upperLimit = i-1
randomNumber = random.randint(0,upperLimit)
print (randomNumber)
print(f"{array[randomNumber]} has been chosen randomly to pay the bill")