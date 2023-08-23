'''
Modules : 
--> Modules refer to a file which contains python statements and definitions. for e.g
datatype.py , marks.py
--> we use modules to break down large programs into small manageable and organized files.
--> Modules also provide reusability of code.
--> we can define our most used functions in a module and import it, instead of copying 
their definitions into different programs.
'''
# How do we import modules ?
'''
we use import keyword for importing a module in our current program, if it is in
python library and not present in our system so firstly we need to install it.
by the command pip install module_name.
'''

import math

sqrt = math.sqrt(100)
print(sqrt)

