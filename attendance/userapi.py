from teacher import Teachers
from students import Student

data = open("data.txt", "a", encoding="utf-8")
data_format = {}
class User(Teachers,Student):
    def __init__(self, username, password, occupation,name,age,sex,class_num):
        if occupation.lower() == "teacher":
            Teachers(name,age,sex,occupation,class_num)
        elif occupation.lower() == "student":
            Student(name,age,sex,occupation,class_num)
        
        self.username = username
        self.password = password


        


