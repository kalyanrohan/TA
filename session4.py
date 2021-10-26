global scope
print('hello')
age=21
def return_double_age():
    #local scope
    name='jeff'
    global age
    age=34
    print(age,name)
print(age)
return_double_age()
print(age)

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
print('before '+x)
foo()
print('after '+x)  

def mean(array):
    result=0
    for num in array:
        result+=num
    return result/len(array)

numbers=[1,2,3,4,5]

def crazy_formula(array,special_number):
    #mean+min^2+max^2//len(array)
    return mean(array)+min(numbers)**2+max(numbers)**2//special_number

print(crazy_formula(numbers,7))
first_name=''
def first_name_input():
    global first_name
    first_name=input('What is your first name?: ')
    print(first_name)

def greet():
    first_name_input()
    print('hello '+first_name)

greet()


