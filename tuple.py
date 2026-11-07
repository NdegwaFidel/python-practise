students=(
    ("fidel",22,"apcs"),
    ("john",23,"engineering"),
    ("mary",21,"physics")
)
print(students[1])
print(students[2][2])

age=0

for student in students:
    age+=student[1]

print(age)

for name,age,course in students:
    print(name)                   



