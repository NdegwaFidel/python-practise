students={}

name=input('ENTER STUDENT NAME ')
reg_no=input('ENTER REGISTRATON NUMBER ').strip().upper()
marks=float(input('ENTER STUDENT MARKS '))
course=input('ENTER STUDENT COURSE ')


def add_student(reg_no,name,marks,course):
    if reg_no in students:
        print('STUDENT ALREADY EXISTS!')
    else:
        students[reg_no]={
        'name':name,
        'course':course,
        'marks':marks
    }
    print()
    print('NEW STUDENT ADDED SUCCESFULLY')
print()
add_student(reg_no,name,marks,course)
print(students)


def display_students():
    if students=={}:
        print('NO STUDENT RECORDS FOUND ')
    else:
        for student,details in students.items():
            print('REG NO: ',student)
            print('NAME; ',details['name'])
            print('COURSE: ',details['course'])
            print('MARKS: 'details['marks'])


display_students()


def search_student(reg_no):
    registration_no=input('ENTER REGISTRATION NUMBER TO ACCESS STUDENT DETAILS: ')

    if registration_no in students:
        print('STUDENT FOUND')
        print(student,details in students.items())
    else:
        print('STUDENT NOT FOUND!')
