# numbers=[1,2,3,4]
# #0,1,2,3
# for num in numbers:
#         print(num)

# #break terminates
# #continue skips
# #pass tells the program to do nothing

# while i <= n:
#     #updating the value of sum
#     sum = sum + i
#     #updating the value of i
#     i = i+1    # update counter
# #1st iteration i=1, sum=0
# #2nd iteration i=2, sum=1
# #3rd iteration i=3, sum=3

num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)
#

# first = [2, 3, 4]
# second = [20, 30, 40]
# final = []
# for i in first:
#     for j in second:
#         final.append(i+j)
# print(final)
# # i=2, j=20,j=30,j=40
# # i=3, j=20, j=30, j=40
# # i=4, j=20, j=30, j=40

# rows=eval(input("How many rows?: "))
# # outer loop
# #step range(1,10)
# for i in range(1, rows + 1):
#     # inner loop
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print('')
# #i=1 end_outer=6 end_inner=2 j=1 
# #i=2 end_outer=6 end_inner=3 j=[1,2]
# #i=3 end_outer=6 end_inner=4 j=[1,2,3]
# #i=4 end_outer=6 end_inner=5 j=[1,2,3,4]
# #i=5 end_outer=6 end_inner=6 j=[1,2,3,4,5]

