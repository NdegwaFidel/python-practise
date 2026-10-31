import random



def roll_dice():

    return random.randint(1,6)


def get_rolls():
    while True:
         try :
    
            rolls=int(input("How many times do you want to roll"))

            if 1 <= rolls <= 100:
                return rolls 
            else:
                print("ENTER A NUMBER BETWEEN 1 AND 100")
         except ValueError:
            print("ENTER A WHOLE NUMBER")
            

def calculate_score(*numbers):
    total=0

    for n in numbers :
        total+=n
    
    return total


def play_game(rolls):
    counter=0
    total_score=0

    while counter < rolls:
        die_1= roll_dice()
        die_2= roll_dice()
        round_score=calculate_score(die_1,die_2)
        total_score+=calculate_score(die_1,die_2)
        counter += 1
        print("you rolled ",die_1," and ",die_2)
        print("round_score is ",round_score)

    print("your final score is ",total_score)

     

def main():

     rolls=get_rolls()
     play_game(rolls)


main()


    
