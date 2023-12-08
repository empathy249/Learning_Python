states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", 
"North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
"Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
"Texas", "'Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
"Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#delaware is [0]
#new jersey is [2]
#hawaii is [-1]
#alaska is [-2]

question = int(input("Which state joined the union at #"))
state = question - 1 
print(f"{states_of_america[state]} is the {question} state to join the union")

countries_visited = ["India", "USA", "Canada"]
countries_visited.append("Mexico")
print(countries_visited)