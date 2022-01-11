import teacher
import students
import userapi

choice=0
choice2=0
name=''
age=''
sex=''
occupation=''
class_num=''

name=input('Please enter your name: ')
age=input('Please enter your age: ')
while type(age) is not int:    
    try:
        age = int(age)
    except ValueError:
        age = input("Please enter a number: ")

sex=input('Please enter your gender: ')
occupation=input('Please enter your occupation: ')
class_num=input('Please enter your class number: ')

user=teacher.Teachers(name,age,sex,occupation,class_num)
while choice!=5:
        print('Please choose your action: ')
        print('1. Check Students')
        print('2. Add Student')
        print('3. Remove Student')
        print('4. Set Students Attendance')
        print('5. Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            user.get_students_info()

        elif choice==2:
            name=input('Please enter the name of the student: ')
            age=int(input('Please enter the age of the student: '))
            sex=input('Please enter the sex of the student: ')
            user.add_student(students.Student(name,age,sex,'student',user.get_class_num()))
            
        elif choice==3:
            name=input('Please enter the name of the student that you want to remove: ')
            for student in user.get_students():
                if student.get_name()==name:
                    user.remove_student(student)
                    print('Student removed')
                    break
        
        elif choice==4:
            name=input('Please enter the name of the student: ')
            for student in user.get_students():
                if student.get_name()==name:
                    attendance=input('Enter "P" if student is present/Enter "A" if student is absent: ')
                    if attendance.upper()=='P':
                        user.set_students_attendance(student,True)
                    elif attendance.upper()=='A':
                        user.set_students_attendance(student,False)
                    else:
                        print('Invalid input')
                    break

            




