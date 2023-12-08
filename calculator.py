import math
import my_functions

operation_string = {
    "+": "add", 
    "-": "substract", 
    "*": "multiply", 
    "/": "divide",
}


def calculator(number1, number2, math_operation):
    """Performs mathematics using two numbers and user defined operation"""
    if math_operation == "add":
        return number1 + number2
    elif math_operation == "substract":
        if number1 > number2:
            return number1 - number2
        else:
            return number2 - number1
    elif math_operation == "multiply":
        return number1 * number2
    elif math_operation == "divide":
        return number1 / number2


num1 = int(input("What's the first number?; "))
num2 = int(input("What's the second number?: "))
for symbol in operation_string:
    print(symbol)
user_operation_symbol = input(f"what do you want to do with {num1} and {num2}: ")
math_operation = operation_string[user_operation_symbol]
answer_string_function = calculator(num1, num2, math_operation)

### method 2 
def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

math_operation2 = operations[user_operation_symbol]
answer_function = math_operation2(num1, num2)
print(f"The answer is {answer_function}")