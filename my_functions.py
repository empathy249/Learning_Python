import os 

def clear_terminal_keep_lines(): 
      """Clears the python terminal \n
      Leaves the original number of lines as blank lines"""
      os.system('cls' if os.name == 'nt' else 'clear')
      print('\n' * os.get_terminal_size().lines)

def clear_terminal(): 
     """Clears the python terminal"""
     os.system('cls' if os.name == 'nt' else 'clear')

def check_if_prime(number):
      """Checks if the number is a prime number \n
      Returns True or False value"""
      data_type = type(number)
      print(data_type)
      if data_type == int:
        is_prime = False
        for i in range(2, number):
                if number % i == 0: 
                    is_prime = False
        return is_prime
      else: 
           print("Data type error. Please only enter number. ")
    

