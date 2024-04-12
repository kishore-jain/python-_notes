Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# variable length arguments (arbitrary arguments)
# -----------------------------------------------

# broadcast massages / services

def greet(*students):
    for i in students:
        print('happt diwali',i)

        
greet('elango','kishore','jain','hari','hemanth','ashwanth','aachith')
happt diwali elango
happt diwali kishore
happt diwali jain
happt diwali hari
happt diwali hemanth
happt diwali ashwanth
happt diwali aachith

greet('jain')
happt diwali jain

============================ RESTART: C:/Python310/variable-function.py ===========================
Traceback (most recent call last):
  File "C:/Python310/variable-function.py", line 4, in <module>
    profile('kishore',23,'mahagliga nager','male','B.E')
  File "C:/Python310/variable-function.py", line 2, in profile
    return name,age,city,gender,degree
NameError: name 'name' is not defined. Did you mean: 'namre'?

============================ RESTART: C:/Python310/variable-function.py ===========================
Traceback (most recent call last):
  File "C:/Python310/variable-function.py", line 4, in <module>
    print(profile('kishore',23,'mahagliga nager','male','B.E'))
  File "C:/Python310/variable-function.py", line 2, in profile
    return name,age,city,gender,degree
NameError: name 'name' is not defined. Did you mean: 'namre'?

============================ RESTART: C:/Python310/variable-function.py ===========================
('kishore', 23, 'mahagliga nager', 'male', 'B.E')
# function call as return mainly use print
# only once the return keyword must be used in one function
# reture must always used to get output by given PRINT before  calling the function




# recursive function [if a function calls itself repeatedly]

def fact(n):
    if n==0:
            return 1
    else:
        return n*fact(n-1)

    
fact(5)
120

# fact(5) = 5 * 4 * 3 * 2 * 1 * 1

>>> # ______-------------------------------
>>> 
>>> # lambda function
>>> # ---------------
>>> 
>>> # one time function
>>> # nameless function
>>> 
>>> # rules
>>> # -----
>>> 
>>> # cannot use def keyword,instead use lambda keyword
>>> # cannot use print function inside lambda
>>> # cannot use elif keyword
>>> 
>>> # this is called in-line function
>>> 
>>> def add (a,b):
...     return a+b
... 
>>> ad = lambda a,b:a+b
>>> add(30,40)
70
>>> ad(30,40)
70
>>> 
>>> # NOTE :lambda function is  only written only in one line
>>> 
