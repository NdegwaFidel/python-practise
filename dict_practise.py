student={
    "name":"fidel",
    "age":21,
    "course":"applied physics",
    "marks":75
}

student["admission no"]="SCT 253"
student["age"]=22
student["marks"]=90
student.update(year=3,course="applied physics and computer science")
removed_marks=student.pop("marks")

print(removed_marks)

del student["admission no"]

print(student)

for key,value in student.items():
    if type(value)==int:
        print(key)
