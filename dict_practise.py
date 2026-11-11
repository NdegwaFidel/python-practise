students={
    "SCT001":{
        "name":"Fidel",
        "age":22,
        "course":"applied physics and computer science",
        "marks":85
    },
    "SCT002":{
        "name":"James",
        "age":21,
        "course":"computer science",
        "marks":78
    },
    "SCT003":{
        "name":"Mary",
        "age":23,
        "course":"applied physics",
        "marks":92
    }
}

students["SCT004"]={
    "name":"peter",
    "age":24,
    "course":"computer science",
    "marks":88}
    


students["SCT001"]["marks"]=95
students["SCT002"].update({"email address":"james45@gmail.com"})
students["SCT003"].update(age=24,marks=96)

no_of_students=len(students)

print(no_of_students)
print(students["SCT001"]["marks"])
print(students["SCT002"]["email address"])
print(students["SCT003"]["age"])
print(students["SCT003"]["marks"])