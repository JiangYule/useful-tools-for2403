import random as r
from email.policy import default
# from msilib import type_binary
from random import random
from turtledemo.penrose import start
from tkinter import messagebox
import customtkinter

root = customtkinter.CTk()
root.geometry('500x300')
root.title("随机数")
root.resizable(False, False)
customtkinter.CTkLabel(master=root, text="起始数字", font=("微软雅黑", 15)).place(relx=0.35, rely=0.3, anchor="center")
customtkinter.CTkLabel(master=root, text="终止数字", font=("微软雅黑", 15)).place(relx=0.65, rely=0.3, anchor="center")
text_con = customtkinter.StringVar()
text = customtkinter.CTkLabel(master=root, textvariable=text_con, font=("微软雅黑", 40)).place(relx=0.5, rely=0.15, anchor='center')
start_con = customtkinter.StringVar()
end_con = customtkinter.StringVar()
start = customtkinter.CTkEntry(master=root, textvariable=start_con).place(relx=0.35, rely=0.45, anchor='center')
end = customtkinter.CTkEntry(master=root, textvariable=end_con).place(relx=0.65, rely=0.45, anchor='center')
start_con.set("1")
end_con.set("37")
def update():
    s = start_con.get()
    e = end_con.get()
    try:
        text_con.set("随机数:" + str(r.randint(int(s), int(e))))
    except ValueError:
        messagebox.showerror(title="错误", message="请输入或填充")

def auto_fill():
    start_con.set("1")
    end_con.set("37")
refresh = customtkinter.CTkButton(master=root, text="生成", command=update,font=("微软雅黑",20)).place(relx=0.5, rely=0.6, anchor='center')
refill = customtkinter.CTkButton(master=root, text="填充", command=auto_fill,font=("微软雅黑",20)).place(relx=0.5, rely=0.75, anchor='center')
root.mainloop()
