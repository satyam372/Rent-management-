from tkinter import *
from tkinter import messagebox  

import pymysql


def back():
    import dashboard_3
    addap.destroy()


def clear():
    appEntery.delete(0,END)
    addEntery.delete(0,END)
 



def add():

    
    try:
     con=pymysql.connect(host='localhost',user='root',password='satyam@4545')
     mycursor=con.cursor()
     print(con)
     

    except:
        messagebox.showerror('Error','connection failed')
        return

    try:
     query='use userdata'
     mycursor.execute(query)
     query='create table adres(id int auto_increment primary key not null, name varchar(100), address varchar(50))'
     mycursor.execute(query)
    except:
     query='use userdata'
     mycursor.execute(query)
     query='insert into adres(name , address ) values(%s,%s)'
     mycursor.execute(query,(appEntery.get(),addEntery.get()))
     messagebox.showinfo('successful','appartment is registered')
     con.commit()
     con.close()
     clear()

 
 
    





def app_entry(event):
    if appEntery.get()=='Enter appartment name ':
        appEntery.delete(0,END)


def add_enter(event):

    if addEntery.get()=='enter address':
        addEntery.delete(0,END)

addap=Tk()
addap.title("dashboard")
addap.geometry('990x660+50+50')


addapLabel=Label(addap,text='Add Apartment',font=('Microsoft Yahei UI Light',35,'bold'))
addapLabel.place(x=400,y=50)



appEntery=Entry(addap,width=25,font=('Microsoft Yahei UI Light',20,'bold')) # to take the entry from the user
appEntery.place(x=300,y=300)
appEntery.insert(0,'Enter appartment name ')

appEntery.bind('<FocusIn>',app_entry)


addEntery=Entry(addap,width=25,font=('Microsoft Yahei UI Light',20,'bold')) # to take the entry from the user
addEntery.place(x=300,y=400)
addEntery.insert(0,'enter address')
#passwordEntery.configure(show='*')

addEntery.bind('<FocusIn>',add_enter)


addButton=Button(addap,text='Add apartment',font=('Microsoft Yahei UI Light',20,'bold'),command=add)
addButton.place(x=500,y=500)

gobackButton=Button(addap,text='Go back',font=('Microsoft Yahei UI Light',20,'bold'),command=back)
gobackButton.place(x=300,y=500)


addap.mainloop()