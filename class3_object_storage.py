# Variable assignment and object storage in python
variable1 = 50           #initialization
variable2 = 100
variable3 = 50
print("variable1",variable1,variable2,variable3,id(variable1),"-------")
print("-----------------")
print(variable1)
print(type(variable1))
print("type(variable1)")    
 #type() function is used to get the datatype of some object

memory = id(variable1)    
 #id() function is used to get the memory location that the variable is referring to.

print("Variable1 : ", memory)
print("variable2 : ", id(variable2))
print("variable3 : ", id(variable3))

variable1 = 300
print("Variable1 : ", id(variable1))
print(variable1)

# Mutable and Immutable datatypes :
'''
1. Mutable datatypes : The datatypes that can be modified/updated after initialization
are called as mutable datatypes.
e.g list, set, dictionary.

1. Immutable datatypes : The datatypes that cannot be modified/updated after initialization
are called as immmutable datatypes.
e.g int,float, complex, string, boolean, tuple.
'''
# immutable datatypes
number1 = 123.07
number1 = 323

# mutable datatypes
lst = ["blue","red","yellow","orange","green"]

lst[0] = 12
print(lst)

tuple = ("blue","red","yellow","orange","green")
print(tuple[0])

string1 = "We are learning mutable and immutable datatypes"
print(string1[10])

set = {1,2,3,4,5,6,7,8,9,10}
set.remove(2)
print(set)

dictionary = {
    "Batch" : "DS250723",
    "Course" : "Datascience",
    "Modules" : ["Python","DSA","ML"],
    "Duration" : "6 Months",
    "Course" : "Full stack developer"
}
# dictionary["Course"] = "Full stack developer"
# print(dictionary["Course"]

dictionary["Batch size"] = 60
print(dictionary)

