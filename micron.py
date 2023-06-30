from tkinter import *
from tkinter import messagebox
from pageFrames import *
from mainWindow import *
from mainPage import *
from sqlite import *

# 主函数
def main():

    # 创建窗口：实例化一个窗口对象。
    root = Tk()

    # 窗口标题
    root.title("我的窗口")

    # 窗口大小
    #root.geometry("600x450")

    page = mainPage(root)
 
    # 开启时钟刷新
    page.clockPage.update()

    #page.mainWindow.createPage()
 
    sqlite()
    
    # 开启界面
    root.mainloop()
 
if __name__ == '__main__':
    main()