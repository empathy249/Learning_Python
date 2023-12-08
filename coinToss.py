import random 

print("Welcome to ICC Cricket world cup Final 2023 between India and Australia")
print("Sachin Tendulkar is ready to toss the coin")
call = input("India calls: Heads or Tails? ").lower()
randomNumber = random.randint(0,1)
print(randomNumber)
if call == "heads" and randomNumber == 1:
    print(f"India called {call} winning the toss")
elif call == "tails" and randomNumber == 0:
    print(f"India called {call} winning the toss")
else: 
    print(f"Australia wins the toss")