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

def get_operation (number1, number2):
    for symbol in operation_string:
        print(symbol)
    user_operation_symbol = input(f"what do you want to do with {number1} and {number2}: ")
    math_operation = operation_string[user_operation_symbol]
    return math_operation

def perform_maths (number1 , number2, user_operation_symbol):
    answer_string_function = calculator(number1, number2, user_operation_symbol)
    return answer_string_function

def continue_calculator ():
    end_calculation = input("Want to continue operation? Y or N: ").lower()
    if end_calculation == "n":
        return False
    else: 
        return True
def print_answer (number1, number2, answer, operation):
    print(f"{number1} {operation} {number2} = {answer}")

num1 = float(input("What's the first number?; "))
num2 = float(input("What's the second number?: "))
math_operation = get_operation(num1, num2)
answer_string_function = perform_maths(num1, num2, math_operation)
print_answer(num1, num2, answer_string_function, math_operation)

continue_calculation = True
current_value = answer_string_function

while continue_calculation == True:
    continue_calculation = continue_calculator()
    if continue_calculation == True: 
        new_number = float(input("What is the new number? "))
        new_user_operation_symbol = get_operation(current_value, new_number)
        new_answer = perform_maths(current_value, new_number, new_user_operation_symbol)
        current_value = new_answer
        print_answer(current_value, new_number, new_answer, new_user_operation_symbol)
    else:
        break
    


