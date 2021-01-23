# Register System with Python GUI and MySQL
import mysql.connector
from tkinter import messagebox as mb
from tkinter import *
from datetime import *
import os

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    # auth_plugin="mysql_native_password"
)

cursor = db.cursor()


admin_login = Tk()
admin_login.resizable(False, False)
admin_login.title("Admin")


#Welcome intro
canvas = Canvas(admin_login, width = 350, height = 90,bg="black")
canvas.pack()
img = PhotoImage(file="index.png")
canvas.create_image(5,5, anchor=NW, image=img)

def login():
    usr = usrEnt.get()
    p = adUps.get()
    sql = "select * from admin where username=%s and password=%s"
    cursor.execute(sql, [(usr), (p)])
    datab = cursor.fetchall()

    if datab:
        mb.showinfo("Login", "login successful")
        admin_login.destroy()
        import admin.py
    else:
        mb.showerror("Unsuccessful", "Login failed")

def back():
    admin_login.destroy()
    import login.py



bck_Btn = Button(admin_login, text="Back", command=back)
bck_Btn.place(x=320, y=180)
privBtn = Button(admin_login, text="Login", command=login)

usrAdLb = Label(admin_login, text="User/Admin Name:", fg="white", bg="black")
usrEnt = Entry(admin_login)
usrAdp = Label(admin_login, text="Password", fg="white", bg="black")
adUps = Entry(admin_login)
usrAdLb.place(x=20, y=100)
usrEnt.place(x=150, y=100)
usrAdp.place(x=20, y=140)
adUps.place(x=150, y=140)
privBtn.place(x=20, y=180)




#Center gui on screen
window_height = 240
window_width = 400

screen_width = admin_login.winfo_screenwidth()
screen_height = admin_login.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

admin_login.geometry("520x300")
admin_login.geometry("400x300")
admin_login.configure(bg="black")

admin_login.mainloop()


