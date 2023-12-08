from prettytable import PrettyTable

table = PrettyTable()
table.align = "r"

table.add_column("Pokemon name", ["Pikachu", "Balbasur", "Charizard"])
table.add_column("Quality", ["Electricity", "Grass", "Fire"])
table.border = False
print(table)

table.border = True
print(table)