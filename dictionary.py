dict1 = { "a" : 1 , "b": 2, "c" : 3 }
print(dict1)
list1 = ["a","tree","apple","book","orange"]
print(list1[2])
#get the value with the help of key {"key":value}
print(dict1["b"])
print(dict1["c"])

# add a key value pair to the dictionary 

dict1["apple1"] = 4
print(dict1)


dict1["name"] = "apple"
print(dict1)

# update a value in the dictionary
dict1["apple1"] = 5
print(dict1)

# remove key value pairs from the dictionary 

dict1.pop("apple1")
print(dict1)

# display all the keys 

print(dict1.keys())

# disp;ay all the values
print(dict1.values()) 