# LIFE CHOICES ONLINE
# Sign-in
from tkinter import *

# Quit
def quit():
    admin.destroy()

def open_admin():
    global window
    global login_gui
    global keyspressed
    global admin

    print(f"Pressed a key: {keyspressed} times")
    keyspressed += 1

    admin.bind("<Key>", lambda x: Tk())
    admin.geometry("530x500")
    admin.title("Admin")

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

def visit():
    global window
    global visitw
    global log_window

    window.withdraw()

    visitorw= Tk()
    visitorw.geometry("500x500")
    visitorw.title("Visitor")

    welcome_lbl= Label(visitorw,text="Welcome dear visitor")
    welcome_lbl.place(x=100, y=50)
    welcome_lbl.config(font=("Courier", 20))

    sub_message = Label(visitorw,text="We hope you will enjoy your time with us here \n at")
    sub_message.place(x=30,y=100)
    sub_message.config(font=("Courier", 12))

    last_message= Label(visitorw,text="LIFE CHOICES ACADEMY")
    last_message.place(x=150,y= 150 )
    last_message.config(font=("Courier", 16))

    vis_fullname_lbl = Label(visitorw,text= "Please enter your full name\n with spacing: ")
    vis_fullname_lbl.place(x=180, y= 200)

    v_fullname_ent = Entry(visitorw)
    v_fullname_ent.place(x=180,y=250)

    mobile_lbl = Label(visitorw,text="Please enter your mobile number: ")
    mobile_lbl.place(x=180,y=300)

    mobile_ent = Entry(visitorw)
    mobile_ent.place(x=180,y=330)

    visitor_login_btn = Button(visitorw,text="Visitor",width=40)
    visitor_login_btn.place(x=80,y=400)

    visitorw.mainloop()


def log_window():
    global window
    global visitw
    global log_window

    # Start of the GUI
    login_gui = Tk()
    login_gui.geometry("520x300")
    login_gui.title("Login to Life Choices-Online")

    # canvas = Canvas(log_window, width = 520, height = 90,bg="black")
    # img = PhotoImage(file="index.png")
    # canvas.create_image(5,5, anchor=NW, image=img)
    # canvas.pack()

    # FULL NAME
    # name label
    fullname_lbl = Label(login_gui,text="Please enter your full name with a space: ")
    fullname_lbl.place(x=10,y=100)

    # fullname entry for users
    fullname_ent = Entry(login_gui)
    fullname_ent.place(x= 290,y=100)

    # Usernamepassword_ent.pack()
    # username label for users
    username_lbl = Label(login_gui,text="Username: ")
    username_lbl.place(x=10,y=130)

    # username entry for users
    username_ent = Entry(login_gui)
    username_ent.place(x= 290,y=130)

    # PASSWORD
    # password label for users
    password_lbl = Label(login_gui,text="Please enter your password: ")
    password_lbl.place(x=10,y=160)

    # password entry for users
    password_ent = Entry(login_gui)
    password_ent.place(x= 290,y=160)

    # def on_record():
    #     messagebox.showinfo("Welcome", "You have \n successfully \n logged in.")
    # # Login Button

    login_btn = Button(login_gui,text="Log-in")
    login_btn.place(x=100, y=200)
    login_btn.config(width = 10)

    logout_btn = Button(login_gui,text="Log-out")
    logout_btn.place(x=290, y=200)
    logout_btn.config(width = 10)

    login_gui.mainloop()

# Mainwindow
window = Tk()
window.title("Life Choices online")
window.geometry("250x250")

main_lbl = Label(window, text="WELCOME TO")
main_lbl.place(x=70,y=20)
main_lbl.config(font=("Courier", 12))

sub_lbl = Label(window, text="Lifechoices-Online")
sub_lbl.place(x=20,y=50)
sub_lbl.config(font=("Courier", 15))

# LOGIN BUTTON
main_login_btn = Button(window,text="Login",command=log_window)
main_login_btn.place(x=70,y= 100)
main_login_btn.config(width=10)

# REGISTER BUTTON
# button to register a new user
register_btn = Button(window,text="Register")
register_btn.place(x=70,y= 200)
register_btn.config(width= 10)

# VISITOR BUTTON
# visitor button
visitor_btn = Button(window,text="Visitor",command=visit)
visitor_btn.place(x=70, y=150)
visitor_btn.config(width=10)

window.mainloop()

# IF "a" or "A" IS PRESSED ON THIS SCREEN IT NEEDS TO OPEN THE ADMIN SCREEN
