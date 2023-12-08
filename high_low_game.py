import random 

def pick_a_number():
    number = random.randint(1, 100)
    return number

def check_high_or_low(user_guess, number):
    array = [""]
    if user_guess == number: 
        array = ["You picked the right number. You win.", "True"]
        return array
    elif user_guess > number: 
        array = ["Too high.", "False"]
        return array
    elif user_guess < number: 
        array = ["Too low.", "False"]
        return array
    else: 
        return array

def start_game(difficulty_level, random_number):
    if difficulty_level == "easy":
        # get 10 trys
        i = 1
        while i < 11:
            user_guess = int(input("Take a guess: "))
            check = check_high_or_low(user_guess, random_number)
            if check[1] == "True": 
                i = 15
                print(check[0])
            else: 
                print(check[0])
                print(f"Number of tries left: {10-i}")
                i += 1
        if i == 11: 
            print(f"Sorry you lost. The correct answer was {random_number}.")
    elif difficulty_level == "hard":
        # get 5 trys
        i = 1
        while i < 6:
            user_guess = int(input("Take a guess: "))
            check = check_high_or_low(user_guess, random_number)
            if check[1] == "True": 
                i = 15
                print(check[0])
            else: 
                print(check[0])
                print(f"Number of tries left: {5-i}")
                i += 1
        if i == 6: 
            print(f"Sorry you lost. The correct answer was {random_number}.")
    
difficulty = input("Guess the number I have picked between 1 -- 100\nWould you like to play easy or hard? ").lower()
start_game(difficulty, pick_a_number())