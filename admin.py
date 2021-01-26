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
    list_name.delete(0,END)
    list_id.delete(0,END)
    list_usern.delete(0,END)
    list_passw.delete(0,END)
    list_user.delete(0, END)
    list_date.delete(0,END)
    list_login.delete(0, END)
    list_logout.delete(0,END)
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
            list_name.insert(END, x)

        list_name.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM admin")

        name = cursor.fetchall()

        for x in name:
            list_id.insert(END, x)

        list_id.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM admin")

        uName = cursor.fetchall()
        for x in uName:
            list_usern.insert(END, x)
        list_usern.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM admin")

        pas = cursor.fetchall()
        for x in pas:
            list_passw.insert(END, x)
        list_passw.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM time_in")

        tUn = cursor.fetchall()
        for x in tUn:
            list_user.insert(END, x)
        list_user.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_in")

        d = cursor.fetchall()
        for x in d:
            list_date.insert(END, x)
        list_date.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_in FROM time_in")

        timeIn = cursor.fetchall()
        for x in timeIn:
            list_login.insert(END, x)
        list_login.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_out FROM time_out")

        timeout = cursor.fetchall()
        for x in timeout:
            list_logout.insert(END, x)
        list_logout.insert(END, str(cursor.rowcount) + " rows")

    elif selction == 2:
        cursor.execute("SELECT id FROM users")

        id = cursor.fetchall()

        for x in id:
            list_name.insert(END, x)

        list_name.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM users")

        name = cursor.fetchall()

        for x in name:
            list_id.insert(END, x)

        list_id.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM users")

        uName = cursor.fetchall()
        for x in uName:
            list_usern.insert(END, x)
        list_usern.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            list_passw.insert(END, x)
            list_passw.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM time_in")

        tUn = cursor.fetchall()
        for x in tUn:
            list_user.insert(END, x)
        list_user.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_in")

        d = cursor.fetchall()
        for x in d:
            list_date.insert(END, x)
        list_date.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_in FROM time_in")

        timeIn = cursor.fetchall()
        for x in timeIn:
            list_login.insert(END, x)
        list_login.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_out FROM time_out")

        timeIn = cursor.fetchall()
        for x in timeIn:
            list_logout.insert(END, x)
        list_logout.insert(END, str(cursor.rowcount) + " rows")

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
list_name = Listbox(admin, width=20)
list_name.place(x=140, y=5)

list_id = Listbox(admin, width=20)
list_id.place(x=250, y=5)

list_passw = Listbox(admin, width=20)
list_passw.place(x=533, y=5)

list_usern = Listbox(admin, width=20)
list_usern.place(x=370, y=5)

# SECOND SET OF LISTBOXES
# THIS INDECATE THE LOG IN AND LOG OUT OF USERS
list_user = Listbox(admin, width=20)
list_user.place(x=370, y=220)

list_date = Listbox(admin, width=20)
list_date.place(x=500, y=220)

list_login = Listbox(admin, width=20)
list_login.place(x=600, y=220)

list_logout = Listbox(admin, width=20)
list_logout.place(x=690, y=220)

#############################################################
# FIRST ROW INFORMATION LABLES
lbl_ib = Label(admin, text="ID:", fg="white", bg="black")
lbl_ib.place(x=140, y=190)

lbl_fulln = Label(admin, text="Fullname:", fg="white", bg="black")
lbl_fulln.place(x=250, y=190)

lbl_user = Label(admin, text="Username", fg="white", bg="black")
lbl_user.place(x=370, y=190)

lbl_passw = Label(admin, text="Password:",fg="white", bg="black")
lbl_passw.place(x=533, y=190)

# SECOND ROW OF LABELS
# THIS INDECATE THE LOG IN AND LOG OUT OF USERS
lbl_userlog = Label(admin, text="Username:",fg="white", bg="green")
lbl_userlog.place(x=370, y=410)

lbl_date = Label(admin, text="Date:", fg="white", bg="black")
lbl_date.place(x=500, y=410)

lbl_intime = Label(admin, text="Login Time:", fg="white", bg="green")
lbl_intime.place(x=600, y=410)

lbl_outtime = Label(admin, text="Logout Time:", fg="white", bg="black")
lbl_outtime.place(x=690, y=410)

###############################################################

admin.mainloop()
