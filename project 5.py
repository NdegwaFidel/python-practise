physics ={"Fidel","John","Mary"}
computer_science={"Fidel","James","Peter"}

physics.add("David")
computer_science.add("Mary")

print("ALL REGISTERED STUDENTS: ",physics | computer_science)
print("STUDENTS TASKING BOTH COURSES: ",physics & computer_science)
print("STUDENTS TAKING PHYSICS ONLY: ",physics-computer_science)
print("STUDENTS TAKING COMP SCIENCE ONLY: ",computer_science-physics)
print("exclusive students: ",physics^computer_science)