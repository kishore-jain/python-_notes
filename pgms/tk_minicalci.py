from tkinter import *
from PIL import ImageTk, Image
class MyWindow:
    def __init__(self, win):
        # label intro
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=100)
        self.lbl3.place(x=100, y=200)
        # entry intro
        self.e1=Entry()
        self.e2=Entry()
        self.e3=Entry()
        self.e1.place(x=200, y=50)
        self.e2.place(x=200, y=100)
        self.e3.place(x=200, y=200)
        # button intro
        self.b1=Button(win, text='Add', command=self.addition,bg='yellow')
        self.b2=Button(win, text='Subtract',command=self.subtraction,bg='yellow')
        self.b3=Button(win, text='Multiply',command=self.multiplication,bg='yellow')
        self.b4=Button(win, text='Divide',bg='yellow')
        self.b4.bind('<Button-1>', self.division)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=300, y=150)
        self.b4.place(x=400, y=150)
    # add fn creation    
    def addition(self):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1+num2
        self.e3.insert(END, str(result))
    # sub fn creation   
    def subtraction(self):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1-num2
        self.e3.insert(END, str(result))
    # Mul fn creation   
    def multiplication(self):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1*num2
        self.e3.insert(END, str(result))
    # Div fn creation   
    def division(self,event):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1/num2
        self.e3.insert(END, str(result))
        
# object cration
win=Tk()
mywin=MyWindow(win) # mywin - obj, MyWindow - 
win.title('Hello Python')
win.config(bg='cyan')
win.geometry("700x700")
path="calcii.jpg"
url = ImageTk.PhotoImage(Image.open(path))
p1 = Label(win, image = url,height=1000,width=750)
p1.pack(side="right")

win.mainloop()
