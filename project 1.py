name=input("ENTER YOUR FULL NAME; ")
admn_no=input("ENTER ADMISSION NUMBER; ")
eng_marks=int(input("ENGLISH SCORE; "))
sci_marks=int(input("SCIENCE SCORE; "))
bio_marks=int(input("BIOLOGY SCORE; "))
total_marks=eng_marks+sci_marks+bio_marks
avg_marks=total_marks/3
print("LOADING INFO",end="...")
print()
print()

print("...STUDENT REPORT CARD...")
print("STUDENT NAME: ",name)
print("ADMISSION NUMBER: ",admn_no)
print("TOTAL MARKS: ",total_marks)
print("AVERAGE MARKS: ",round(avg_marks,2))