import tkinter
import time
from tkinter import ttk
window = tkinter.Tk()

def start_progress():
    for k in range(1, 11):
        progress_var.set(k)
        print("STEP", k)
        k += 1
        time.sleep(2)
        window.update_idletasks()

b1 = tkinter.Button(window, text="START", command=start_progress)
b1.pack(side="left")

progress_var = tkinter.IntVar()

pb = ttk.Progressbar(window,orient="horizontal",length=200, maximum=10,
                     mode="determinate",var=progress_var) # heart of the pgm

pb.pack(side="left")
pb["value"] = 0
window.mainloop()
