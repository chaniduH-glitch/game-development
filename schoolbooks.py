dict1 = { "english" : 150,"physics": 170,"maths" : 180 } 
dict1["physics"]= 200
print(dict1)

dict1["chemistry"]=160
print(dict1)
dict1["biology"]=140
print(dict1)

subj = input("enter a book from the dictionary")
if subj in dict1:
    print(dict1[subj])
else: 
    print("book not found")

print(dict1)

 

    


 
 








