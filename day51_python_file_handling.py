Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # file handling
>>> # -------------
>>> 
>>> # file is used to store the data and info result in a permanent way.
>>> # usually file stores output in the format of text (.txt file)
>>> 
>>> # file handiling access modes
>>> # ---------------------------
>>> 
>>> # 'r' - default mode for reading data from a file
>>> # 'w' - writing mode to allow data to be written in a file
>>> # 'a' - append mode (writes new data with old data)
>>> # 'r+' - first it checks for file existence then reads content
>>> # 'w+' - overriding mode (deletes old data and stores only new data)
>>> # 'a+' - appends both old and new data together after checking file
>>> 
>>> # file operations
>>> # ---------------
>>> 
>>> # to work with file handling we need a file object
>>> 
>>> # f.read()
>>> # f.readline()
>>> # f.readlines()
>>> # f.write()
>>> # f.writelines()
>>> # f.open()
>>> # f.close()
>>> 
>>> f = open('alvi.txt')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f = open('alvi.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'alvi.txt'
f = open('alvi.txt','w')

f.write('my fav tamil films so far in last 3 decades \n1.vikram \n2.sagalagala vallavan \n3.enakkula oruvan \n4.sathya')
105

# ram,heep,hashtable - these three actives when the system is turned on
# heep - runtime memory
# hashtable - means stores the task location in a  system

# here - f.write para is stored in heep now
# to excute the para in notepad close the file

f.close()

f=open('alvi.txt','r')
f.read()
'my fav tamil films so far in last 3 decades \n1.vikram \n2.sagalagala vallavan \n3.enakkula oruvan \n4.sathya'
f.read()
''
# read only once


f=open('1.cgi.txt','r')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    f=open('1.cgi.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: '1.cgi.txt'

f.readline()
''
f.close()
f.readline()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.
f.close()

f=open('alvi.txt','r')

f.readline()
'my fav tamil films so far in last 3 decades \n'
f.readline()
'1.vikram \n'
f.readline()
'2.sagalagala vallavan \n'
f.readline()
'3.enakkula oruvan \n'
f.readline()
'4.sathya'
f.readline()
''

f.close
<built-in method close of _io.TextIOWrapper object at 0x0000019B3874D8A0>

f.close()

# readlines

f=open('alvi.txt','r')

f.readlines()
['my fav tamil films so far in last 3 decades \n', '1.vikram \n', '2.sagalagala vallavan \n', '3.enakkula oruvan \n', '4.sathya']

# write lines

flim = ['\nbilla','\nyennai arinthall','\nkadhalar dhinam','\nroja','\nazhagi','\nnanban','\nfriends','\nsurra','\npadaiyappa']
'
f=open('alvi.txt','a+')# ?

f.writelines(film)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    f.writelines(film)

NameError: name 'film' is not defined
f.writelines(flim)

f.close()

f=open('alvi.txt','r')
f.read(5)
'my fa'

f.read(5)
'v tam'
f.read(5)
'il fi'
f.read(5)
'lms s'
f.read(5)
'o far'
f.read(5)
' in l'
f.read(5)
'ast 3'
f.read(5)
' deca'


f=open('alvi.txt','w+')
f.writelines(flim)
f.close()

============================================== RESTART: C:/Python310/file_program.py ==============================================
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

============================================== RESTART: C:/Python310/file_program.py ==============================================
Traceback (most recent call last):
  File "C:/Python310/file_program.py", line 9, in <module>
    pat()
  File "C:/Python310/file_program.py", line 5, in pat
    f.write(i)
TypeError: write() argument must be str, not int

============================================== RESTART: C:/Python310/file_program.py ==============================================

============================================== RESTART: C:/Python310/file_program.py ==============================================
