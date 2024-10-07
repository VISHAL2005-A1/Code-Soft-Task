while True:
   import random 
   name= input("Enter your good name:")
   print(f"Hello {name} Welcome to the rock-paper-scissor Game...")
   item_list = ["rock","paper","scissor"]
   user_choice = input("Enter your choice (rock-paper-scissor):")
   comp_choice = random.choice(item_list)
   if user_choice==comp_choice:
       print(f"Computer choice is {comp_choice}")
       print("It's a tie!")
   
   elif user_choice =="rock":
       if comp_choice =="scissor":
           print(f"Computer choice is {comp_choice}")
           print("hurray! you Win:")
       else:
           print("You lose:")
   elif user_choice=="paper":
       if comp_choice=="scissor":
           print(f"Computer choice is {comp_choice}")
           print("You lose")
       else:
           print("hurray! you Win:")
   elif user_choice=="scissor":
       if comp_choice=="paper":
           print(f"Computer choice is {comp_choice}")
           print("hurray! you Win:")
       else:
           print("You lose:")
   play_again = input("Do you want to play again: ")
   if play_again!="yes":
        print("Thanks for playing")
        break
        
        
    
