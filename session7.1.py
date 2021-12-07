#Overriding
class A:
    def show(self):
        print("In A")
class B(A):
    def show(self):
        print("In B")
class C(B):
    def show(self):
        print("In C")

A().show()
B().show()
C().show()

class Person:
    def __init__(self,first_name,last_name,age,sex,birth):
        self.first_name = first_name
        self.last_name =last_name
        self.age = age
        self.sex = sex
        self.birth = birth
    def __str__(self):
        return "Name: " + self.first_name +" "+ self.last_name +" \nAge: " + str(self.age)+" \nSex: " + str(self.sex)+"\nBirth: " + str(self.birth)+""

class Employee(Person):
    
    def __init__(self,first_name,last_name,age,sex,birth,salary,department,position):
        #super is a function that refers to the parent class
        super().__init__(first_name,last_name,age,sex,birth)
        self.salary = salary
        self.department = department
        self.position = position
    
    def __str__(self):
        return super().__str__() + "\nSalary: " + str(self.salary)+"\nDepartment: " + str(self.department)+"\nPosition: " + str(self.position)+"\n"

employee1 = Employee("John","Cena",45,"m",1969,500,"Sports","Coach")
employee2 = Employee("Candace","Nuts",369,"f",1980,420,"Management","Chad")
person1=Person("Kenya","Cox",35,"m",1998)
print(employee1.__str__())
print(employee2.__str__())
print(person1.__str__())


#Overloading
#*args allows you to pass multiple positional arguments to a function
def add(*args):
    print(type(args))
    print(args)
    sum = 0
    for i in args:
        sum += i
    return sum

def mean(*args):
    sum = 0
    inputs=list(args)
    for i in inputs:
        sum += i
    return "mean: "+str(sum/len(args))
#kwargs are used to pass multiple keyword arguments to a function
def person(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)

def sort(**kwargs):
    teens=[]
    mid=[]
    old=[]
    for key,value in kwargs.items():
        if value < 20:
            teens.append(key)
        elif value >= 20 and value < 40:
            mid.append(key)
        else:
            old.append(key)
    return "Teens: "+str(teens)+"\nMid: "+str(mid)+"\nOld: "+str(old)

print(add(1,2,3,4,5,6,7,8,9,10))
print(mean(1,2,3,4,5,6,7,8,9,10))
person(name="John",age=45,occupation="Actor",salary=500)
print(sort(John=45,Candace=369,Kenya=35,Ken=17,Cena=45,Cox=20))
    
def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Cannot divide by zero"
#positional arguments
print(divide(6,3))
#keyword arguments
print(divide(num2=6,num1=3))

def func(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)