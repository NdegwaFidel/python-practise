#dice rolling game
import random
#loop
             
while True:
    choice=input("Roll the dice ? y/n ")
       
#displaying the numbers
    if choice=="y":
        rolls=int(input("How many times do you want to roll? "))
        
        while rolls <= 0:
            print("please enter a positive number")
            rolls=int(input("How many times do you want to roll? "))
            

        counter=0

        while counter < rolls:

            die_1=random.randint(1,6)
            die_2=random.randint(1,6)

            print("You rolled ",die_1 , " and ",die_2 )

            counter=counter+1
        
        print("GAME OVER! YOU COMPLETED ",counter,"ROLLS")

    elif choice=="n":
        print("Thanks for playing!")
        break
    else:
         print("Invalid choice..try again")
    

    


     
   