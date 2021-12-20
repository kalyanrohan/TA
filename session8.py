# try, except, finally, else, raise, assert

numbers=[1,2,3,4]
try:
    input1=eval(input("Enter the position of the number that you want to select: "))
    input2=eval(input("Enter a number: "))
    if input2<0:
        #prints out the string in the bracket if value error is catched
        raise ValueError("Number has to be more than 0")
    elif input2==0:
        raise ZeroDivisionError("You can't divide by zero")
    print(numbers[input1]/input2)
except IndexError:
    print("Index out of range")
else:
    print("No error")
finally:
    print("This will run no matter what")

def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))

age = input("Enter your age: ")

while type(age) is not int:    
    try:
        age = int(age)
    except ValueError:
        age = input("This was not a valid input please try again: ")


print ("your age: ", age)
