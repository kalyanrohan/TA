operator=eval(input("Select a number to choose an operator (1.Addition 2.Subtraction 3.Multiplication 4.Division): "))
num_1=eval(input("enter a number: "))
num_2=eval(input("enter another number: "))
result=0
if(operator==1):
    result=num_1+num_2
    print(f'The result is: {result}')
elif(operator==2):
    result=num_1-num_2
    print(f'The result is: {result}')
elif(operator==3):
    result=num_1*num_2
    print(f'The result is: {result}')
else:
    result=num_1/num_2
    print(f'The result is: {result}')
