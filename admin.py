from tkinter import *
import mysql.connector
from datetime import *
import time
import pipes
import subprocess
from tkinter import  messagebox
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="lifechoices",
  password="@Lifechoices1234",
  database="lifechoicesonline"
)

mycursor = mydb.cursor()

# Create database if it does not exist
cursor = mydb.cursor()
cursor.execute("create database if not exists lifechoicesonline")
cursor.execute("use lifechoicesonline")

# Creates the tables if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS time_in(full_name varchar(60) Default null, date date, logged_in time)")
mydb.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS time_out(full_name varchar(60) Default null, date date, logged_out time)")
mydb.commit()

# START OF THE TKINTER ADMIN GUI
admin = Tk()
admin.geometry("880x550")
admin.title("Admin")

# WINDOW THAT OPENS WHEN "a" or "A" is pressed

canvas = Canvas(admin, width =900,bg="black")
canvas.place(y=450)
img = PhotoImage(file="index.png")
canvas.create_image(2,2, anchor=NW, image=img)

# Deleting records
def delete():
    pass
# Adding users to the admin and to the users/students
def add():
    selction = var.get()
    if selction == 1:
        comm3 = "INSERT INTO admin (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(nameReg.get()), str(usrName.get()), psswrd.get()
        mycursor.execute(comm3, user_info1)
        mydb.commit()
        messagebox.showinfo("Confirmation", "New admin successfully created")

    elif selction == 2:
        comm3 = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(nameReg.get()), str(usrName.get()), psswrd.get()
        mycursor.execute(comm3, user_info1)
        mydb.commit()
        messagebox.showinfo("Confirmation", "New user successfully created")

# Count how many admin users is logged in
# AND THE AMOUNT OF USERS
def count():
    selection = var.get()
    if selection == 1:
        cursor = mydb.cursor()
        query = "SELECT count(*) FROM admin"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of admin users logged in\n',(myresult[-1][-1]))
        messagebox.showinfo("Attention", total)

    elif selection == 2:
        cursor = mydb.cursor()
        query = "SELECT count(*) FROM users"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of users logged in\n', (myresult[-1][-1]))
        messagebox.showinfo("Attention", total)

# Granting access and tells you when a admin is signed in
def grant():
    selection = var.get()
    if selection == 1:
        u = usrName.get()
        priv_com = "GRANT ALL PRIVILEGES ON books.authors  TO '%s'@'localhost'" % (u)
        mycursor.execute(priv_com)
        messagebox.showinfo("Message", "Privileges Granted")
    elif selection >=2:
        messagebox.showerror("Attention", "Admin users online")

# THIS WILL CLEAR THE LISTBOX AND THE ENTRY FIELDS
def clear_list():
    liName.delete(0,END)
    liD.delete(0,END)
    liT.delete(0,END)
    liP.delete(0,END)
    Liu.delete(0, END)
    Lid.delete(0,END)
    LiTi.delete(0, END)
    LiT0.delete(0,END)
    nameReg.delete(0,END)
    usrName.delete(0,END)
    psswrd.delete(0,END)


# Display information
def display():
    selction = var.get()
    if selction == 1:
        cursor.execute("SELECT id FROM admin")

        id = cursor.fetchall()

        for x in id:
            liName.insert(END, x)

        liName.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM admin")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM admin")

        uName = cursor.fetchall()
        for x in uName:
            liT.insert(END, x)
        liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM admin")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
        liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM time_in")

        tUn = cursor.fetchall()
        for x in tUn:
            Liu.insert(END, x)
        Liu.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_in")

        d = cursor.fetchall()
        for x in d:
            Lid.insert(END, x)
        Lid.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_in FROM time_in")

        timeIn = cursor.fetchall()
        for x in timeIn:
            LiTi.insert(END, x)
        LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_out FROM time_out")

        timeout = cursor.fetchall()
        for x in timeout:
            LiT0.insert(END, x)
        LiT0.insert(END, str(cursor.rowcount) + " rows")

    elif selction == 2:
        cursor.execute("SELECT id FROM users")

        id = cursor.fetchall()

        for x in id:
            liName.insert(END, x)

        liName.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM users")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM users")

        uName = cursor.fetchall()
        for x in uName:
            liT.insert(END, x)
        liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
            liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM time_in")

        tUn = cursor.fetchall()
        for x in tUn:
            Liu.insert(END, x)
        Liu.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_in")

        d = cursor.fetchall()
        for x in d:
            Lid.insert(END, x)
        Lid.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_in FROM time_in")

        timeIn = cursor.fetchall()
        for x in timeIn:
            LiTi.insert(END, x)
        LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_out FROM time_out")

        timeIn = cursor.fetchall()
        for x in timeIn:
            LiT0.insert(END, x)
        LiT0.insert(END, str(cursor.rowcount) + " rows")

def dump():
    username = 'lifechoices'
    password = '@Lifechoicesonlin1234'
    database = 'lifechoicesonline'

    with open('backup.sql','w') as output:
        c = subprocess.Popen(['mysqldump', '-u',username,'-p%s'%password,database],
                         stdout=output, shell=True)

# Quit
def quit():
    admin.destroy()

# button to add a user
# button that will add a user
add_user = Button(admin,text="Add User",command=add)
add_user.place(x=10,y=5)
add_user.config(width=9)

# Button that will count the users
count_user = Button(admin,text="Count users",command=count)
count_user.place(x=10,y=35)
count_user.config(width=9)

# update button
update_btn = Button(admin,text="Grant",command=grant)
update_btn.place(x=10,y=65)
update_btn.config(width=9)

# display button
display_btn = Button(admin,text="Display",command=display)
display_btn.place(x=10,y=95)
display_btn.config(width=9)

# Delete button
delete_btn= Button(admin,text="Delete",command=delete)
delete_btn.place(x=10,y=185)
delete_btn.config(width=9)

# Clear button
clear_btn = Button(admin,text="Clear",command=clear_list)
clear_btn.place(x=10,y=125)
clear_btn.config(width=9)

# quit button
quit_btn = Button(admin,text="Quit", command= quit)
quit_btn.place(x=10,y=155)
quit_btn.config(width=9)

# Radio buttons that allows admin to have  look at fields
# Users and admin
var = IntVar()
admin_radio = Radiobutton(admin, text="ADMIN", variable=var, value=1, fg="white", bg="black")
admin_radio.place(x=10, y=410)

user_radio = Radiobutton(admin, text="USERS", variable=var, value=2, fg="white", bg="green")
user_radio.place(x=100, y=410)

# LABELS OF FIELDS
# ENTRIES OF FIELDS TO ADD
nameReg_lbl = Label(admin,text="Fullname: ")
nameReg_lbl.place(x=10,y=250)

usrName_lbl = Label(admin,text="Username: ")
usrName_lbl.place(x=10,y=300)

nameReg = Entry(admin)
nameReg.place(x=150,y=250)

psswrd_lbl = Label(admin,text="Password: ")
psswrd_lbl.place(x=10,y=350)

usrName = Entry(admin)
usrName.place(x=150,y=300)

psswrd = Entry(admin)
psswrd.place(x=150,y=350)

###############################
# PLACEMENT OF LISTBOX
# THE ABOVE
# LISTBOX
liName = Listbox(admin, width=20)
liName.place(x=140, y=5)

liD = Listbox(admin, width=20)
liD.place(x=250, y=5)

liT = Listbox(admin, width=20)
liT.place(x=370, y=5)

liP = Listbox(admin, width=20)
liP.place(x=500, y=5)

# SECOND SET OF LISTBOXES
# THIS INDECATE THE LOG IN AND LOG OUT OF USERS
Liu = Listbox(admin, width=20)
Liu.place(x=370, y=220)

Lid = Listbox(admin, width=20)
Lid.place(x=500, y=220)

LiTi = Listbox(admin, width=20)
LiTi.place(x=600, y=220)

LiT0 = Listbox(admin, width=20)
LiT0.place(x=690, y=220)

#############################################################
# FIRST ROW INFORMATION LABLES
liLb = Label(admin, text="ID:", fg="white", bg="black")
liLb.place(x=140, y=190)

li2Lb = Label(admin, text="Fullname:", fg="white", bg="black")
li2Lb.place(x=250, y=190)

liTL = Label(admin, text="Username", fg="white", bg="black")
liTL.place(x=370, y=190)

liLp = Label(admin, text="Password:",fg="white", bg="black")
liLp.place(x=500, y=190)

# SECOND ROW OF LABELS
# THIS INDECATE THE LOG IN AND LOG OUT OF USERS
lbU = Label(admin, text="Username:",fg="white", bg="green")
lbU.place(x=370, y=410)

lbD = Label(admin, text="Date:", fg="white", bg="black")
lbD.place(x=500, y=410)

LiTiL = Label(admin, text="Login Time:", fg="white", bg="green")
LiTiL.place(x=600, y=410)

LiOl = Label(admin, text="Logout Time:", fg="white", bg="black")
LiOl.place(x=690, y=410)

###############################################################

admin.mainloop()
