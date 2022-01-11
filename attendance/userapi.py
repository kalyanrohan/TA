from teacher import Teachers
from students import Student

data = open("data.txt", "r+", encoding="utf-8")
data_format = {}

class User(Teachers,Student):
    
    def __init__(self):
        self.username = ""
        self.password = ""
        self.occupation = ""
        self.name = ""
        self.age = 0
        self.sex = ""
        self.class_num = ""
    
    def __init__(self, username, password, occupation,name,age,sex,class_num):
        super().__init__(name,age,sex,occupation,class_num)
        self.username = username
        self.password = password
        if username not in data.read():
            if occupation.lower() == "teacher":
                data_format['username']=username
                data_format['password']=password
                data_format['occupation']=occupation
                data_format['name']=name
                data_format['age']=age
                data_format['sex']=sex
                data_format['class_num']=class_num
                for datas in data_format:
                    data.write(f'{datas}: {data_format[datas]}, ')
                data.write(f'\n')

            elif occupation.lower() == "student":
                data_format['username']=username
                data_format['password']=password
                data_format['occupation']=occupation
                data_format['name']=name
                data_format['age']=age
                data_format['sex']=sex
                data_format['class_num']=class_num
                data_format['attendance']=self.get_attendance()
                
                for datas in data_format:
                    data.write(f'{datas}: {data_format[datas]}, ')
                data.write(f'\n')
        else:
            print("Username already exists")
        data.seek(0)

    def login(self,username,password):
        data.seek(0)
        for line in data:
            line = line.strip().split(', ')
            if username in line[0] and password in line[1]:
                print("Login successful")
                return True
        print("Login failed")
        return False

    def update_attendance(self,attendance):
        self.attendance = attendance
        data_format['attendance']=attendance
        data.seek(0)
        for line in data:
            line = line.strip().split(', ')
            if self.username in line[0]:
                for datas in data_format:
                    data.write(f'{datas}: {data_format[datas]}, ')
                data.write(f'\n')
                break
        data.seek(0)
    

user1=User('starlord123','123','teacher','Tony Stark',35,'m','1')
user2=User('ironman','123','student','Jeff',15,'m','1')

user2.login('starlord123','123')





        


