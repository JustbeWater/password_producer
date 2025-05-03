# 请运行该文件

import tkinter as tk
from tkinter import filedialog
from password import *
from tkinter import END

# 创建一个类，继承自listbox，写一个同时执行插入和查看最后一行的操作
class Log_Listbox(tk.Listbox):
    def insert_and_see(self, message):
        self.insert(END, message)
        self.see(END)

#  UI 类
class GUI:
    __abc = 'abcdefghijklmnopqrstuvwxyz'
    __ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __dig = '0123456789'
    __spc = '~`!@#$%^&*()_+-={[]}|\\:;",<>.?/\''
    __mine = ''
    __a = None
    __b = None
    __c = None
    __d = None
    CharSet = ''
    mode = 1
    pw_length = []
    mask = ''
    folder = ''
    filename = ''

    def __start(self, log_listbox:Log_Listbox):
        # 每次设置字符集之前都要置空，否则累加
        self.CharSet = ''
        if self.__a.get():
            self.CharSet += self.__dig
        if self.__b.get():
            self.CharSet += self.__abc
        if self.__c.get():
            self.CharSet += self.__ABC
        if self.__d.get():
            self.CharSet += self.__spc
        if self.__mine.get():
            self.CharSet += self.__mine.get()
        # 当没有选择时，默认选择数字装入字符集
        if self.CharSet == '':
            self.CharSet = self.__dig
        
        # print(self.CharSet)
        pwb_path = f"{self.folder.get()}/{self.filename.get()}"
        # print(pwb_path)
        lengths = []
        for i in range(16):
            length = self.pw_length[i].get()
            if length:
                lengths.append(length)

        start_in_back(self.mode.get(), log_listbox, lengths, self.mask.get(), self.CharSet, pwb_path)


    def __open_folder(self):
        folder = filedialog.askdirectory(title='选择文件夹')
        if folder:
            self.folder.set(folder)

    def __init__(self):
        window = tk.Tk()
        w, h = window.maxsize()
        # 固定窗口大小以及动态调整窗口位置处于桌面正中间
        window.geometry(f'512x432+{(w-512)//2}+{(h-432)//2}')
        window.title('密码本生成器')

        tk.Label(master=window, text='字符集：').place(x=10, y=10)

        self.__a = tk.BooleanVar(value=1)   # 设置默认字符集
        self.__b = tk.BooleanVar()
        self.__c = tk.BooleanVar()
        self.__d = tk.BooleanVar()

        tk.Checkbutton(master=window, text='数字', onvalue=True, offvalue=False, variable=self.__a).place(x=60, y=10)
        tk.Checkbutton(master=window, text='小写字母', onvalue=True, offvalue=False, variable=self.__b).place(x=115, y=10)
        tk.Checkbutton(master=window, text='大写字母', onvalue=True, offvalue=False, variable=self.__c).place(x=190, y=10)
        tk.Checkbutton(master=window, text='特殊字符', onvalue=True, offvalue=False, variable=self.__d).place(x=270, y=10)
        
        self.__mine = tk.StringVar()
        tk.Label(master=window, text='自定义字符集：').place(x=10, y=50)
        tk.Entry(master=window, textvariable=self.__mine, width=40).place(x=100, y=50)


        tk.Label(master=window, text='模式：').place(x=10, y=90)

        self.mode = tk.IntVar(value=1)  # 默认为密码长度模式
        tk.Radiobutton(master=window, text='密码长度模式', value=1, variable=self.mode).place(x=50, y=90)
        tk.Radiobutton(master=window, text='掩码模式', value=0, variable=self.mode).place(x=150, y=90)


        tk.Label(master=window, text='密码长度：').place(x=10, y=120)

        
        for _ in range(16):
            self.pw_length.append(tk.IntVar())
        for i in range(16):
            if i < 8:
                x = 70 + i * 40
                y = 120
            else:
                 x = 70 + i % 8 * 40
                 y = 150
            tk.Checkbutton(master=window, text=i+1, onvalue=i+1, offvalue=0, variable=self.pw_length[i]).place(x=x, y=y)

        tk.Label(master=window, text='掩码：').place(x=10, y=180)
        self.mask = tk.StringVar()
        tk.Entry(master=window, textvariable=self.mask, width=30).place(x=50, y=180)

        tk.Label(master=window, text='1?34?6 意思是只有 2 和 5 位发生改变', font=('', 8), fg='red').place(x=50, y=210)

        # 选择文件夹按钮在输入框后面，需要给输入框设置一个变量，后面再把选择的路径赋予这个变量，就完成了插入输入框的操作
        self.folder = tk.StringVar(value='.')
        tk.Label(master=window, text='密码本路径：').place(x=10, y=240)
        tk.Entry(master=window, textvariable=self.folder).place(x=90, y=240)
        tk.Button(master=window, text='选择', command=self.__open_folder, font=('', 9)).place(x=240, y=240)

        self.filename = tk.StringVar(value='password.txt')
        tk.Label(master=window, text='文件名：').place(x=10, y=270)
        tk.Entry(master=window, textvariable=self.filename).place(x=60, y=270)

        # 创建一个日志框
        log_listbox = Log_Listbox(master=window, width=50, height=6)
        log_listbox.place(x=10, y=300)

        # 使用 lambda 把函数传入参数，函数不会立即执行（类似延迟扩展）
        tk.Button(master=window, text='开始', width=10, command=lambda:self.__start(log_listbox)).place(x=410, y=390)

        window.mainloop()



if __name__ == "__main__":
    GUI()