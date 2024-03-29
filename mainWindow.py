# mainWindow
from tkinter import *
from tkinter import messagebox
import math, time
import time
import threading
import matplotlib

class mainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.root.geometry("400x500")
        self.createPage()

    def createPage(self):
        clock = Label(self,text='',font=28)
        clock.pack()
        thread = threading.Thread(target=self.get_time, args=(clock,))
        thread.setDaemon(True)
        thread.start()

    def get_time(self,clock):
        while True:
            clock.configure(text=time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)
    
