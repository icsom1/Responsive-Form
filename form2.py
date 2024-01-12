import tkinter
from tkinter import messagebox 

windows = tkinter.Tk()
windows.title('Login Form')
windows.geometry('340x440')
windows.configure(bg='#333333')

def login():
    username = 'icsom1'
    password = '0000'
    if username_entry.get()== username and password_entry.get()== password:
        messagebox.showinfo(title= 'Login Success', message = 'you successfully logged in.')
    else:
        messagebox.showerror(title= 'Login Error', message = 'invalid logged in.')
frame = tkinter.Frame(bg='#333333')


# creating widgets
login_label = tkinter.Label(frame, text='Sign in', bg='#333333', fg='red', font=('Arial', 30))
username_label = tkinter.Label(frame, text='Username', bg='#333333',fg='white', font=('Arial', 16))
username_entry = tkinter.Entry(frame, font=('Arial', 10))
password_entry = tkinter.Entry(frame, show='*', font=('Arial', 10))
password_label = tkinter.Label(frame, text='Password', bg='#333333', fg='white', font=('Arial', 16))
login_button = tkinter.Button(frame, text='Login', bg='#ff3399', fg='white',command=login) 


# placing widgets

login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=20) #news means north east west south
username_label.grid(row=1, column=0, pady=20) #pady is used to space the two labels
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=20)




frame.pack() 

windows.mainloop()