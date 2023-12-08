lists = ["pie", "cake", "cookie"]
dictionaries = {
    "pie" : "crust with filling",
    "cake" : "layers of bread and cream",
    "cookie" : "dough and butter baked with sugar",
}

dictionaries["brownie"] = "dough, butter, and cocao baked with sugar"

print(dictionaries["cookie"])

# for loops only gives us keys
for key in dictionaries:
    print(key) #pie, cake, cookie, brownie
    
    #to also print value 
    value = dictionaries[key]
    print(value)
