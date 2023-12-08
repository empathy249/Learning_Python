def prime_number_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0: 
            is_prime = False
    return is_prime

number = int(input("Type a number to check if it is prime number: "))
is_prime = prime_number_checker(number)

if is_prime == True:
    print(f"{number} is a prime number!")
else: 
    print(f"{number} is not a prime number!")
