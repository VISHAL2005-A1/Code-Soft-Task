contact={}  
print("Welcome to the Contact Book App...") 
while True: 
    x = int(input("Enter\n 1-To Add Contact\n 2-To View Contact List\n 3-To Search Contact\n 4-To Update Contact\n 5-To Delete Contact\n")) 
print(x)  
    if x==1:
       print("You select 1 to add Contact:")
       name= input("Enter the name:\t")
       if name in contact:
         print(f"name{name} is already added: ")
       else:
         phone_number= int(input("Enter the phone_number:\t"))
         email= input("Enter the email:\t")
         address = input("Enter the adderss:\t")
         print("Contact Information created Successfully")   
         contact[name]= {"phone_number":int(phone_number),"email":(email),"address":(address)}
    elif x == 2:
        print("You select 2 to view contact:")
        name=input("Enter contact name to view contact list:\t")
        if name in contact:
            print(contact[name])
        else:
           print("Contact not Exist")   
           print(" Please Create a new Contact")
    elif x == 3:
        print("You select 3 to search contact:")
        name=input("Enter the name to search contact:\t")
        if name in contact:
            print(contact[name])
        else:
            print("No Contact Found")   
    elif x == 4:
            print("You select 4 to update contact:")
            name=input("Enter name to update contact:\t")
            if name in contact:
               phone_number = int(input("Enter updated phone_number:"))
               email= input("Enter updated email:\t")
               address = input("Enter updated address:\t")
               contact[name]= {"phone_number":int(phone_number),"email":(email),"address":(address)}
            else:
                print("Contact not found")   
            print("Contact updated successfully")
    elif x == 5:
            name=input("Enter name to delete contact:\t")
            if name in contact:
               del contact[name]
               print("Contact not found")
               print("Contact Deleted successfully")
              
    
