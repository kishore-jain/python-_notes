import tkinter as ki
from tkinter.filedialog import askdirectory
import pygame as p
import os
import time
print("********************My mp3 player**********************")
class new:
    def fselect(self):
        ki.Tk().withdraw()#used to open gui window and hide it
        fname=askdirectory()#used to select a folder using windows explorer
        return fname
       
    def sselect(self,fname):
        songlist=os.listdir(fname)#used to list the contents of a directory
        b=1
        for i in songlist:
            print(b,i)
            b+=1
        n=int(input("enter song number to play or enter '0' to play all songs"))
        p.mixer.init()#intialize sonund mixer py game
        print("100 is maximum volume 1 is least ")
        v1=float(input(" "))
        v=v1/10
        p.mixer.music.set_volume(v)#setting volume
        if n==0:
            NEXT= p.USEREVENT + 1
            tracknum=len(songlist)
            current_track =0
            p.init()#we are initializing a event loop
            screen = p.display.set_mode((800,600))# used to crete sceen when cosses end opp
            p.mixer.init()
            p.mixer.music.load(fname+"/"+songlist[current_track])
            print("playing",songlist[current_track])
            p.mixer.music.play()#playing first track
            p.mixer.music.set_endevent(NEXT)
            running = True
            while running:
                for event in p.event.get():
                    if event.type ==p.QUIT:
                        running= False
                    elif event.type == NEXT:
                        try:
                            current_track=(current_track + 1)%tracknum
                            print("playing:",songlist[current_track])
                            p.mixer.music.load(fname+"/"+songlist[current_track])
                            p.mixer.music.play()
                        except:
                            p.quit()
            p.quit()
            '''p.mixer.music.load(fname+"/"+songlist[0])
            print("song playing",songlist[0])
            p.mixer.music.play()
            for x in songlist[1:]:
                p.mixer.music.queue(fname+"/"+x)
                p.mixer.music.play()
                #time.sleep(120)'''
                
                                
        else:
            p.mixer.music.load(fname+"/"+songlist[n-1])
            print("song playing",songlist[n-1])
            p.mixer.music.play()
        
        while 1:
            print("press 'p' to pause,'r'to resume")
            print("press 'n'to play new song")
            print("press 'e' to exit")
            option=input("")
            if option == 'p':
                p.mixer.music.pause()
            elif option == 'r':
                p.mixer.music.unpause()
            elif option == 'e':
                p.mixer.music.stop()
                break      
            elif option== 'n':
                new.sselect(self,fname)
a=new()               
a.sselect(a.fselect())


