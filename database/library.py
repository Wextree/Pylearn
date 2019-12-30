# 用于连接 mysql 数据库
import pymysql
# python GUI
import tkinter as tk
import tkinter.messagebox
# 获取时间
import datetime

class library():
    """ 二手书共享书架管理系统"""

    def __init__(self):
        # 存放数据库语句
        self.sql = ""
        self.window = tk.Tk()
        self.title = '欢迎进入二手书共享书架系统！'
        self.picture = '10.gif'
        self.user = tk.StringVar()
        self.pwd = tk.StringVar()
        self.data = ()
        self.no = ""

    # 退出窗口
    def usr_sign_quit(self):
        self.window.destroy()

    # 打开数据库执行sql操作
    def opendatabse(self):
        # 打开数据库表并且获得游标数据以元组返回
        conn = pymysql.connect(
            host='127.0.0.1', user='root', passwd='110325', port=3306, db='library', charset='utf8')
        cur = conn.cursor()
        cur.execute(self.sql)
        data = cur.fetchall()
        # 事务确认
        conn.commit()
        cur.close()
        conn.close()
        return data

    # 注册程序
    def usr_sign_up(self):
        def savepwd():
            # 获取输入信息
            nn = new_name.get()
            idd = id.get()
            np = new_pwd.get()
            npf = new_pwd_confirm.get()

            flag = 0
            for value in self.data:
                if value[0] == nn:
                    tk.messagebox.showerror(message='用户已存在')
                    flag = 1
                elif nn == '' or np == '':
                    tk.messagebox.showerror(message='用户名或者密码不能为空！')
                    flag = -1
                elif np != npf:
                    tk.messagebox.showerror(message='前后密码不一致')
                    flag = -1

            if flag == 0:
                self.sql = 'insert into pwd values(\'' + nn + '\',\'' + np + '\',\'' + idd + '\')'
                print(self.sql)
                print(self.opendatabse())
                tk.messagebox.showinfo('欢迎', '注册成功')
                window_sign_up.destroy()

        window_sign_up = tk.Toplevel(self.window)
        window_sign_up.geometry('350x250')
        window_sign_up.title('注册')
        # 用户名变量及标签、输入框
        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

        # 身份确认框
        id = tk.StringVar()
        tk.Label(window_sign_up, text='身份：').place(x=10, y=50)
        tk.Entry(window_sign_up, textvariable=id).place(x=150, y=50)

        # 密码变量及标签、输入框
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=90)
        tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=90)
        # 重复密码变量及标签、输入框
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=130)
        tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=130)
        # 确认注册按钮及位置
        bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册', command=savepwd)
        bt_confirm_sign_up.place(x=150, y=170)

    # 查看基本信息
    def showdata(self):
        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        self.sql = 'select * from student where sname = \'' + self.user.get() + '\''
        data = self.opendatabse()
        window_top.title('基本信息')
        factory = ['学号：', '名字：', '手机号：', '性别：']
        list = tk.Listbox(window_top)
        for i in range(4):
            list.insert(0, factory[3-i] + data[0][3-i])

        list.pack()

    # 更改基本信息
    def updatedata(self):
        def save_d():
            sex_z = sex.get()
            tele_z = tele.get()
            self.sql = 'update student set Stele = \'' + tele_z + '\',Ssex = \'' + sex_z + '\' where sname = \'' + self.user.get() + '\''
            self.opendatabse()
            tk.messagebox.showinfo('恭喜', '修改成功！')

        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        window_top.title('信息更改选择')

        sex = tk.StringVar()
        tele = tk.StringVar()

        # 设置性别和手机号码
        tk.Label(window_top, text='性别：').place(x=60, y=80)
        tk.Label(window_top, text='电话：').place(x=60, y=120)
        # 输入框
        tk.Entry(window_top, textvariable=sex).place(x=120, y=80)
        tk.Entry(window_top, textvariable=tele).place(x=120, y=120)
        # 提交
        bt = tk.Button(window_top, text='提交', command=save_d)
        bt.place(x=140, y=160)

    # 租书架
    def Rackrent(self):
        def save_d():
            term_z = term.get()
            today = datetime.date.today()
            self.sql = 'insert into rackrent values(\'' + self.no + '\','\
                       + str(now_rack+1) + ',' + str(term_z) + ',\'' + str(today) + '\')'
            self.opendatabse()
            tk.messagebox.showinfo(message='租架子成功')

        self.sql = 'select max(Brno) from bookrack'
        data = self.opendatabse()
        # 获取当前书架总数量
        max_rack = data[0][0]
        self.sql = 'select max(Brno) from Rackrent'
        data = self.opendatabse()
        # 获取已出租的书架数量
        now_rack = data[0][0]
        self.sql = 'select * from Rackrent,Student w' \
                   'here Rackrent.Sno = Student.Sno and ' \
                   'sname = \'' + self.user.get() + '\''
        data = self.opendatabse()


        if now_rack == max_rack:
            tk.messagebox.showerror(message='书架已满，无法出租')
        elif len(data) != 0:
            tk.messagebox.showerror(message='你已经有了一个书架，不必要再租')
        else:
            window_top = tk.Toplevel(self.window)
            window_top.geometry('350x250')
            window_top.title('输入租期')
            term = tk.StringVar()
            tk.Label(window_top, text='租期：').place(x=60, y=120)
            tk.Entry(window_top, textvariable=term).place(x=120, y=120)
            # 提交
            bt = tk.Button(window_top, text='提交', command=save_d)
            bt.place(x=140, y=160)

    # 放书
    def put_book(self):
        def save_d():
            name_z = name.get()
            press_z = press.get()
            price_z = price.get()

            self.sql = 'select * from Book where Bname = \'' + name_z + '\' and press = \'' + press_z + '\''
            data = self.opendatabse()
            if len(data) != 0:
                # 获取书号
                bno = data[0][0]
                # 在学生书籍关系表，还有库存表对应的位置加一
                self.sql = 'update repertory set num = num+1 where bno = \'' + bno + '\''
                self.opendatabse()
                self.sql = 'select * from stubo where bno = \'' + bno + '\' and sno = \'' + self.no + '\''
                data_z = self.opendatabse()
                if len(data_z) == 0:
                    self.sql = 'insert into stubo values(\'' + self.no + '\',\'' + bno + '\',1)'
                    self.opendatabse()
                else:
                    self.sql = 'update stubo set num = num+1 where bno = \'' + bno + '\' and sno = \'' + self.no + '\''
                    self.opendatabse()
            else:
                self.sql = 'select max(bno) from book'
                data = self.opendatabse()
                jur = ""
                bno = str(int(data[0][0]) + 1)
                is_rent = tk.messagebox.askyesno(message="是不是可租")
                if is_rent:
                    jur = jur + 'R'
                is_buy = tk.messagebox.askyesno(message="是不是可卖")
                if is_buy:
                    jur = jur + 'B'
                self.sql = 'insert into Book values(\'' + bno + '\',\'' + name_z + '\',\''\
                           + press_z + '\',' + price_z + ',\'' + jur + '\')'
                self.opendatabse()
                self.sql = 'insert into Repertory values(\'' + bno + '\',1)'
                self.opendatabse()
                self.sql = 'insert into stubo values(\'' + self.no + '\',\'' + bno + '\',1)'
                self.opendatabse()

            tk.messagebox.showinfo(message='存放书籍成功')

        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        window_top.title('书籍信息')
        name = tk.StringVar()
        press = tk.StringVar()
        price = tk.StringVar()

        # 输入书籍信息
        tk.Label(window_top, text='书名：').place(x=60, y=40)
        tk.Label(window_top, text='出版社：').place(x=60, y=80)
        tk.Label(window_top, text='价格：').place(x=60, y=120)
        # 输入框
        tk.Entry(window_top, textvariable=name).place(x=120, y=40)
        tk.Entry(window_top, textvariable=press).place(x=120, y=80)
        tk.Entry(window_top, textvariable=price).place(x=120, y=120)
        # 提交
        bt = tk.Button(window_top, text='提交', command=save_d)
        bt.place(x=140, y=160)

    # 买书
    def buy_book(self):
        def save_d():
            name_z = name.get()
            print(name_z)
            self.sql = 'select book.bno,bname,price,repertory.num from repertory,book ' \
                       'where repertory.bno=book.bno and ' \
                       'repertory.num > 0 and jur like \'%B\' and Bname = \'' + name_z + '\''
            data = self.opendatabse()
            if len(data) == 0:
                tk.messagebox.showerror(message='抱歉，没有你想要的书籍')
                window_top.destroy()
            else:
                bno = data[0][0]
                self.sql = 'select Brno,stubo.sno from Rackrent,stubo ' \
                           'where rackrent.sno = stubo.sno and num > 0 and bno = \'' + bno + '\''
                data = self.opendatabse()
                # 组合消息
                brno = data[0][0]
                sno = data[0][1]
                message = '你要找的《' + name_z + '》有存货，在' + str(brno) + '书架，是否购买？'
                is_buy = tk.messagebox.askyesno(title='找到啦！', message=message)
                # 若是购买
                if is_buy:
                    self.sql = 'update repertory set num = num-1 where bno = \'' + bno + '\''
                    self.opendatabse()
                    self.sql = 'update stubo set num = num-1 where bno = \'' + bno + '\' and sno = \'' + sno + '\''
                    self.opendatabse()
                    today = datetime.date.today()
                    self.sql = 'insert into bought values(\'' + self.no + '\',\'' + bno + '\',1,\'' + str(today) + '\')'
                    self.opendatabse()
                    tk.messagebox.showinfo(message='购买成功')


        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        window_top.title('买书')
        name = tk.StringVar()
        tk.Label(window_top, text='书名：').place(x=60, y=80)
        tk.Entry(window_top, textvariable=name).place(x=120, y=80)
        # 提交
        bt = tk.Button(window_top, text='提交', command=save_d)
        bt.place(x=140, y=160)

    # 租书
    def rent_book(self):
        def save_d():
            name_z = name.get()
            term_z = term.get()
            print(name_z)
            self.sql = 'select book.bno,bname,price,repertory.num from repertory,book ' \
                       'where repertory.bno=book.bno and ' \
                       'repertory.num > 0 and jur like \'R%\' and Bname = \'' + name_z + '\''
            data = self.opendatabse()
            if len(data) == 0:
                tk.messagebox.showerror(message='抱歉，没有你想要的书籍')
                window_top.destroy()
            else:
                bno = data[0][0]
                self.sql = 'select Brno,stubo.sno from Rackrent,stubo ' \
                           'where rackrent.sno = stubo.sno and num > 0 and bno = \'' + bno + '\''
                data = self.opendatabse()
                # 组合消息
                brno = data[0][0]
                sno = data[0][1]
                message = '你要找的《' + name_z + '》有存货，在' + str(brno) + '书架，是否租用？'
                is_buy = tk.messagebox.askyesno(title='找到啦！', message=message)
                # 若是购买
                if is_buy:
                    self.sql = 'update repertory set num = num-1 where bno = \'' + bno + '\''
                    self.opendatabse()
                    self.sql = 'update stubo set num = num-1 where bno = \'' + bno + '\' and sno = \'' + sno + '\''
                    self.opendatabse()
                    today = datetime.date.today()
                    self.sql = 'insert into rent values(\'' + self.no + '\',\'' + bno + '\',' + term_z + ',\'' + str(today) + '\')'
                    self.opendatabse()
                    tk.messagebox.showinfo(message='租书成功')

        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        window_top.title('租书')
        name = tk.StringVar()
        term = tk.StringVar()

        tk.Label(window_top, text='书名：').place(x=60, y=40)
        tk.Entry(window_top, textvariable=name).place(x=120, y=40)
        tk.Label(window_top, text='租期：').place(x=60, y=80)
        tk.Entry(window_top, textvariable=term).place(x=120, y=80)
        # 提交
        bt = tk.Button(window_top, text='提交', command=save_d)
        bt.place(x=140, y=160)

    # 学生模块
    def student(self):
        self.title = '学生服务程序'
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry('900x600')

        # 设置画布放置图片
        canvas = tk.Canvas(self.window, height=600, width=1000)
        imagefile = tk.PhotoImage(file=self.picture)
        # 刚开始指定位置，nw表示从左上角开始
        image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
        canvas.pack(side='top')

        bt1 = tk.Button(self.window, text='查看基本信息', command=self.showdata)
        bt1.place(x=330, y=100)
        bt2 = tk.Button(self.window, text='更改基本信息', command=self.updatedata)
        bt2.place(x=330, y=150)
        bt3 = tk.Button(self.window, text='租书架', command=self.Rackrent)
        bt3.place(x=330, y=200)
        bt4 = tk.Button(self.window, text='买书', command=self.buy_book)
        bt4.place(x=330, y=250)
        bt5 = tk.Button(self.window, text='放书', command=self.put_book)
        bt5.place(x=330, y=300)
        bt6 = tk.Button(self.window, text='租书', command=self.rent_book)
        bt6.place(x=330, y=350)
        bt7 = tk.Button(self.window, text='退出', command=self.usr_sign_quit)
        bt7.place(x=330, y=400)

        self.window.mainloop()

    def te_show(self):
        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        self.sql = 'select * from teacher where tname = \'' + self.user.get() + '\''
        data = self.opendatabse()
        window_top.title('基本信息')
        factory = ['工号：', '名字：', '手机号：', '性别：']
        list = tk.Listbox(window_top)
        for i in range(4):
            list.insert(0, factory[3 - i] + data[0][3 - i])

        list.pack()

    def te_update(self):
        def save_d():
            sex_z = sex.get()
            tele_z = tele.get()
            self.sql = 'update teacher set Ttele = \'' + tele_z + '\',Tsex = \'' + sex_z + '\' where Tname = \'' + self.user.get() + '\''
            self.opendatabse()
            tk.messagebox.showinfo('恭喜', '修改成功！')

        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x250')
        window_top.title('信息更改选择')

        sex = tk.StringVar()
        tele = tk.StringVar()

        # 设置性别和手机号码
        tk.Label(window_top, text='性别：').place(x=60, y=80)
        tk.Label(window_top, text='电话：').place(x=60, y=120)
        # 输入框
        tk.Entry(window_top, textvariable=sex).place(x=120, y=80)
        tk.Entry(window_top, textvariable=tele).place(x=120, y=120)
        # 提交
        bt = tk.Button(window_top, text='提交', command=save_d)
        bt.place(x=140, y=160)

    # 增加书架
    def add_rack(self):
        self.sql = 'select max(brno) from bookrack'
        data = self.opendatabse()
        max_brno = data[0][0]
        max_brno += 1
        self.sql = 'insert into bookrack values(' + str(max_brno) + ',\'' + self.no + '\')'
        self.opendatabse()
        tk.messagebox.showinfo(title='恭喜！', message='增加成功，新书架号为' + str(max_brno))

    # 查看库存
    def show_res(self):
        window_top = tk.Toplevel(self.window)
        window_top.geometry('350x500')
        window_top.title('库存信息')
        self.sql = 'select book.Bno,Bname,num from repertory,book where repertory.bno = book.bno order by bno desc'
        data = self.opendatabse()
        list = tk.Listbox(window_top)
        for i in range(len(data)):
            list.insert(0, data[i])

        list.pack()

    # 老师模块
    def teacher(self):
        self.title = '教师服务程序'
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry('900x600')

        # 设置画布放置图片
        canvas = tk.Canvas(self.window, height=600, width=1000)
        imagefile = tk.PhotoImage(file=self.picture)
        # 刚开始指定位置，nw表示从左上角开始
        image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
        canvas.pack(side='top')

        bt1 = tk.Button(self.window, text='查看基本信息', command=self.te_show)
        bt1.place(x=330, y=100)
        bt2 = tk.Button(self.window, text='更改基本信息', command=self.te_update)
        bt2.place(x=330, y=150)
        bt3 = tk.Button(self.window, text='增加书架', command=self.add_rack)
        bt3.place(x=330, y=200)
        bt4 = tk.Button(self.window, text='查看库存', command=self.show_res)
        bt4.place(x=330, y=250)
        bt5 = tk.Button(self.window, text='退出', command=self.usr_sign_quit)
        bt5.place(x=330, y=350)
        self.window.mainloop()

    # 用户登录程序
    def usr_log_in(self):
        username = self.user.get()
        userpwd = self.pwd.get()

        flag = 0

        for value in self.data:
            if value[0] == username and value[1] == userpwd:
                if value[2] == 'stu':
                    self.sql = 'select sno from student where sname = \'' + self.user.get() + '\''
                    data = self.opendatabse()
                    if len(data) == 0:
                        def save_d():
                            sno_z = sno.get()
                            sex_z = sex.get()
                            tele_z = tele.get()
                            self.sql = 'insert into Student values(\'' + sno_z + '\',\'' + \
                                       self.user.get() + '\',\'' + tele_z + '\',\'' + sex_z + '\')'
                            self.opendatabse()
                            tk.messagebox.showinfo('恭喜', '修改成功！')

                        window_top = tk.Toplevel(self.window)
                        window_top.geometry('350x250')
                        window_top.title('完善信息')
                        sno = tk.StringVar()
                        sex = tk.StringVar()
                        tele = tk.StringVar()

                        # 设置性别和手机号码
                        tk.Label(window_top, text='学号：').place(x=60, y=40)
                        tk.Label(window_top, text='性别：').place(x=60, y=80)
                        tk.Label(window_top, text='电话：').place(x=60, y=120)
                        # 输入框
                        tk.Entry(window_top, textvariable=sno).place(x=120, y=40)
                        tk.Entry(window_top, textvariable=sex).place(x=120, y=80)
                        tk.Entry(window_top, textvariable=tele).place(x=120, y=120)
                        # 提交
                        bt = tk.Button(window_top, text='提交', command=save_d)
                        bt.place(x=140, y=160)
                    else:
                        self.no = data[0][0]
                        print(self.no)
                        self.student()
                else:
                    self.sql = 'select tno from teacher where tname = \'' + self.user.get() + '\''
                    data = self.opendatabse()
                    if len(data) == 0:
                        def save_d():
                            tno_z = tno.get()
                            sex_z = sex.get()
                            tele_z = tele.get()
                            self.sql = 'insert into teacher values(\'' + tno_z + '\',\'' + \
                                       self.user.get() + '\',\'' + tele_z + '\',\'' + sex_z + '\')'
                            self.opendatabse()
                            tk.messagebox.showinfo('恭喜', '修改成功！')

                        window_top = tk.Toplevel(self.window)
                        window_top.geometry('350x250')
                        window_top.title('完善信息')
                        tno = tk.StringVar()
                        sex = tk.StringVar()
                        tele = tk.StringVar()

                        # 设置性别和手机号码
                        tk.Label(window_top, text='工号：').place(x=60, y=40)
                        tk.Label(window_top, text='性别：').place(x=60, y=80)
                        tk.Label(window_top, text='电话：').place(x=60, y=120)
                        # 输入框
                        tk.Entry(window_top, textvariable=tno).place(x=120, y=40)
                        tk.Entry(window_top, textvariable=sex).place(x=120, y=80)
                        tk.Entry(window_top, textvariable=tele).place(x=120, y=120)
                        # 提交
                        bt = tk.Button(window_top, text='提交', command=save_d)
                        bt.place(x=140, y=160)
                    else:
                        self.no = data[0][0]
                        print(self.no)
                        self.teacher()
                flag = 1
                break
            elif value[0] == username and value[1] != userpwd:
                tk.messagebox.showerror(message='密码错误！')
                flag = -1

        if flag == 0:
            is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
            if is_signup:
                self.usr_sign_up()

    # 登录页面初始化
    def login_init(self):
        self.window.title(self.title)
        self.window.geometry('900x600')

        # 设置画布放置图片
        canvas = tk.Canvas(self.window, height=600, width=1000)
        imagefile = tk.PhotoImage(file=self.picture)
        # 刚开始指定位置，nw表示从左上角开始
        image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
        canvas.pack(side='top')

        # 设置标签，用户名和密码选项
        tk.Label(self.window, text='用户名：').place(x=250, y=250)
        tk.Label(self.window, text='密码：').place(x=250, y=330)
        # 输入框
        tk.Entry(self.window, textvariable=self.user).place(x=330, y=250)
        tk.Entry(self.window, textvariable=self.pwd, show='*').place(x=330, y=330)

        # 登录 注册按钮
        bt_login = tk.Button(self.window, text='登录', command=self.usr_log_in)
        bt_login.place(x=260, y=380)
        bt_logup = tk.Button(self.window, text='注册', command=self.usr_sign_up)
        bt_logup.place(x=330, y=380)
        bt_logquit = tk.Button(self.window, text='退出', command=self.usr_sign_quit)
        bt_logquit.place(x=400, y=380)

        self.window.mainloop()

    # 总程序入口，以登录为开始
    def login(self):
        self.sql = "select * from pwd"
        self.data = self.opendatabse()
        self.login_init()




if __name__ == '__main__':
    lib = library()
    lib.login()