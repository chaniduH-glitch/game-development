#known as packing of values
my_tuple = (1,2,3,4)
for i in my_tuple:
    print(i,end = " ")

# how to unpack the values
a,b,c,d = my_tuple
print()
print(a)
print(b)
print(c)
print(d)

my_tuple = 1,2,3,4
print(my_tuple)
print(my_tuple[1])

#nested tuple
my_tuple = 1,2,3,4,("apple","banana","orange")
print(my_tuple[4][1]) 

#access elements using slicing 
new_tuple = ("apple","pen","pineapple","book",2,4,6,8)
print(new_tuple[1:4])
print(new_tuple[3:8])

#printing the whole tuple   
print(new_tuple[:])

#changing tuple values
#new_tuple[2]="orange"

#we cannot change/update/add/delete anything anything in the tuple 
new1_tuple = ("science","chemistry","physics",["biology","art","maths"])
new1_tuple[3][2]="science"
print(new1_tuple)

 