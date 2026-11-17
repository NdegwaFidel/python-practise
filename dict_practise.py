students = {
    "SCT001": {
        "name": "Fidel",
        "maprks": 76,
        "course": "Computer Science"
    },

    "SCT002": {
        "name": "Mary",
        "marks": 89,
        "course": "Applied Physics"
    }
}
students["SCT001"]["marks"]=90
students["SCT003"]={
    'name':'James',
    'marks':68,
    'course':'computer science'

}
for student,details in students.items():
    print(student)
    
    print(student)
    print('NAME; ',details['name'])
    print('SCORE; ',details['marks'])
    if details['marks']>=50:
        print('PASS')
    else:
        print('FAIL')

    print('SCORE; ',details['marks'])
    if details['marks']>=50:
        print('PASS')
    else:
        print('FAIL')


def search_student(reg_no):
   
    if reg_no in students:
        details=students[reg_no]

        print('NAME; ',details['name'])
        print('SCORE; ',details['marks'])
        print('COURSE; ',details['course'])
    else:
        print('ADMISSION NUMBER NOT FOUND')

search=input("ENTER STUDENT REGISTRATION NUMBER: ")

search_student(search)

