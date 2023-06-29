# mainWindow
from tkinter import *
from tkinter import messagebox
import math, time
import time
import threading
from pageFrames import *
import matplotlib

def get_time(self):
        clock = Label(self,text='',font=28)
        clock.place(x=25, y=240)
        while True:
            clock.configure(text=time.strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(1)

class mainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.root.geometry("400x500")
        self.createPage()

    def createPage(self):
        thread = threading.Thread(target=get_time)
        thread.setDaemon(True)
        thread.start()

    
