Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# math functions
# --------------

import math

dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


math.cell(56.2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    math.cell(56.2)
AttributeError: module 'math' has no attribute 'cell'. Did you mean: 'ceil'?
math.ceil(56.2)
57
math.ceil(45.6)
46
math.ceil(44.4)
45
math.ceil(44.5)
45
# ceil means it can change hight values 44.5 can change 45.

math.floor(34.9)
34
math.floor(84.34)
84
# floor means it can change minimum value 84.34 can change 84

math.comb(5,2) # (5*4)/(2*1)
10
math.comb(5,3) # (5*4*3)/(3*2*1)
10

# ------------------------------
math.perm(5,3) # (5*4*3)
60

# ------------------------------
math.copysign(20,-4)
-20.0
# it can be change second value signe (20, -4 )values -20.0

20/5
4.0
# -------------------------------

math.degrees(300)
17188.733853924696

math.radians(17188.734)
300.000002549495
# -------------------------------
math.exp(1)
2.718281828459045
#---------------------------------
math.fabs(-4)
4.0
# it change values 4 is -4.0
# --------------------------------
math.factorial(5) # 5*4*3*2*1
120
# --------------------------------

math.fmod(10,6)
4.0
math.fmod(17,9)
8.0
# ---------------------------------

math.fsum([20,30,40,50])
140.0
# sum of all values
# -----------------------------------
math.gcd(15,20)
5
math.gcd(12,20)
4
# 12==>2,3,4,6,12
# 20==>2,4,5,10,20


# GCD= Means ==> greatest common divisor
# ----------------------------------------

# 10 =100
# 11 = 121
>>> # 12 = 144
>>> # 13 = 169
>>> # 14 = 196
>>> # 15 = 225
>>> # 16 = 256
>>> # 17 = 289
>>> # 18 = 324
>>> # 19 = 361
>>> # 20 = 400
>>> 
>>> math.isqrt(200)
14
>>> math.isqrt(260)
16
>>> math.isqrt(310)
17
>>> math.isqrt(361)
19
>>> math.isqrt(300)
17
>>> # =----------------------------------------
>>> 
>>> math.sqrt(300)
17.320508075688775
>>> # sqrt currect squroot of value is 300
>>> 17.32 * 1732
29998.24
# --------------------------------------------

math.log10(1000)
ans = 3.0
# -------------------------------------------
math.pi
 ans = 3.141592653589793


 # --------------------------------------------
 math.pow(10,3)
 1000.0

 math.pow(10,2)
 100.0

 math.pow(10,1)
 10.0
 # ----------------------------------------------
 math.trunc(23.0987654321)
 23

 math.trunc(65.123456789)
 65
 # task
 # math functions real world applications:-
