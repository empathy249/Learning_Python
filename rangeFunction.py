rangeNumber = range(1, 101, 1)
sum = 0 
for number in rangeNumber:
    sum = sum + number
    #print (sum)

#only add even numbers 

sum2 = 0 

for number in range(2, 101, 2):
    sum2 += number
    #print (number)
    print (sum2)

sum3 = 0 
for number in rangeNumber: 
    if number % 2 == 0: 
        sum3 += number
    else: 
        print ("--")

print(sum3)