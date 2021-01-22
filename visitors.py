from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lifechoices",
  password="@Lifechoices1234",
  database="lifechoicesonline"
)



mycursor = mydb.cursor()

sql = "INSERT INTO visitors (full_name, mobile_number ) VALUES ( %s, %s)"
val = [
    ('')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


window = Tk()
window.geometry("500x500")
window.title("Visitor")

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

v_fullname_ent = Entry(window)
v_fullname_ent.place(x=180,y=250)

mobile_lbl = Label(window,text="Please enter your mobile number: ")
mobile_lbl.place(x=180,y=300)

mobile_ent = Entry(window)
mobile_ent.place(x=180,y=330)

visitor_login_btn = Button(window,text="Visitor",width=40)
visitor_login_btn.place(x=80,y=400)


# quit button
# quit_btn_v = Button(window,text="Quit", command= quit)
# quit_btn_v.place(x=10,y=150)
# quit_btn_v.config(width=9)



window.mainloop()
