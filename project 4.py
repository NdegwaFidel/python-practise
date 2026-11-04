students= [
    ["Fidel",[80,75,90]],
    ["James",[65,70,85]],
    ["Mary",[90,95,88]]
]

print("STUDENT MARK MANAGEMENT LIST")

averages=[]

for student in students:
    print("Student: ",student[0])
    print ("Marks: ",student[1])

    
    total=sum(student[1])
    count=len(student[1])
    average=total/count

   
    averages.append(average)

   
   

    print("Average ",f"{average:.2f}")
    print()



class_total=sum(averages)
class_count=len(averages)
class_average=class_total/class_count


print("Class Average: ",f"{class_average:.2f}")


highest=max(averages)
lowest=min(averages)
new_averages=sorted(averages,reverse=True)

formatted_avrg=[f"{average:.2f}" for average in averages]
formatted_sorted=[f"{average:.2f}"for average in new_averages]
passing_students=[new for new in formatted_sorted if float(new) >= 50]
failing_students=[new for new in formatted_sorted if float(new)< 50]



print("STUDENT AVERAGE; ",end="")
print(formatted_avrg)
print("STUDENT AVERAGE HIGHEST TO LOWEST:  ",end="")
print(formatted_sorted)
print("HIGHEST AVERAGE: ",f"{highest:.2f}")
print("LOWEST AVERAGE: ",f"{lowest:.2f}")
print(passing_students)
print(failing_students)









   
    
    

    


    
    
    
