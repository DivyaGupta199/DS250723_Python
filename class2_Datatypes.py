# Datatypes : The type of data we are storing in the variables is refered as datatype.
# Classification of Datatypes
'''
1. Numerical : 
    1. int - it is referred for integer values.
    2. float - it is referred for decimal values.
    3. complex - it is referred for imaginary numbers. 0 + j

2. Squence :
   1. string - it is used for storing letters, words, and even numerical values can be stored as string.
                it is stored using "", '' , '''''' , """ """
   2. list - It is used for storing the collection of elements, It is a heterogeneous collection of elements. data. It can be modified later
   3. tuple - It is used for storing the collection of elements,It is a heterogeneous collection of elements. data. It cannot be modified later

3. Boolean : It is used for storing true/false values.

4. mapping :
    1. Dictionary - we store data in key value pairs. e.g {1 : "One", 
    "two" : 2},  {"name":"John","age":36}

5. set : It is used to store unique collection of data, It do not allow duplicates. e.g {1,2,3,4,5,6,7}

'''


"string Datatype"
string1 = "a"
string2 = "apple"
string3 = 'python is a programming language'
string4 = "1"
string5 = "0.50"
string6 = '30'
string7 = '''
            Python is a multipurpose programming language.
            It was developed by Guido van rossam.
            It is an Interpreted, object oriented programming language.
'''
string7 = """
            Python is a multipurpose programming language.
            It was developed by Guido van rossam.
            It is an Interpreted, object oriented programming language.
"""

num1 = "100"
num2 = "200"
print(num1+num2)


# List and tuple Datatype
lst1 = ["apple", "banana", "cherry", "mango"]
lst2 = ("apple", "banana", "cherry", "mango")
lst3 = [10,10.20,"apple",[1,2,3,4],(5,6,7,8),4+8j]
lst3 = (10,10.20,"apple",[1,2,3,4],(5,6,7,8),4+8j)
print("type of lst1",type(lst1))
print("type of lst2",type(lst2))
print("type of lst3",type(lst3))

# Boolean Datatype
status1 = True
status2 = False

status3 = bool("")
status4 = bool("1")

print("Status1",type(status1))
print("Status2",type(status2))
print("Status3",status3)
print("Status4",status4)

# Dictionary Datatype :
dict1 = {"Student_Name" : "Ram", "Batch" : "DS121223", "marks" : (10,20,30,40,50)}
print(type(dict1))

# Set Datatype : 
set1 = {1,2,3,4,5,6,6,6,6,7,8,8,9,10}
set2 = {11,12,13,14,15,16}
print(set1.union(set2))
set1.add(15)
print(set1)
print(type(set1))
