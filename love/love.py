from tkinter import *
from tkinter import messagebox

def closeWindow():
    messagebox.showinfo(title='警告', message='不许关闭，认真作答')
    return

def closeallwin():
    window.destroy()

def No_love():
    no_love = Toplevel()
    no_love.geometry("300x100+610+260")
    no_love.title("这样下去不行的")
    label = Label(no_love, text="再考虑考虑嘛", font=('宋体', 25))
    label.pack()

def Love():
    # print("刚好我也是")
    love = Toplevel()
    love.geometry("300x100+610+260")
    love.title("好巧啊，我也是")
    label = Label(love, text="好巧啊，我也是", font=("楷体", 25))
    label.pack()
    btn = Button(love, text='确定', width=10, height=2, command=closeallwin)
    btn.pack()

# 创建窗口
window = Tk()

# 设置窗口标题
window.title("七夕节快乐~")
# 设置窗口大小（前两个参数）     设置窗口位置（后两个参数）
window.geometry("400x450+600+200")

# 当用户关闭，出触发这个方法
# window.protocol("WM_CLOSE_WINDOW", closeWindow())

# 标签控件
label1 = Label(window, text="hey,baby", font=('微软雅黑', 15), fg='red')
# 定位 grid  网格式布局
label1.grid()
label2 = Label(window, text="Do you like me ?", font=('微软雅黑', 25), fg='orange')
# sticky 对齐方法 E S W N
label2.grid(row=1, column=1, sticky=E)

# 显示图片
photo = PhotoImage(file='./gf_love.jpg')
imageLabel = Label(window, image=photo)
# columnspan 组件跨越的列数
imageLabel.grid(row=2, columnspan=2)
imageLabel.grid(row=2, columnspan=2)

# 显示按钮
btn1 = Button(window, text='喜欢', width=15, height=2, command=Love)
btn1.grid(row=3, column=0, sticky=W)

btn2 = Button(window, text='不喜欢', command=No_love)
btn2.grid(row=3, column=1, sticky=E)

# 显示窗口  循环
window.mainloop()