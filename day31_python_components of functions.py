Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# COMPONENTS OF A FUNCTION
# -------------------------

# parameter - [place holder/value container]-name,age,city,hight,weight,skintone,degree,salary

# Argument - actual value to be stored in parameter-(ex holds parameter value : kishore,22,elavur,.....)

# Types of function in python
# ---------------------------
# 1. builtin functions
# 2. math functions
# 3. user defined functioms
# 4. recursive functions
# 5. lambda functions

# 1. built in functions
# ---------------------

# default function / in build function / predefined function /system function / readymade function /internal functions

# also mainly called as IMPLICIT FUNCTION -ans in interview

# build in functions  are represented in PURPLE color

# List of build in functions
# --------------------------

import builtins
dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# , 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'

# importan built in function

abs(-8)
8
# doest not cares about the math function show only the value

bin(8)
'0b1000'
# show binary value

bool(0)
False

bool(1)
True

# show boolen true or false

chr(65)
'A'

# show character value

complex(10)
(10+0j)
# converts into complex value

divmod(11,4)
(2, 3)

# 2 is quotent and 3 is reminder - act division

'kishore'
'kishore'

for i in ('positive kishore'):
    print(i)

    
p
o
s
i
t
i
v
e
 
k
i
s
h
o
r
e
for i in enumerate('positive kishore'):
    print(i)

    
(0, 'p')
(1, 'o')
(2, 's')
(3, 'i')
(4, 't')
(5, 'i')
(6, 'v')
(7, 'e')
(8, ' ')
(9, 'k')
(10, 'i')
(11, 's')
(12, 'h')
(13, 'o')
(14, 'r')
(15, 'e')

# show in index of the string using enumerate function

'34'+'67'
'3467'
55+98
153

eval('30+40')
70
# evaulate the given maths


max(67,84,49)
84
>>> 
>>> min(67,39,65)
39
>>> # it show max or min values
>>> 
>>> ord('a')
97
>>> 
>>> chr(97)
'a'
>>> 
>>> # show the equalent assicc value
>>> 
>>> pow(5,3)
125
>>> 
>>> # powers of gives values ->5,3 =5*5*5 here 1st value and after,3 is three times
>>> 
>>> 
>>> for i in reversed('kishore'):
...     print(i,end=' ')
... 
...     
e r o h s i k 
>>> # its show reversed of string values
>>> 
>>> sum([54,65,24])
143
