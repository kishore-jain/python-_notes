from tkinter import * # second type of module importation

from PIL import ImageTk, Image # PIL - python photo image library

root = Tk() # crated parent window

url = ImageTk.PhotoImage(Image.open("alvina.jpg")) # general syntax to open jpeg img

p1 = Label(root, image = url)

p1.pack(side = "left", fill = "both")

root.mainloop() # to trigger input actions from user @ runtime





# usually photoimage process only .png images

# in addition to use and open a.jpg image, i use image function along side imagetk

# "C:\Users\SASIKUMAR\Desktop\web_shape.jpg"

'''logoImage=PhotoImage(file='C:\Python310\1-MAIN- Restaurant  Management  project\image\RMSgmail.PNG.png')
    label=Label(root2,image=logoImage,bg='red4')
    label.pack()'''
