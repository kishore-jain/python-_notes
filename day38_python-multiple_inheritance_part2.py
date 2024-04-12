OPython 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# multiple inheritance
# --------------------

# if a single child is accessing the properties of multiple independent parent class

class HDFC:
    def customer(self):
        print('rk is one of the salaried professional customer')

        
class Lic:
    def policyholder(self):
        print('rk is having 3 polices in lic')

        
class Postoffice:
    def user(self):
        print('rk is having an acc in dgl post office')

        
class Rk(HDFC,Lic,Postoffice):
    ''' common to all these parent cls '''

    
r = Rk()

r.customer()
rk is one of the salaried professional customer

r.policyholder()
rk is having 3 polices in lic

r.user()
rk is having an acc in dgl post office


# multilevel inheritance
# ----------------------

# if a child is inheriting the prop of another inherited child of previous stage






class First:
    def f1(self):
        print('access granted for f1')

        
class Two(First):
    def f2(self):
        print('access granted for f2')

        
class Three(Two):
    def f3(self):
        print('access granted for f3')

        
# Three - f3, f2, f1

# Two - f2, f1

# first - f1

t = Three()

t.f2()
access granted for f2
t.f3()
access granted for f3
t.f1()
access granted for f1

tw = Two()

tw.f2()
access granted for f2
tw.f1()
access granted for f1

f = First()

f.f1()
access granted for f1


# hierarchical inheritance
# ------------------------

# if a single parent is having multiple childeren, then each childeren might have a limited restricted access to that parent

class Abraham:
    def pension(self):
        print('appa is getting pension of 32500 per month')

        
>>> class Raja(Abraham):
...     def operationmanager(self):
...         print('raja getting gud salary from his profession')
... 
...         
>>> class Rk(Abraham):
...     def Trainingmanager(self):
...         print('rk is getting gud salary too from sla')
... 
...         
>>> 
>>> r = Rk()
>>> 
>>> r.Trainingmanager()
rk is getting gud salary too from sla
>>> r.pension()
appa is getting pension of 32500 per month
>>> 
>>> rg = Raja()
>>> 
>>> rg.operationmanager()
raja getting gud salary from his profession
>>> rg.pension()
appa is getting pension of 32500 per month
>>> 
>>> 
>>> 
========================================== RESTART: C:/Python310/polymorphism_program.py ==========================================
rk 38 male
----------------------
Traceback (most recent call last):
  File "C:/Python310/polymorphism_program.py", line 29, in <module>
    m = Mointor('muzza','22','male','vellore','mba')
NameError: name 'Mointor' is not defined. Did you mean: 'Monitor'?
