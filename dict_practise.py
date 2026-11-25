students={}


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


def display_students():
    if students=={}:
        print('NO STUDENT RECORDS FOUND ')
    else:
        for student,details in students.items():
            print('REG NO: ',student)
            print('NAME; ',details['name'])
            print('COURSE: ',details['course'])
            print('MARKS: ',details['marks'])


def search_student(reg_no):
    

    if reg_no in students:
        details=students[reg_no]
        print('STUDENT FOUND')
        print('REG NO: ',reg_no)
        print('NAME; ',details['name'])
        print('COURSE: ',details['course'])
        print('MARKS: ',details['marks'])
    else:
        print('STUDENT NOT FOUND!')


def update_marks(reg_no):
    if reg_no in students:
        details =students[reg_no]
        try:

           new_marks=float(input('ENTER NEW MARKS: '))
           if new_marks<0 or new_marks>100:
               print('INVALID MARKS !')
               return
               details['marks']=new_marks
               print('MARKS UPDATED SUCCESFULLY')
        except ValueError:
            print('ENTER VALID MARKS!!')
    else:
        print('STUDENT NOT FOUND')


while True:
    print('....STUDENT MANAGEMENT SYSTEM....')
    print('1. ADD STUDENT')
    print('2. DISPLAY ALL STUDENTS')
    print('3. SEARCH FOR STUDENTS')
    print('4. UPDATE STUDENT MARKS')
    print('5. EXIT SYSTEM')

    choice=input('SELECT A CHOICE 1-5: ')

    if choice=='1':
        name=input('ENTER STUDENT NAME: ')
        reg_no=input('ENTER REGISTRATION NUMBER: ').strip().upper()
        marks=float(input('ENTER STUDENT MARKS: '))
        course=input('ENTER STUDENT COURSE: ')
        add_student(reg_no,name,marks,course)

    elif choice=='2':
        display_students()

    elif choice=='3':
        reg_no=input('ENTER REG NO TO SEARCH: ')
        search_student(reg_no)

    elif choice=='4':
        update_marks(reg_no)

    elif choice=='5':
        print('EXITING PROGRAMME...')
        break

    else:
        print('INVALID CHOICE!TRY AGAIN')