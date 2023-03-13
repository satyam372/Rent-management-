from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image,ImageTk



def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    passwordEntry.delete(0,END)

def connect_database():
    if emailEntry.get()=='' or userEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('error',' enter  all information')

    else:

        try:
         con=pymysql.connect(host='localhost',user='root',password='satyam@4545')
         print(con)
         
         mycursor=con.cursor()

        except:
            messagebox.showerror('error','try again')
            return
        try:
         query='create database userdata'
         mycursor.execute(query)
         query='use userdata'
         mycursor.execute(query)
         query='create table data(id int auto_increment primary key not null,email varchar(50), username varchar(100), password varchar(50))'
         mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),userEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('successful','regestration is done')
        clear()
    
        



        






def login_page():

    signup_window.destroy()
    import test




signup_window=Tk()


def on_email(event):
 if emailEntry.get()=='Enter email':
    emailEntry.delete('0',END)

def on_name(event):
    if userEntry.get()=='enter name':
        userEntry.delete('0',END)


def on_password(event):
    if passwordEntry.get()=='enter new password':
     passwordEntry.delete('0',END)
     passwordEntry.configure(show='*')

signup_window.geometry('990x660+50+50') # set the size of window
signup_window.resizable(0,0) # to fix the size of window,,disable the function
signup_window.title('signup page') # gives the title for the page
bgimage=Image.open('C:\\Users\\Satyam\\Pictures\\Screenshot 2023-01-27 153547.jpg')
img=bgimage.resize((700, 750))
bkend=ImageTk.PhotoImage(img)
bgLabel=Label(signup_window,image=bkend)
bgLabel.place(x=0,y=0)


bgimage1=Image.open('C:\\Users\\Satyam\\Pictures\\Screenshot 2023-01-28 153808.jpg')
img1=bgimage1.resize((190, 190))
bkend1=ImageTk.PhotoImage(img1)
bgLabel1=Label(signup_window,image=bkend1)
bgLabel1.place(x=695,y=115)

heading=Label(signup_window,text='Create account',font=('Microsoft Yahei UI Light',35,'bold'),fg='firebrick')
heading.place(x=595,y=50)

emailEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',20,'bold'),fg='firebrick')
emailEntry.place(x=595,y=300)
emailEntry.insert(0,'Enter email')
emailEntry.bind('<FocusIn>',on_email)

userEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',20,'bold'),fg='firebrick')
userEntry.place(x=595,y=400)
userEntry.insert(0,'enter name')
userEntry.bind('<FocusIn>',on_name)
#bgimage=Label(signup_window)


passwordEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',20,'bold'),fg='firebrick')
passwordEntry.place(x=595,y=500)
passwordEntry.insert(0,'enter new password')
passwordEntry.bind('<FocusIn>',on_password)


savebutton=Button(signup_window,text='Save',font=('Microsoft Yahei UI Light',20,'bold'),bd=5,bg='white',activebackground='white',fg='firebrick',command=connect_database)
savebutton.place(x=900,y=600)



gobackbutton=Button(signup_window,text='go back',font=('Microsoft Yahei UI Light',20,'bold'),bd=5,bg='white',activebackground='white',fg='firebrick',command=login_page)
gobackbutton.place(x=700,y=600)

signup_window.mainloop()