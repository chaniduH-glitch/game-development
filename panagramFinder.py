#count the ocurrants of vowels of this string 
text = input("enter the string").lower()
vowels = ["a","e","i","o","u"]
dictV = {}
for i in text: 
    if i in  vowels:
        if i in dictV:
            dictV[i]+=1
        else: 
            dictV[i]=1
print(dictV) 

# count the occurants of alphabets in the string

text = input("enter the string").lower()
dict = {}
for i in text:
    if i.isalpha():
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
print(dict)


# check if the number entered by the user is panagram or not

number = input("enter a number")
dictn = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
for i in number:
    if i in dictn:
        dictn[i]+=1
p = True 
for i in dictn.values():
    if i == 0:
        p = False 
if p:
    print("entered number is a panagram")
else:
    print("it is not a panagram") 
    



            


