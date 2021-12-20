class Person:

    def __init__(self,name,address):
        self.name=name
        self.address=address
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def set_name(self,name):
        self.name=name
    
    def set_address(self,address):
        self.address=address
    
    def toString(self):
        return f"Name: {self.name}\nAddress: {self.address}"

class Student(Person):
    
    def __init__(self,name,address):
        super().__init__(name,address)
        self.numCourses=0
        self.courses=[]
        self.grades=[]
    
    def toString(self):
        return f"Name: {self.name}\nAddress: {self.address}\nNumber of courses: {self.numCourses}\nCourses: {self.courses}\nGrades: {self.grades}"
    
    def addCoursesGrade(self,course,grade):
        self.courses.append(course)
        self.grades.append(grade)
        self.numCourses+=1
    
    def printGrades(self):
        print(f'\nHere are the grades of {self.name}: ')
        for i in range(self.numCourses):
            print(f"{self.courses[i]}: {self.grades[i]}")
    
    def getAverageGrades(self):
        total=0
        for grade in self.grades:
            total+=grade
        return total/self.numCourses

class Teachers(Person):

    def __init__(self,name,address):
        super().__init__(name,address)
        self.numCourses = 0
        self.courses = []
    
    def addCourse(self,course):
        if course in self.courses:
            print("Course already exists")
            return False
        else:
            self.courses.append(course)
            self.numCourses+=1
            return True
    
    def removeCourse(self,course):
        if course not in self.courses:
            print("Course doesn't exist")
            return False
        else:
            self.courses.remove(course)
            self.numCourses-=1
            return True
    
    def toString(self):
        return f"Name: {self.name}\nAddress: {self.address}\nNumber of courses: {self.numCourses}\nCourses: {self.courses}"
            
    

    student1=Student("John","123 Main St.")
    student1.addCoursesGrade("Math",90)
    student1.addCoursesGrade("English",80)
    student1.addCoursesGrade("Science",70)
    print(student1.toString())
    student1.printGrades()
    print(f'Average grade: {student1.getAverageGrades()}')

    teacher1= Teachers("Jane","456 Main St.")


{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    