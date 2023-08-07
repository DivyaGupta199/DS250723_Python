# Python operators 
'''
Operators are used to perform operation on data/variables/values.

Types of operators :
1. Arithmetic operators : Arithmetic operators are used to perform mathematical operations like addition,
substraction, multiplication etc.
    1. Addition (+)
    2. Substraction (-)
    3. multiplication (*)
    4. Division (/)
    5. Floor Division (//)
    6. Modulus (%)
    7. exponent ( ** )

2. Assignment operator ( = ) Assignment operators are used to assign values to variables.
    =, +=, -=, *=, /= ,//= ,%= , **=

3. Comparision operators : These are used for comparison of two data/variables.
    1. ==
    2. !=
    3. >
    4. <
    5. >=
    6. <=

4. Logical operators :
    1. AND
    2. OR
    3. NOT

5. Identity operators :
    1. is 
    2. is not

6. Membership operators : 
    1. in 
    2. not in 

7. Bitwise operators :
    
'''
# Addition operator (+) :
variable1 = 50
variable2 = 30
sum = variable1 + variable2
print("----------------------------")
print("Addition",sum)
print("-------------------------------")

# Substraction (-) :
variable1 = 100
variable2 = 30
difference = variable1 - variable2
print("Substraction : ",difference)
print("----------------------------------")

# multiplication (*) :
variable1 = 100
variable2 = 30
product = variable1 * variable2
print("product : ",product)
print("----------------------------------------")

# Division (/) :
variable1 = 100
variable2 = 30
Division = variable1 / variable2
print("Division : ",Division)
print("----------------------------------------")

# Floor Division (//) :
variable1 = 100
variable2 = 30
Floor_Division = variable1 // variable2
print("Floor Division : ",Floor_Division)
print("----------------------------------------")

# Modulus (%) :
variable1 = 100
variable2 = 30
modulus = variable1 % variable2
print("Reminder : ",modulus)

# Exponential (**) :
base = 3
exponent = 2
result = base ** exponent
print("--------------------------------------------")
print("Exponent : ",result)

# Assignment operator ( = ) :
variable = "Assignment operator"
print("--------------------------------------------")
print(variable)

number = 10
number += 5
print("--------------------------------------------")
print("Assigning new value by adding a number using assignment operator : ", number)

number = 10
number -= 3
print("--------------------------------------------")
print("Assigning new value  by substracting a number using assignment operator : ", number)

number = 10
number *= 3
print("--------------------------------------------")
print("Assigning new value  by multiplying a number using assignment operator : ", number)

number = 10
number /= 2
print("--------------------------------------------")
print("Assigning new value  by dividing a number using assignment operator : ", number)

number = 10
number //= 3
print("--------------------------------------------")
print("Assigning new value  by floor division using assignment operator : ", number)

# Comparison operators
#  1. == (equals to)
number1 = 10
number2 = 10
print("-----------------Comparison operators---------------------")
print("------------------ == -----------------------")
print(number1," == ",number2)
print(number1 == number2)

#  != (Not equals to)
number1 = 10
number2 = 10
print()
print("------------------ != -----------------------")
print(number1," != ",number2)
print(number1 != number2)

#  > (greater than)
number1 = 100
number2 = 10
print()
print("------------------ > -----------------------")
print(number1," > ",number2)
print(number1 > number2)

#  < (less than)
number1 = 100
number2 = 10
print("--------------------------------------------")
print(number1," < ",number2)
print(number1 < number2)

#  >= (greater than or equals to )
number1 = 100
number2 = 10
print("---------------------------------------")
print(number1," >= ",number2)
print(number1 >= number2)

#  <= (less than or equals to )
number1 = 100
number2 = 10
print("----------------------------------------")
print(number1," <= ",number2)
print(number1 <= number2)

# Logical operators
# 1. "AND" It checks for two conditions and if both the conditions are true then it returns true otherwise
# it will return False
print()
print("-----------------------------------------")
print("-------------Logical and operator-----------------")
print(20 == 100/2 and 10 == 30/3)

# 2. "OR" It checks for two conditions and if any one of the conditions are true or both the conditions are true 
# then it returns true otherwise it will return False
print("-----------------------------------------")
print("-------------Logical or operator-----------------")
print(20 == 100/2 or 10 == 30/2 or 100 == 1000/10)

# 2. "NOT" It checks for the condition and then reverse the output and then give us the final result.
# It is used to reverse the results.

print("-----------------------------------------")
print("-------------Logical not operator-----------------")
print(not(20 == 100/2 and 10 == 30/3))


# Identity operators :
# is 
x = 20
y = 30
print("------------------------------ Identity operator (is)---------------------")
print(x is 20)

# is not
x = 20
y = 30
print("------------------------------ Identity operator (is not)---------------------")
print(x is not 20)

# Membeship operators
# in
x = 10
print("------------------------------ Membership operator (in)---------------------")
print(x in [10,20,30,40,50])

# in
x = 8
lst = [10,20,30,40,50]
print("------------------------------ Membership operator (not in)---------------------")
print(x not in lst )

print("----------\\n---------")