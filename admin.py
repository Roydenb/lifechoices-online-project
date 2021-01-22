from tkinter import *
import mysql.connector
import mysql.connector

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

# Adding a user
def add():
     sql = "INSERT INTO users (full_name, username, password ) VALUES (%s, %s, %s)"
     val = [
        ('Shane kolkoto', 'ShaneK', '2345')
        ]

     mycursor.executemany(sql, val)

     mydb.commit()

     print(mycursor.rowcount, "was inserted.")
     return

# Quit
def quit():
    admin.destroy()

# button to add a user
# button that will add a user
add_user = Button(admin,text="Add User")
add_user.place(x=10,y=5)
add_user.config(width=9)

# Delete button
# button that will delete a user
del_user = Button(admin,text="Delete User")
del_user.place(x=10,y=35)
del_user.config(width=9)

# update button
update_btn = Button(admin,text="Update")
update_btn.place(x=10,y=65)
update_btn.config(width=9)

# display button
display_btn = Button(admin,text="Display")
display_btn.place(x=10,y=95)
display_btn.config(width=9)

# quit button
quit_btn = Button(admin,text="Quit", command= quit)
quit_btn.place(x=10,y=150)
quit_btn.config(width=9)

 # List that display information
frame_info = LabelFrame(admin,text="Information",
                           font=("FreeMono",20,"bold")
                           ,fg="green",bd=5,relief=GROOVE)
frame_info.place(x=120,y=0,width=400,height=210)

# Scrollbar for the listbox
scroll_bar= Scrollbar(frame_info,orient=VERTICAL)

# Adding the info_list to the listbox
list = Listbox(frame_info,yscrollcommand=scroll_bar.set,selectbackground="gold",
                      selectmode=SINGLE,font=("times new roman",15,"bold")
                      ,bg="white",fg="red",bd=5,relief=GROOVE)

# Combines the scrollbar and the listbox
scroll_bar.pack(side=RIGHT,fill=Y)
scroll_bar.config(command=list.yview)
list.pack(fill=BOTH)

stud_fullname_lbl = Label(admin,text="Student Fullname: ")
stud_fullname_lbl.place(x=10,y=250)

stud_fullname_ent = Entry(admin)
stud_fullname_ent.place(x=150,y=250)

stud_username_lbl = Label(admin,text="Student Username: ")
stud_username_lbl.place(x=10,y=300)

stud_username_ent = Entry(admin)
stud_username_ent.place(x=150,y=300)

stud_password = Label(admin,text="Password: ")
stud_password.place(x=10,y=350)

stud_password_ent = Entry(admin)
stud_password_ent.place(x=150,y=350)

admin.mainloop()
