#pseudorandom number generator 

import random 

randomNumber = random.randint(2,200)
randomNumberFloat = random.random() # between 0 and 1 but not including
randomFloat = random.uniform(2, 5) # between 2 and 5 
print(randomNumber)
print(randomFloat)