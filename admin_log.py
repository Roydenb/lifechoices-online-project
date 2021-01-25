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
)

cursor = db.cursor()

# CREATES A ADMIN TABLE IF ONE DOESN'T EXIST
cursor.execute(
    "CREATE TABLE IF NOT EXISTS admin(id int(11) Not null primary key AUTO_INCREMENT, full_name varchar(60) Default null, "
    "username varchar(50) Default null ,password varchar(20) Default null)")
db.commit()

# INSERT DEFAULT INFO IN THE ADMIN
cursor.execute("INSERT INTO admin(full_name, username, password) \
   SELECT * FROM (SELECT 'Admin', 'lifechoices', '@Lifechoices12!') as temp \
   WHERE NOT EXISTS \
   (SELECT 'lifechoices' FROM admin WHERE username = 'lifechoices') LIMIT 1")

# # CREATE TABLE FOR USERS TO BE ADDED
# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS users(id int(11) Not null primary key AUTO_INCREMENT, full_name varchar(60) Default null, "
#     "username varchar(50) Default null ,password varchar(20) Default null)")
# mydb.commit()
#
# # DEFAULT INFO IN THE USERS
# cursor.execute("INSERT INTO users(full_name, username, password) \
#    SELECT * FROM (SELECT 'Roy', 'RoydenB', 'lifechoices') as temp \
#    WHERE NOT EXISTS \
#    (SELECT 'RoydenB' FROM users WHERE username = 'RoydenB') LIMIT 1")
# mydb.commit()


# WINDOW WHEN THE ADMIN HAVE SUCCESFULLY LOGGEDIN
admin_login = Tk()
admin_login.title("Admin Login Window")


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


