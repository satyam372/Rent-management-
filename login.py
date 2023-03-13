from tkinter import *
from PIL import ImageTk,Image




def user_enter(event):  # event is a variable which accepts the value passed by the on_enter function
   if usernameEntery.get()=='Enter Username':
     usernameEntery.delete(0,END)


def password_enter(event):
    if passwordEntery.get()=='Enter password':
        passwordEntery.delete(0,END)
        passwordEntery.configure(show='*')

   #def login():

 # for login entery
login_window =Tk()
login_window.geometry('990x660+50+50') # set the size of window
# login_window.resizable(0,0) # to fix the size of window,,disable the function
login_window.title('login page') # gives the title for the page
bgImage=Image.open('C:\\Users\\Satyam\\Desktop\\satyam\\login.jpg')
img=bgImage.resize((2000, 880))
bkend=ImageTk.PhotoImage(img)
bgLabel=Label(login_window,image=bkend)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='User login',font=('Microsoft Yahei UI Light',35,'bold'),fg='black')
heading.place(x=700,y=500)

usernameEntery=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',20,'bold')) # to take the entry from the user
usernameEntery.place(x=500,y=300)
usernameEntery.insert(0,'Enter Username')

usernameEntery.bind('<FocusIn>',user_enter)


# for password entery


passwordEntery=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',20,'bold')) # to take the entry from the user
passwordEntery.place(x=500,y=400)
passwordEntery.insert(0,'Enter password')
#passwordEntery.configure(show='*')

passwordEntery.bind('<FocusIn>',password_enter)

loginButton=Button(login_window,text='Login',font=('Microsoft Yahei UI Light',20,'bold'),bd=5,bg='white',activebackground='white',fg='blue')
loginButton.place(x=500,y=500)


signuplabel=Label(login_window,text='dont have an account?',font=('Microsoft Yahei UI Light',15,'bold'))
signuplabel.place(x=750,y=500)
heading.place(x=600,y=150)

createnewbutton=Button(login_window,text='Create one',font=('Microsoft Yahei UI Light',15,'bold'),bd=5,bg='white',activebackground='white',fg='blue')
createnewbutton.place(x=750,y=550)







login_window.mainloop()





