Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# type 2 - string methods
# -----------------------

#string concatenation / string repetition

# string formatting (manual / automated / general)

# manual formatting
# -----------------

name='alvi'
gender='female'
age=6

print('my baby name is {0} aged {1} gender is {2}')
my baby name is {0} aged {1} gender is {2}

print('my baby name is {0} aged {1} gender is {2}'.format(name,age,gender))
my baby name is alvi aged 6 gender is female

print('my baby name is {2} aged {0} gender is {1}'.format(name,age,gender))
my baby name is female aged alvi gender is 6

print('my baby name is {2} aged {0} gender is {1}'.format(age,gender,name))
my baby name is alvi aged 6 gender is female

print('my baby name is {} aged {} gender is {}'.format(name,age,gender))
my baby name is alvi aged 6 gender is female


# () - parenthesis
# {} - braces
# [] - brackets

# [] - list data struture
# () - tuple
# {} - set / dick


# automated formatting
# ---------------------

print('my baby name is %s aged %d gender is %s' % (name,age,gender))
my baby name is alvi aged 6 gender is female

print('my baby name is %s aged %s gender is %s' % (name,age,gender))
my baby name is alvi aged 6 gender is female

print('my baby name is %s aged %s gender is %d' % (name,age,gender))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print('my baby name is %s aged %s gender is %d' % (name,age,gender))
TypeError: %d format: a real number is required, not str

print('my baby name is %s aged %s gender is %d' % (name,gender,age))
my baby name is alvi aged female gender is 6


# general formatting
# ------------------

print ('baby name is',name)
baby name is alvi

print ('baby name is',name,'gender is',gender)
baby name is alvi gender is female

print ('baby name is',name,'gender is',gender,'baby current age is',age)
baby name is alvi gender is female baby current age is 6


# self introdcution
# -----------------

print ('baby name is',name,'gender is',gender,'baby current age is',age)
baby name is alvi gender is female baby current age is 6

# name,age, city ,degree , interest , strength, tech course


===================== RESTART: C:/Python310/day8_python_string_handling_string methods_type_3.py ====================
self intro using manual formatting
----------------------------------
 Hi SIR
my name is kishore
my age is 21
im living at chennai
my interest is CIRCKET
my strength is TEAM WORK
my techcourse is python
thank you
>>> 
===================== RESTART: C:/Python310/day8_python_string_handling_string methods_type_3.py ====================
self intro using automated formatting
----------------------------------
 Hi SIR
my name is kishore
my age is 21
im living at chennai
my interest is CIRCKET
my strength is TEAM WORK
my techcourse is python
thank you
>>> 
===================== RESTART: C:/Python310/day8_python_string_handling_string methods_type_3.py ====================
self intro using general formatting
----------------------------------
 Hi SIR
my name is  kishore
my age is  21
im living at  chennai
my interest is  CIRCKET
my strength is  TEAM WORK
my techcourse is  python
thank you
