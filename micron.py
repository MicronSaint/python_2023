from tkinter import *
from tkinter import messagebox
import math, time
import time
import threading

def func():
    result = entry.get()  # 获取文本输入框的内容
    print(result) 
    label = Label(root,text= result ,font=("宋体",25),fg="black")
    # 定位
    label.grid()
    #label.grid(row=3,column=2)
def funcdel():
    result = entry.delete(0, END)# 删除文本输入框的内容

# 创建窗口：实例化一个窗口对象。
root = Tk()

#  窗口标题
root.title("我的窗口")

# 窗口大小
root.geometry("600x450")
 
#添加标签控件
label = Label(root,text="输入框",font=("宋体",25),fg="black")
"""
text参数用于指定显示的文本；
font参数用于指定字体大小和字体样式；
fg参数用于指定字体颜色；
"""
# 定位
label.grid()

# 添加输入框
entry = Entry(root,font=("宋体",25),fg="black")
entry.grid()

# 添加点击按钮
button = Button(root,text="确定",font=("宋体",25),fg="blue",command=func)
button.grid(row=3,column=4)

button = Button(root,text="取消",font=("宋体",25),fg="blue",command=funcdel)
button.grid(row=3,column=9)


clock = Label(root,text='',font=28)
clock.place(x=25, y=240)

def get_time():
     while True:
        clock.configure(text=time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)


thread = threading.Thread(target=get_time)
thread.setDaemon(True)
thread.start()

# 显示窗口
#root.mainloop()
class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()
 
    def createPage(self):
        self.clockPage = clockPage(self.root)  # 创建不同Frame
        #self.weatherPage = weatherPage(self.root)
        self.clockPage.pack()  # 默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='时钟', command=self.clockShow)
        menubar.add_command(label='天气', command=self.weatherShow)
        self.root['menu'] = menubar  # 设置菜单栏
 
    def clockShow(self):
        self.clockPage.pack()
        self.weatherPage.pack_forget()
 
    def weatherShow(self):
        self.clockPage.pack_forget()
        #self.weatherPage.pack()
        
# 主函数
def main():
    #root = tk.Tk()
    #page = MainPage(root)
 
    # 开启时钟刷新
    #page.clockPage.update()
 
    #开启界面
    root.mainloop()
 
 
if __name__ == '__main__':
    main()