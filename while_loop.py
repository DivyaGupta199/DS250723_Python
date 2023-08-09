# while loops : while loops are used to execute some block of code till a certain condition is getting satisfied.
'''
for variable_name in range():
    pass
for variable_name in iterable_obj:
    pass
while condition:
    pass
'''
'''
number = 5
i = 5
while i<=number:  
    print(i)
    i+=1
print("--------------finished---------------")
'''
# write a program to print all the multiples of 3 and 5 between 1 to 100.
number = 4
while number<=100:
    if number%3==0 and number%5==0:
        print(number, end = " , ")
    number+=1

while True:
    choice = int(input("Enter 1. To order some products\n Enter 2. To see the wishlist \n Enter 3. To exit this window"))
    if choice == 1:
        print("Order the products")
    if choice == 2:
        print("Show the wishlist")
    if choice == 3:
        break

print("-----------------")