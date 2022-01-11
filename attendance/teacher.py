from person import Person

class Teachers(Person):
    
    def __init__(self, name, age,sex,occupation,class_num):
        super().__init__(name, age,sex,occupation,class_num)
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)
    
    def remove_student(self,student):
        self.students.remove(student)
    
    def get_students(self):
        return self.students
    
    def get_students_info(self):
        for student in self.students:
            print(f'name: {student.get_name()}, age: {student.get_age()}, sex: {student.get_sex()}, class:{student.get_class_num()}, attendance: {student.get_attendance()} \n')
    
    def set_students_attendance(self,student,attendance):
        student.set_attendance(attendance)
    

