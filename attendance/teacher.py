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
    

