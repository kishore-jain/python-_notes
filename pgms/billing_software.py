from tkinter import*
import random
from tkinter import messagebox
import os
root=Tk()
root.title('billing slip')
root.geometry('1280x720')
bg_color='#4D0039'

#============Variable================
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
Quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))

global l
l=[]
#===================Function============
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,'\t Welcome Murali Laptop Service Center')
    textarea.insert(END,f'\n\n Bill Number:\t\t{bill_no.get()}')
    textarea.insert(END,f'\n Customer Name:\t\t{c_name.get()}')
    textarea.insert(END,f'\n Phone Number:\t\t{c_phone.get()}')
    textarea.insert(END,f'\n=======================================')
    textarea.insert(END,f'\n Product\t\t QTY\t\t Price')
    textarea.insert(END,f'\n=======================================\n')
    textarea.configure(font='arial 12 bold')


def additm():
    n=Rate.get()
    m=Quantity.get()*n
    l.append(m)
    if item.get()=='':
        messagebox.showerror('Error','Please Enter the item')
    else:
        textarea.insert((10.0+float(len(l)-1)),f'\n{item.get()}\t\t{Quantity.get()}\t\t{m}')

def gbill():
    if c_name.get()=='' or c_phone.get()=='':
        messagebox.showerror('Error','Customer Details are must')
    else:
        text=textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END,text)
        textarea.insert(END,f'\n======================================')
        textarea.insert(END,f'\nTotal Paybill Amount:\t\t\t{sum(l)}')
        textarea.insert(END,f'\n======================================')
        
         
def save():
    data=textarea.get(1.0,END)
    f1=open('records/'+str(bill_no.get())+'.txt','w')
    f1.write(data)
    f1.close()
    messagebox.showinfo('Saved',f'Bill no:{bill_no.get()} Saved successfully')
   
def print():
    data=textarea.get(1.0,END)
    f='C:\\Python37\\project\\records\\'+str(bill_no.get())+'.txt'
    os.startfile(f,'print')
    
def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    op=messagebox.askyesno('Exit','Do you really want to exit')
    if op>0:
        root.destroy()
                    

#=================Top Section=============
title=Label(root,text='Billing Software',bg=bg_color,fg='white',font=('times new roman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)
#========================Customer Details==============
F1=LabelFrame(root,text='Customer Details',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='gold')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new rommon',18,'bold'),bg=bg_color,fg='white')
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone NO',font=('times new rommon',18,'bold'),bg=bg_color,fg='white')
cphone_lbl.grid(row=0,column=2,padx=10,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_phone)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)

#=======================Product Details=================
F2=LabelFrame(root,text='Product Details',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='gold')
F2.place(x=20,y=200,width=800,height=1000)

itm=Label(F2,text='Product Name',font=('times new rommon',18,'bold',),bg=bg_color,fg='lightgreen')
itm.grid(row=0,column=0,padx=30,pady=20)
itm_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)

rate=Label(F2,text='Product Rate',font=('times new rommon',18,'bold',),bg=bg_color,fg='lightgreen')
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)

quantity=Label(F2,text='Product Quantity',font=('times new rommon',18,'bold',),bg=bg_color,fg='lightgreen')
quantity.grid(row=2,column=0,padx=30,pady=20)
quantity_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Quantity)
quantity_txt.grid(row=2,column=1,padx=30,pady=20)

#=============================button===================

btn1=Button(F2,text='Add item',font='arial 15 bold',padx=5,pady=5,bg='lime',width=10,command=additm)
btn1.grid(row=3,column=0,padx=20,pady=10)


btn2=Button(F2,text='Generate Bill',font='arial 15 bold',padx=5,pady=5,bg='lime',width=10,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3=Button(F2,text='Save',font='arial 15 bold',padx=5,pady=5,bg='lime',width=10,command=save)
btn3.grid(row=3,column=2,padx=10,pady=30)

btn4=Button(F2,text='Print',font='arial 15 bold',padx=5,pady=5,bg='lime',width=10,command=print)
btn4.grid(row=4,column=0,padx=10,pady=30)


btn5=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=5,bg='lime',width=10,command=clear)
btn5.grid(row=4,column=1,padx=10,pady=30)


btn6=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=5,bg='lime',width=10,command=exit)
btn6.grid(row=4,column=2,padx=10,pady=30)


#==========================bill area==================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=800,y=200,width=500,height=1000)


bill_title=Label(F3,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.mainloop()


