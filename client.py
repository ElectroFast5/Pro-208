#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openChatWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Music 🎵🎵🎵')
    window.geometry("500x350")
    window.config(bg="cyan")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "🎵 Play Music! 🎵", font = ("Calibri",30),bg="green")
    namelabel.place(x=10, y=8)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10),bg="red")
    listbox.place(x=10, y=70)

    sendButton=Button(window,text="Pause",font=("Calibri",10),bg="orange")
    sendButton.place(x=400,y=180)

    sendButton=Button(window,text="Play",font=("Calibri",10),bg="orange")
    sendButton.place(x=20,y=180)

    sendButton=Button(window,text="Next",font=("Calibri",10),bg="orange")
    sendButton.place(x=20,y=280)

    sendButton=Button(window,text="Download",font=("Calibri",10),bg="orange")
    sendButton.place(x=400,y=280)
  
    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()