treasure = "🔶"
line1 = ["⚪️", "⚪️", "⚪️"]
line2 = ["⚪️", "⚪️", "⚪️"]
line3 = ["⚪️", "⚪️", "⚪️"]
map = [line1, line2, line3]
print ("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ").lower() # Where do you want to put the treasure?

# Write your code below this columnNew
columnNew = 0
rowNew = 0
i = True

# for loop to get each character from the position (hard way)
for positionKey in position: 
    if i ==True: 
        columnNew = positionKey
        print(columnNew)
        i = False
    elif i == False:
        rowNew = positionKey
        print (rowNew)
        i = True
    else: 
        print("error in loop")

# easier way to get character from word 
columnOld = position[0]
rowOld = position[1]

if columnNew == "a":
    if rowNew == "1":
        line1[0] = treasure #A1
    elif rowNew == "2":
        line2[0] = treasure #A2
    elif rowNew == "3":
        line3[0] = treasure #A3
    else: 
        print("error in columnNew A if statement")
elif columnNew == "b":
    if rowNew == "1":
        line1[1] = treasure #B1
    elif rowNew == "2":
        line2[1] = treasure #B2
    elif rowNew == "3":
        line3[1] = treasure #B3
    else: 
        print("error in columnNew B if statement")
elif columnNew == "c":
    if rowNew == "1":
        line1[2] = treasure #C1
    elif rowNew == "2":
        line2[2] = treasure #C2
    elif rowNew == "3":
        line3[2] = treasure #C3
    else: 
        print("error in columnNew C if statement")
else: 
    print ("error in main if statement or out of index A/B/C")


# 3 Don't change the code below
print(f"{line1}\n{line2}\n{line3}")

# london app brewery solution 

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = treasure

print(f"{line1}\n{line2}\n{line3}")What to learn next

