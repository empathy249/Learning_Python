import os 

def clear(): 
      os.system('cls' if os.name == 'nt' else 'clear')
      print('\n' * os.get_terminal_size().lines)