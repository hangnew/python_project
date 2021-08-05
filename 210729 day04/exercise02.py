from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# mac button text color


def login():
    id2 = id_entry.get()
    print('입력한 id: ' + id2)
    pw2 = pw_entry.get()
    print('입력한 pw: ' + pw2)
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인 성공', '축하합니다')
    else:
        messagebox.showinfo('로그인 실패', '다시 해보세요')


w = Tk()
w.geometry("400x300")
id = Label(w, text='ID 입력')
id_entry = Entry(w)
pw = Label(w, text='pw 입력')
pw_entry = Entry(w)
id.pack()
id_entry.pack()
pw.pack()
pw_entry.pack()

b = ttk.Button(w, text='로그인 처리',
               command=login)
b.pack()

w.mainloop()
