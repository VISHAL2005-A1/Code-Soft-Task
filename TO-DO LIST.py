def quest():
    quests=[]
    print("Welcome to the TO DO LIST APP")
    total_quest = int(input("Enter number of quests you want to add : "))
    for i in range(1, total_quest+1):
        name_quest = input(f"Enter quests {i} :\t")
        quests.append(name_quest)
    print(f"Todays quests : {quests}")
    while True:
        actions = int(input("Enter\t \n 1-for : Add \n 2-for : Update\n 3- for : Delete \n 4-for : View\n 5-for : Exit"))
        if actions == 1:
            add = input("Enter the name of quest you want to add : ")
            quests.append(add)
            print("quest are added successfully")
        elif actions == 2:
            updated_value = input("Enter the name of quest you want to update")
            if updated_value in quests:
                up = input("Enter new quest: ")
                ind = quests.index(updated_value)
                quests.insert(ind,up)
                print(f"Updated quests, {up}")
        elif actions == 3:
            del_value = input("Name of quest you want to delete : ")
            if del_value in quests:
                ind = quests.index(del_value)
                del quests[ind]
                print(f"quest {del_value} has been deleted ....")
        elif actions == 4:
            print(f"Total quests is : {quests}")
        elif actions == 5:
            print("Closing the program")
        else:
            print("Invalid quest")
            
quest()
        