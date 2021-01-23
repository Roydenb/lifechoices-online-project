from tkinter import *
import mysql.connector
import mysql.connector
from tkinter import  messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="lifechoices",
  password="@Lifechoices1234",
  database="lifechoicesonline"
)

mycursor = mydb.cursor()

admin = Tk()
admin.geometry("530x500")
admin.title("Admin")

# WINDOW THAT OPENS WHEN "a" or "A" is pressed

canvas = Canvas(admin, width = 520, height = 90,bg="black")
canvas.place(x=5,y=400)
img = PhotoImage(file="index.png")
canvas.create_image(5,5, anchor=NW, image=img)

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


def display():
    selction = var.get()
    if selction == 1:
        mycursor.execute("SELECT id FROM admin")

        id = mycursor.fetchall()

        for x in id:
            liName.insert(END, x)

        liName.insert(END, str(mycursor.rowcount) + " rows")

        mycursor.execute("SELECT full_name FROM admin")

        name = mycursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(mycursor.rowcount) + " rows")

        mycursor.execute("SELECT username FROM admin")

        uName = mycursor.fetchall()

        for x in uName:
            liT.insert(END, x)
        liT.insert(END, str(mycursor.rowcount) + " rows")

        mycursor.execute("SELECT password FROM admin")

    elif selction == 2:
        mycursor.execute("SELECT id FROM users")

        id = mycursor.fetchall()

        for x in id:
            liName.insert(END, x)

        liName.insert(END, str(mycursor.rowcount) + " rows")

        mycursor.execute("SELECT full_name FROM users")

        name = mycursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(mycursor.rowcount) + " rows")

        mycursor.execute("SELECT username FROM users")

        uName = mycursor.fetchall()
        for x in uName:
            liT.insert(END, x)
        liT.insert(END, str(mycursor.rowcount) + " rows")

        mycursor.execute("SELECT password FROM users")

def dump():
    pass

# Quit
def quit():
    admin.destroy()

# button to add a user
# button that will add a user
add_user = Button(admin,text="Add User",command=add)
add_user.place(x=10,y=5)
add_user.config(width=9)

# Delete button
# button that will delete a user
del_user = Button(admin,text="Count users",command=count)
del_user.place(x=10,y=35)
del_user.config(width=9)

# update button
update_btn = Button(admin,text="Grant",command=grant)
update_btn.place(x=10,y=65)
update_btn.config(width=9)

# display button
display_btn = Button(admin,text="Display",command=display)
display_btn.place(x=10,y=95)
display_btn.config(width=9)

# quit button
quit_btn = Button(admin,text="Quit", command= quit)
quit_btn.place(x=10,y=150)
quit_btn.config(width=9)

# Radio buttons that allows addmin to have  look at fields
# Users and admin
var = IntVar()
admin_radio = Radiobutton(admin, text="admin", variable=var, value=1, fg="white", bg="black")
admin_radio.place(x=10, y=220)

user_radio = Radiobutton(admin, text="Users", variable=var, value=2, fg="white", bg="black")
user_radio.place(x=100, y=220)

# LABELS
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

# LISTBOX
liName = Listbox(admin, width=20)

liD = Listbox(admin, width=20)

liT = Listbox(admin, width=20)


# PLACEMENT OF LISTBOX
liName.place(x=130, y=5)

liD.place(x=200, y=5)

liT.place(x=350, y=5)








admin.mainloop()
