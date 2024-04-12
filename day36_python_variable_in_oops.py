Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # OOPS
>>> # ----
>>> 
>>> # class / object / abstraction / encapsulation / polymorphism / inheritance / self / __init__
>>> 
>>> # variables in oops
>>> # -----------------
>>> 
>>> # class variable
>>> # local variable
>>> # global variable
>>> 
>>> # class var = if a var is declared inside class and outside of all cls methods, then it is accessed by all cls methods
>>> 
>>> # NOTE : if a function is declared inside the class then it is called as methods
>>> 
>>> class cr7:
...     var = 'ac,tv,light'
...     def m1(self):
...         print('rk is having access to use',cr7.var)
...     def m2(self):
...         print('bablu also having access to use',cr7.var)
...     def m3(self):
...         print('ragu also having access to use',cr7.var)
... 
...         
>>> c = cr7()
>>> 
>>> # c = object
>>> # cr7 - class
>>> 
>>> c.var()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c.var()
TypeError: 'str' object is not callable
c.var
'ac,tv,light'

c.m1()
rk is having access to use ac,tv,light
c.m2()
bablu also having access to use ac,tv,light
c.m3()
ragu also having access to use ac,tv,light


# local variable
# --------------

# if a var is declared inside a specific method, then it should be accessible only to that method

class family:
    def rk(self):
        v = 'M.E degree holder with silver medal'
        print('rk qualification is',v)
    def raja(self):
        print('raja qualification is B.com')
    def nimmy(self):
        print('nimmy qulification is B.sc,B.A,B.ed,M.ed')
        print('nimmy is trying to use',v)

        
f = family()

f.rk()
rk qualification is M.E degree holder with silver medal

f.nimmy()
nimmy qulification is B.sc,B.A,B.ed,M.ed
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    f.nimmy()
  File "<pyshell#53>", line 9, in nimmy
    print('nimmy is trying to use',v)
NameError: name 'v' is not defined


# global variable
# ---------------

# if a variable is declared outside of class and still accessible using global keyword

v1 = 'karnataka bank atm'

class sla:
    def sla_trainers(self):
        print('if sla trainers are having an atm card then they may use',v1)
    def sla_students(self):
        print('if any students are having an atm card then they may use',v1)
    def tresspasser(self):
        print('valipokkan also use',v1)

        
a = sla()

a.sla_students()
if any students are having an atm card then they may use karnataka bank atm
a.sla_trainers()
if sla trainers are having an atm card then they may use karnataka bank atm
a.tresspasser()
valipokkan also use karnataka bank atm


a.sla_students
<bound method sla.sla_students of <__main__.sla object at 0x000002B0BA2F3400>>

