dict1 = {}

while True: 


    print("1.insert")
    print("2.display all countries")
    print("3. display all capitals")
    print("4.get capital")
    print("5. delete")

    option = input("what number do you want to choose?")
    if option == "1":
        country1 = input("enter the country name") 
        value1 = input("enter the capital")
        dict1[country1] = value1 
    elif option == "2":
        print(dict1.keys())
    elif option == "3":
        print(dict1.values())

    elif option == "4": 
        capital = input("what country's capital do you want to display?").lower()
        print(dict1[capital])
    elif option == "5":
        delete = input("what country do you want to delete?").lower()
        dict1.pop(delete)  
        

        










    

    