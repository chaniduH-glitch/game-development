matrix = [[1,2,3],[4,5,6],[7,8,9]] 
print(matrix)
#number of rows

print(len(matrix))
#number of columns in first row
print(len(matrix[0]))  
#access an element 
print(matrix[2][0])
print(matrix[0][1])
rows = int(input("enter the number of rows"))
colomns = int(input("enter the number of colomns"))
matrix = []
for i in range(rows):
    t = []
    for j in range(colomns):
        e = int(input("enter an element"))
        t.append(e) 
    matrix.append(t)
for i in range(rows):
    for a in range(colomns):
        print(matrix[i][a],end=" ")
    print()




      

