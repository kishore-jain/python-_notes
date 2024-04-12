from tkinter import *
gk=Tk()
gk.title('Student info')
gk.configure(bg='#4D0039')
gk.geometry('400x400')

#Label
#-----
l1=Label(gk,text='student name',bg='cyan',fg='blue',font=('Arial',18))
l1.grid(row=0,column=0)

l2=Label(gk,text='student city',bg='cyan',fg='blue',font=('Arial',18))
l2.grid(row=1,column=0)

l3=Label(gk,text='student gender',bg='cyan',fg='blue',font=('Arial',18))
l3.grid(row=2,column=0)

l4=Label(gk,text='student degree',bg='cyan',fg='blue',font=('Arial',18))
l4.grid(row=3,column=0)

l5=Label(gk,text='student lang',bg='cyan',fg='blue',font=('Arial',18))
l5.grid(row=4,column=0)

l6=Label(gk,text='studen KYC Doc',bg='cyan',fg='blue',font=('Arial',18))
l6.grid(row=5,column=0)

l7=Label(gk,text='student date of birth',bg='cyan',fg='blue',font=('Arial',18))
l7.grid(row=6,column=0)

l8=Label(gk,text='student desctionrip',bg='cyan',fg='blue',font=('Arial',18))
l8.grid(row=7,column=0)


# Button
# ------
def life():
    name =e1.get()
    city =e2.get()
    #degree =combo.get()
    
    l1.config(text='student name : '+ name)
    l2.config(text='student city : '+ city)
    l4.config(text='student degree : '+ degree)
b1=Button(gk,text="get Details",bg='green',fg='white',command=life)
b1.place(x=200,y=400)
b2=Button(gk,text="Quit",bg='green',fg='white')
b2.place(x=300,y=400)

# Entry
# -----

e1= Entry(gk,width=20)
e1.grid(row=0,column=1)
e2= Entry(gk,width=20)
e2.grid(row=1,column=1)


# combobox
# --------
from tkinter.ttk import *
combo = Combobox(gk)
combo['value']=('BE','BSC','MBA','BCA','MCOM')
combo.grid(row=3,column=1)

# checkbutton
# -----------
state = BooleanVar()
state.set(False)

state1 = BooleanVar()
state1.set(False)

state2 = BooleanVar()
state2.set(False)

state3 = BooleanVar()
state3.set(False)

state4 = BooleanVar()
state4.set(False)

state5 = BooleanVar()
state5.set(False)

cb = Checkbutton(gk,text='tamil',var=state).grid(row=4,column=1)
cb1 = Checkbutton(gk,text='English',var=state1).grid(row=4,column=2)
cb2 = Checkbutton(gk,text='Hindi',var=state2).grid(row=4,column=5)
cb3 = Checkbutton(gk,text='Aadhar',var=state3).grid(row=5,column=1)
cb4 = Checkbutton(gk,text='Voter ID',var=state4).grid(row=5,column=2)
cb5 = Checkbutton(gk,text='PAN',var=state5).grid(row=5,column=5)

# Radiobutton
# -----------
select = StringVar()

rb = Radiobutton(gk,text='Male',value ='Male',variable=select).grid(row=2,column=1)
rb1 = Radiobutton(gk,text='Female',value ='Female',variable=select).grid(row=2,column=3)
# Spinbox
# -------
date = Spinbox(gk,from_=1,to=31,width=5).grid(row=6,column=1)
month = Spinbox(gk,from_=1,to=12,width=5).grid(row=6,column=2)
year = Spinbox(gk,from_=1975,to=2050,width=5).grid(row=6,column=3)
# scrolledtext
# ------------

from tkinter import scrolledtext
st = scrolledtext.ScrolledText(gk,height=5,width=20)
st.insert(INSERT,'Type your opinion about students')
st.grid(row=7,column=1)


gk.mainloop()
