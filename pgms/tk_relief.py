from tkinter import *

border_effects={'flat':FLAT, 'sunken':SUNKEN, 'ridge':RIDGE, 'raised':RAISED, 'groove':GROOVE }

window=Tk()

for i,j in border_effects.items():
    f=Frame(master=window,relief=j,borderwidth=30)
    # frame creates partitioned space inside a window
    f.pack()
    
    lbl=Label(master=f,bg='blue',fg='yellow',text=i,font=("Calibri",20))
    lbl.pack()
    
window.mainloop()



















