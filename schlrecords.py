group_records =  []
for i in range(5):
    print("Enter details for Group Name:")
    groupname = (input("Enter Group Name"))
    sizeofgroup = int(input("Enter group size"))
    dateofcompetition =  input("Enter Date of the competition (YYYY-MM-DD): ")
    Venue = input("Enter Venue")
    TypeofMedal = input("Enter Type of Medal: ")
    group_record = (dateofcompetition,Venue,groupname,TypeofMedal,sizeofgroup)

    group_records.append(group_record)
    print("Record added successfully! \n")

print("\nRecorded Details of All Groups:") 
for i in group_records:
    print(i)


