from tkinter import *
from tkinter import messagebox
 
def func():
    result = entry.get()  # 获取文本输入框的内容
    print(result) 
def funcdel():
    result = entry.delete(0, END)# 删除文本输入框的内容
    
# 创建窗口：实例化一个窗口对象。
root = Tk()

#  窗口标题
root.title("我的窗口")

# 窗口大小
root.geometry("600x450")
 
#添加标签控件
label = Label(root,text="签名",font=("宋体",25),fg="black")
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
button.grid(row=1,column=1)

button = Button(root,text="取消",font=("宋体",25),fg="blue",command=funcdel)
button.grid(row=1,column=2)

# 显示窗口
root.mainloop()
