from tkinter import *
import mysql.connector
from tkinter import  messagebox

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
)

cursor = db.cursor()


# CREATE TABLE FOR USERS TO BE ADDED
cursor.execute(
    "CREATE TABLE IF NOT EXISTS visitors(full_name varchar(60) Default null,"
     "mobile varchar(20) Default null, reason varchar(20) Default null)")
db.commit()

# DEFAULT INFO IN THE USERS
cursor.execute("INSERT INTO visitors (full_name, mobile, reason) \
   SELECT * FROM (SELECT 'Roy', '078-123-4576', 'Professional dev') as temp \
   WHERE NOT EXISTS \
   (SELECT 'Roy' FROM visitors WHERE visitors = '078-123-4576') LIMIT 1")
db.commit()


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
v_fullname_ent = Entry(window)
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
