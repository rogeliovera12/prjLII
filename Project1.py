from tkinter import*
from time import sleep
import songs
mainwindow = Tk()

def functionA():
    global counter
    counter = +1
    if counter == 1:
       songs.testbois()
       print("Playing Song 1")
    else: counter == 0
    print("Please pick a song")


#print ("Playing Song 1",counter)

def functionB():
    global counter
    counter = +2
    if counter == 2:
        print("Playing song 2")
    else: counter == 0
    print("please pick a song")
        
    

def functionC():
    global counter
    counter = +3
    Label.config(text = counter)
    print("Playing Song 3",counter)


def functionD():
    global counter
    counter = +4
    Label.config(text = counter)
    print("Playing Song 4", counter)



Label = Label(mainwindow, text = "")
Abutton = Button(mainwindow, text = " Song 1" ,command = functionA)
Bbutton2 = Button(mainwindow, text = "Song 2", command  = functionB)
Cbutton3 = Button(mainwindow, text = " Song 3", command = functionC)
Dbutton4 = Button(mainwindow, text = "Song 4", command  = functionD)

Abutton.pack()
Bbutton2.pack()
Cbutton3.pack()
Dbutton4.pack()

mainwindow.geometry("500x500")
mainwindow.mainloop()
