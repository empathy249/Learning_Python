userInput = input("Enter height of the team: ")
heightList = userInput.split()
sum = 0 
team = 0 
tempHeight = 0 
i = 0 
for height in heightList: 
    sum = sum + int(height) 
    team = team + 1 

averageHeight = sum/team
print (f"average height is {averageHeight}")

for height in heightList: 
    if int(height) > tempHeight: 
        tempHeight = int(height)
    else: 
        i = i + 1 

print(f"The tallest height is {tempHeight}")