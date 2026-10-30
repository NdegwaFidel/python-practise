#dice rolling game
import random
#loop
             
while True:
    choice=input("Roll the dice ? y/n ").lower()
       
#displaying the numbers
    if choice=="y":
       
    
        while True:
            try:
                 rolls=int(input("How many times do you want to roll? "))

                 if 1 <= rolls <= 10:
                    break
                 else:
                    print("ENTER A NUMBER BETWEEN 1 AND 10")
            except ValueError:
                print("Invalid input,enter a whole number")


        counter=0
        total_score=0

        while counter < rolls:

            die_1=random.randint(1,6)
            die_2=random.randint(1,6)

            print("You rolled ",die_1 , " and ",die_2 )

            total_score = total_score + die_1 + die_2
            counter=counter+1
        
        print("GAME OVER! YOU COMPLETED ",counter,"ROLLS")
        print("YOUR TOTAL SCORE IS ",total_score)


    elif choice=="n":
        print("Thanks for playing!")
        break
    else:
         print("Invalid choice..try again")
    

    


     
   