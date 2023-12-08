name1 = input("What is your name? ")
name2 = input("What is their name? ")

combine = name1 + name2
coupleLower = combine.lower()

t = coupleLower.count("t")
r = coupleLower.count("r")
u = coupleLower.count("u")
e = coupleLower.count("e")

firstDigit = str(t+r+u+e)


l = coupleLower.count("l")
o = coupleLower.count("o")
v = coupleLower.count("v")
e = coupleLower.count("e")

secondDigit = str(l+o+v+e)

score = int(firstDigit+secondDigit)
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")