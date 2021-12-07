class Person:

    #self refers to the object itself
    def __init__(self, name, age, sex, occupation):
        #attributes
        self.name = name
        self.age = age
        self.sex = sex
        self.occupation = occupation
    #getters to get the attributes
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_occupation(self):
        return self.occupation

    #setters to set or change the attributes
    def set_name(self, name):
        self.name=name  
    
    def set_age(self, age):
        self.age = age
    
    def set_sex(self, sex):
        self.sex=sex
    
    def set_occupation(self,Occupation):
        self.occupation=Occupation
    
    def __str__(self):
        return f"{self.name} is {self.age} years old. {self.name} is a {self.sex} that is currently working as {self.occupation}"

#instatiate the class//creating the object
student1=Person("Bernard",19,'male','student') #calls the init function
student2=Person(None,None,None,None)

# name=input("What is your name?")
# student2.set_name(name)
# age=eval(input("What is your age? "))
# student2.set_age(age)
# sex=input("What is your sex? ")
# student2.set_sex(sex)
# occupation=input("What is your occupation? ")
# student2.set_occupation(occupation)
# student3=Person(name,age,sex,occupation)


student1.set_age(20)
print(student1.get_age())
print(student1.__str__())
student1.get_name()
student1.get_name('candace')

#POLYMORPHISM
# different classes with the same function name
#parent class
class Animal:
    def __init__(self, name,population):
        self.name = name
        self.population = population
    
    def get_name(self):
        return self.name
    
    def get_population(self):
        return self.population
    
#child class
class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
cat1.get_population()
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()