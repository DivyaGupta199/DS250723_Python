# conditional statements are the statements used for giving certain conditions  in our program.
# if statement 
# else statement
# elif  --- else if


# example of if else condition : - 
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a < b :
  print("a is smaller than b")
  print("-------------------------")

else :
  if b < a:
      print("b is smaller than a")
      print("-------------------------")

  else :
      print("a and b are equal")
  

print("------------Program is finished--------------------")
'''

# example of elif : 
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a > b:
    print("a is greater than b")

elif b > a :
    print("b is greater than a")

else :
    print("Both the numbers are equal")
'''

# Write a program to check whether a number is even or odd.

# 0,2,4,6,8,10..............
# 1,3,5,7,9,11,13...............

# number = int(input("Enter any number"))
# if number % 2 == 0:
#     print(number,"is an even number")

# else:
#     print(number,"is an odd number")



a = int(input("enter a number:"))
if a%2==0:
    print(a,"number is even")
else:
   print(a," is odd")

# Nested if condition :

first_num = int(input("Enter the first number"))
second_num = int(input("Enter the second number"))
third_num = int(input("Enter the Third number"))

if first_num > second_num :
    if first_num > third_num:
        print("First number is greatest")
    elif first_num < third_num:
        print("Third number is greatest")
    else:
        print("First and third number are greater than second")

else:
    if second_num > third_num :
        print("Second number is the greatest")
    elif second_num < third_num:
        print("Third number is greatest")
    else:
        print("second and third number are greater than first")

# You have to take input of marks from the user and on the basis of marks you have to assign grades :
'''
--> Marks will be between 0 to 100
--> if the marks are greater than 90, then assign A+ grade.
--> if the marks are greater than 80, then assign A grade.
--> if the marks are greater than 70, then assign B+ grade.
--> if the marks are greater than 60, then assign B grade.
--> if the marks are greater than 50, then assign C+ grade.
--> if the marks are less than 50, then assign C grade.
'''



