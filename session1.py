# x = 5; y = 10
# #format output
# print('The value of x is {} and y is {}'.format(x,y))

# print(f'The value of x is {x} and y is {y}')

# number=input("Enter a number: ")
# #type function returns the data type
# print(type(number))
# #casting
# print(int(number))
# print(float(number))

#eval function to evaluate input type
number_2=eval(input("Enter a number: "))
print(number_2)
print(type(number_2))

if number_2>10:
    print('VERY GOOD')
    if(number_2%2==0):
        print(f'{number_2} is an even number')
    elif(number_2%2!=0):
        print(f'{number_2} is an odd number')
elif 3>number_2>7:
    print('GOOD')
else:
    print('nice try')
#list and array
list1=[1,'string',True]
#dictionary
student1={'name':'Jeff','age':120,'is_vaccinated':True}