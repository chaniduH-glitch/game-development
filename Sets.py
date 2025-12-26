list = [1,1,2,2,3,4,5,6,7]
a = set(list)
print(a)
#accessing the elements 
#print(a[1])#it throws an error

#check if element exists within the set
if 4 in a:
    print("yes")
else:
    print("No")
#add an element to the set
a.add(8)
a.add(9)
print(a)
#removing elements
a.discard(1)
print(a)

a.remove(7)
print(a)

#set operations 
a = {2,3,5,7,8,9} 
b = {1,2,4,6,8,10}
# union = addition of sets 
print(a.union(b))
print(a | b)

#intersection = elements that are in both sets 

print(a.intersection(b))
print(a & b)

#difference = elements that are present in only one set 
print(a.difference(b))
print(a-b)

# symmetric difference = union - intersection 
print(a.symmetric_difference(b))
print(a^b)


