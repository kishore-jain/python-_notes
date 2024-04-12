Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#  python language components

# 4. operators
#-------------------------

# arithmetic (+ - * / % // )-->(floor division)
# logical ( and or not)
# relational(> >= < <= == !=)
# assignment (= += -= /= %= //= )
#  membership operator ( in not in )
# identity operator (is is not)

#---------------------------------------------------------------------------

# identity operator
#------------------

a=200

a is 200
True
a is 300
False
a is not 200
False
a is not 300
True

# membership operator (in not in)
#------------------------------------------

'a' in 'alvinas sadhana'
True
'y' in'alvinas sadhana'
False
'a' not in 'alvinas sadhana'
False
'x' not in'alvinas sadhana'
True
'alvinas sadhana'.count('a')
5
# assignment ( =, +=, -=, *=, %=, //=)
#--------------------------------------

#  Note: this operator permanently changes the value

a=30

a+=20 # a=a+20
a
50
a*=2 # a=a*2
a
100
a-=50 # a-50
a
50
a/=2 #a=a/2
a
25.0
a
25.0
a
25.0
a=int (a)
a
25

# arithmetic (+ - * / % //)
#-----------------------------

20+30
50
30-15
15
30/2
15.0
10/3
3.3333333333333335
20*5
100


10%3
1
20%6
2
>>> 30%13
4
>>> 40%15
10
>>> 60%20
0
>>> 12%5
2
>>> # modulo = remainder value ( remainder in tamil = meedhi)
>>> 
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> # //-floor division
>>> 
>>> # // - returns only quotient value
>>> 
>>> 23//3
7
>>> 32//6
5
>>> 20//7
2
>>> 21//8
2
>>> 40//4
10
>>> 20//6
3
