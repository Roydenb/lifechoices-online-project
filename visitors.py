from tkinter import *
import mysql.connector
from tkinter import  messagebox
mydb = mysql.connector.connect(
  host="localhost",
  user="lifechoices",
  password="@Lifechoices1234",
  database="lifechoicesonline"
)

mycursor = mydb.cursor()

def add():
    selction = var.get()
    if selction == 1:
        comm3 = "INSERT INTO visitors (full_name, mobile_number) VALUES (%s, %s, %s)"
        user_info1 =  str(v_fullname_ent.get()), mobile_ent.get()
        mycursor.execute(comm3, user_info1)
        mydb.commit()
        messagebox.showinfo("Confirmation", "New admin successfully created")


def clear_v():
    v_fullname_ent.delete(0,END)
    mobile_ent.delete(0,END)

def quit_v():
    window.withdraw()

# WINDOW
window = Tk()
window.geometry("550x550")
window.title("Visitor")

# LABELS
welcome_lbl= Label(window,text="Welcome dear visitor")
welcome_lbl.place(x=100, y=50)
welcome_lbl.config(font=("Courier", 20))

sub_message = Label(window,text="We hope you will enjoy your time with us here \n at")
sub_message.place(x=30,y=100)
sub_message.config(font=("Courier", 12))

last_message= Label(window,text="LIFE CHOICES ACADEMY")
last_message.place(x=150,y= 150 )
last_message.config(font=("Courier", 16))

vis_fullname_lbl = Label(window,text= "Please enter your full name\n with spacing: ")
vis_fullname_lbl.place(x=180, y= 200)

mobile_lbl = Label(window,text="Please enter your mobile number: ")
mobile_lbl.place(x=180,y=300)

# ENTRIES
v_fullname_ent = Entry(window,command=add)
v_fullname_ent.place(x=180,y=250)

mobile_ent = Entry(window)
mobile_ent.place(x=180,y=330)

# BUTTONS
visitor_login_btn = Button(window,text="Submit",width=40,bg= "green")
visitor_login_btn.place(x=80,y=400)

# quit button
quit_btn_v = Button(window,text="Quit", command= quit_v)
quit_btn_v.place(x=200,y=450)
quit_btn_v.config(width=9)

# clear button
clear_v_btn = Button(window,text="Clear", command= clear_v)
clear_v_btn.place(x=200,y=500)
clear_v_btn.config(width=9)


window.mainloop()
