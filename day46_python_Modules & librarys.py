Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# modules
# -------

# module means pre defined program from python community.
# module means user created python program.

import calendar

# module --> user created python programs

# package --> collections of module
import calendar
month=2
year= 5
x=calendar.month(month,year)
print(x)
       May 2
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31


# library --> publicly available licensed package

# library --> package --> module --> class --> function --> var --> data

# modules benefits
# ----------------

# memory optimisation
# lesser code
# time consupmtion
# code reusability
# user friendly access
# simplified usage

# type of modules importation
# ----------------------------
# type 1 : import modulename
# type 2 : from modulename import *
# type 3 : from modulename import function name

import math

dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.factorial(5)
120

# type 2
# ------

from math import *

# Type 3
# ------

from math import factorial

# mainly use second or third types it can data  reduces

from math import factorial,float,ceil
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    from math import factorial,float,ceil
ImportError: cannot import name 'float' from 'math' (unknown location)
from math import factorial,ceil,floor
factorial(3)
6

# Type of modules
# ---------------

>>> # os module
>>> # sys module
>>> # time module
>>> # datatime module
>>> # calender module
>>> # holidays module
>>> # random module
>>> # pyscreenshoot module
>>> # qrcode module
>>> # playsound module
>>> 
>>> import holidays
>>> 
>>> rk = holidays.india(years=2023)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    rk = holidays.india(years=2023)
AttributeError: module 'holidays' has no attribute 'india'. Did you mean: 'India'?
>>> import holidays

>>> rk = holidays.india(years=2023)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    rk = holidays.india(years=2023)
AttributeError: module 'holidays' has no attribute 'india'. Did you mean: 'India'?
>>> rk = holidays.India(years=2023)
>>> for i in rk.items():
... print(f'{i} -->{j}')
SyntaxError: expected an indented block after 'for' statement on line 1


