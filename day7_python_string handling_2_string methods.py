Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# string handling - category2
#-----------------------------

# string methods
#----------------

# type1 = string concatenation
# type2 = string repetition
# type3 = string formatting(manual/automated/general)


# string concatenation
#---------------------

20+20
40
'20'+'20'
'2020'
'20'+20
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    '20'+20
TypeError: can only concatenate str (not "int") to str
name
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name
NameError: name 'name' is not defined
name='alvina'
age=6
gender='female'

print('my baby name is '+name)

my baby name isalvina
print('my baby gender is'+name)
my baby gender isalvina
print('my baby gender is'+ gender)
my baby gender isfemale
print('my baby age is'+age)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print('my baby age is'+age)
TypeError: can only concatenate str (not "int") to str
print('my baby age is'+str(age))
my baby age is6
>>> age
6
>>> type(age)
<class 'int'>
>>> print('my baby name is'+name+'gender is'+ gender +'ageis'+str(age))
my baby name isalvinagender isfemaleageis6
>>> 
>>> 
>>> 'rajesh'
SyntaxError: incomplete input
>>> 
>>> 
>>> # type 2 = string repetition
>>> #----------------------------
>>> 
>>> name
'alvina'
>>> name*6
'alvinaalvinaalvinaalvinaalvinaalvina'
>>> name=' alvina '
>>> name*5
' alvina  alvina  alvina  alvina  alvina '
>>> name*500
' alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina  alvina '
@# function is an indepened.
# depened function is methods
