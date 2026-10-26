#dice rolling game
import random
#loop

while True:
    choice=input("Roll the dice? y/n: ").lower() #ask for input
    die_1= random.randint(1,6)  #generate 2 random numbers
    die_2= random.randint(1,6)
#displaying the numbers
    if choice=="y":
        print("You rolled "+str(die_1) + " and " +str(die_2))
    elif choice=="n":
        print("Thanks for playing!")
    else:
        print("Invalid choice..try again")

