from tkinter import *
root=Tk()# Tk mean toolskit ,root represent root
root.title('student info')
root.configure(bg='cyan')
root.geometry('600x600')
# label 
#-------
l_name = Label(root,text='student Name',bg='yellow',fg='blue',font=('Arial',10))
l_name.grid(row=0,column=0)
#l_name.pack()
#l_name.place(x=50,y=50)

l_city = Label(root,text='student city',bg='yellow',fg='blue',font=('Arial',10))
#l_city.place(x=50,y=100)
l_city.grid(row=1,column=0)

l_gender = Label(root,text='student gender',bg='yellow',fg='blue',font=('Arial',10))
#l_gender.place(x=50,y=150)
l_gender.grid(row=2,column=0)

l_degree = Label(root,text='student degree',bg='yellow',fg='blue',font=('Arial',10))
l_degree.grid(row=3,column=0)

l_lang = Label(root,text='Language Skills',bg='yellow',fg='blue',font=('Arial',10))
l_lang.grid(row=4,column=0)

l_dob = Label(root,text='Date of birth',bg='yellow',fg='blue',font=('Arial',10))
l_dob.grid(row=5,column=0)

l_dos = Label(root,text='Description of student',bg='yellow',fg='blue',font=('Arial',10))
l_dos.grid(row=6,column=0)
# Entry
e1 = Entry(root, width=35)
e1.grid(row=0,column=1)
e2 = Entry(root, width=35)
e2.grid(row=1,column=1)
#e3 = Entry(root, width=25)
#e3.grid(row=2,column=1)
#e4 = Entry(root, width=25)
#e4.grid(row=3,column=1)
#------
# button
# ------
def info():

    name =e1.get()
    city =e2.get()
   # gender=e3.get()
    degree = combo.get()

    l_name.config(text='student name : '+name)
    l_city.config(text='student city : '+city)
   # l_gender.config(text='student gender: '+gender)
    l_degree.config(text='student degree: '+degree)
     

b1 = Button(root,text="get details",bg='green',fg='white',command = info)
#b1.grid(row=8,column=0)
b1.place(x=100,y=500)
b2 = Button(root,text="quit",bg='green',fg='white')
b2.place(x=250,y=500)

# combobox
#----------
from tkinter.ttk import *
combo = Combobox(root)
combo['values'] = ('BE','BSC','BCOM','BBA','MSC','MCOM','MBA')
combo.grid(row=3,column=1)

# checkbutton
# -----------
status = BooleanVar()
status.set(True)

status1 =BooleanVar()
status1.set(False)

status2 =BooleanVar()
status2.set(False)

cb = Checkbutton(root,text='Tamil',var=status).grid(row=4,column=1)
cb1 = Checkbutton(root,text='English',var=status1).grid(row=4,column=2)
cb2 = Checkbutton(root,text='Hindi',var=status2).grid(row=4,column=9)

# Radiobutton
# -----------
select = StringVar() #?

rb = Radiobutton(root,text='Male', value ='Male',variable = select).grid(row=2,column=1)
rb1 = Radiobutton(root,text='Female', value ='Female',variable = select).grid(row=2,column=2)

# Spinbox
# -------
date = Spinbox(root,from_=1,to=31,width=5).grid(row=5,column=1)
month = Spinbox(root,from_=1,to=12,width=5).grid(row=5,column=2)
year = Spinbox(root,from_=1975,to=2030,width=7).grid(row=5,column=3)

# scrolledtext
# ------------
from tkinter import scrolledtext
st = scrolledtext.ScrolledText(root,height=5,width=20)
st.insert(INSERT,'Type your opinion about student')
st.grid(row=6,column=1)


