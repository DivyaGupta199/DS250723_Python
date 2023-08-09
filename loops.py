# what is loop ? 
# DRY -- Donot repeat yourself.
'''
1. For loop : when we know the number of iterations, we use for loops.

2. While loop : when we want to execute some block of code till a particular condition is getting satisfied, 
we use while loops.

'''
# using for loop for printing numbers between certain range
# start = int(input("Give the start range : "))
# end = int(input("Enter the end range : "))
# for i in range(start,end,2):
#     print(i)

# numbers = [23,45,32,55,37,21,17,19,67]
# for element in lst:
#     print(element)

# string = "python programming"
# for s in string:
#     if s == 'o':
#         print("match found")

# dictionary1 = {1 : "one", 2:"two", 3 : "three"}
# for k in dictionary1:
#     print(k,end = " ")

# Write a program to find the sum of first n natural numbers using for loop. take the value of n from the user.
'''
n = 10
sum = 1+2+3+4+5+6+7+8+9+10
'''

n = int(input("Enter the value of n : "))
sum = 0
for i in range(1,n+1):
    # sum = sum + i
    sum += i
    print("i" , i)
    print("sum",sum)

print(f"""The sum of {n} natural numbers is""",sum)
