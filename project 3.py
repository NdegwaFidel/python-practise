#simple calculator 
while True:
    try:

        num_1=float(input("first number "))
        num_2=float(input("second number "))

        choices =["add","subtract","multiply","divide"]

        for index, choice in enumerate(choices,start=1):
            print(index,choice)


 

        

        operation=int(input("choose operation to use by selecting the number "))
    except ValueError:
        print("please enter a viable number and correct operation")
        continue
    

    if operation == 1:
        print(num_1 + num_2)
    elif operation == 2:
        print(num_1 - num_2)
    elif operation == 3:
        print(num_1 * num_2)  
    elif operation == 4:
        if  num_2 == 0:
            print("cannot divide by zero")
        else:
            print(num_1 / num_2)
    else:
        print("invalid operation ! try again")
    
    while True:

        leave=input("continue or exit? y/n ").lower()
        if leave == "y":
           break
        elif leave =="n":
           print("starting a new round...")
           break
        else:
           print("invalid choice...")
    if leave == "y":
        break
    
