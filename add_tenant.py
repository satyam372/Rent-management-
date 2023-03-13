from tkinter import *

from tkinter import messagebox
import pymysql


add = Tk()
add.title("dashboard")
add.geometry('990x660+50+50')



def abc():

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
     query='create table adres2(id int auto_increment primary key not null, name varchar(100),adhar varchar(100),mob varchar(100),appartment varchar(100),home varchar(100),flat varchar(100),deposit varchar(100))'
     mycursor.execute(query)
   except:
     query='use userdata'
     mycursor.execute(query)
     query='insert into adres2(name,adhar,mob,appartment,home,flat,deposit) values(%s,%s,%s,%s,%s,%s,%s)'
     mycursor.execute(query,(addEntry.get(),adhEntry.get(),mobEntry.get(),appEntry.get(),homEntry.get(),flatEntry.get(),depEntry.get()))
     messagebox.showinfo('successful','appartment is registered')
     con.commit()
     con.close()
     
     




def back():
   import dashboard_App_A_4
   add.destroy()
    


def user_add(event):  # event is a variable which accepts the value passed by the on_enter function
   if addEntry.get()=='Enter name':
     addEntry.delete(0,END)




    


def user_adh(event):  # event is a variable which accepts the value passed by the on_enter function
   if adhEntry.get()=='enter adhar no':
      adhEntry.delete(0,END)




    


def user_mob(event):  # event is a variable which accepts the value passed by the on_enter function
   if mobEntry.get()=='enter mobile no':
     mobEntry.delete(0,END)




    


def user_hom(event):  # event is a variable which accepts the value passed by the on_enter function
   if homEntry.get()=='enter home town ':
     homEntry.delete(0,END)




    


def user_app(event):  # event is a variable which accepts the value passed by the on_enter function
   if appEntry.get()=='enter appartment ':
     appEntry.delete(0,END)




    


def user_agg(event):  # event is a variable which accepts the value passed by the on_enter function
   if aggEntry.get()=='upload aggrement ':
     aggEntry.delete(0,END)




    


def user_flat(event):  # event is a variable which accepts the value passed by the on_enter function
   if flatEntry.get()=='enter flat no ':
        flatEntry.delete(0,END)




    


def user_dep(event):  # event is a variable which accepts the value passed by the on_enter function
   if depEntry.get()=='enter deposit amount ':
      depEntry.delete(0,END)




    


def user_img(event):  # event is a variable which accepts the value passed by the on_enter function
   if imgEntry.get()=='upload image ':
     imgEntry.delete(0,END)



Welcomelabel=Label(add,text='ADD TENANT',font=('Microsoft Yahei UI Light',35,'bold'))
Welcomelabel.place(x=290,y=50)



addEntry=Entry(add,text='Enter name',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
addEntry.place(x=20,y=270)
addEntry.insert(0,'Enter name')
addEntry.bind('<FocusIn>',user_add)


adhEntry=Entry(add,text='enter adhar no',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
adhEntry.place(x=400,y=270)
adhEntry.insert(0,'enter adhar no')
adhEntry.bind('<FocusIn>',user_adh)


mobEntry=Entry(add,text='enter mobile no',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
mobEntry.place(x=800,y=270)
mobEntry.insert(0,'enter mobile no')
mobEntry.bind('<FocusIn>',user_mob)


homEntry=Entry(add,text='enter home town ',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
homEntry.place(x=20,y=410)
homEntry.insert(0,'enter home town ')
homEntry.bind('<FocusIn>',user_hom)

appEntry=Entry(add,text='enter appartment ',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
appEntry.place(x=800,y=610)
appEntry.insert(0,'enter appartment ')
appEntry.bind('<FocusIn>',user_app)


aggEntry=Entry(add,text='upload aggrement ',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
aggEntry.place(x=400,y=610)
aggEntry.insert(0,'upload aggrement ')
aggEntry.bind('<FocusIn>',user_agg)


flatEntry=Entry(add,text='enter flat no ',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
flatEntry.place(x=20,y=610)
flatEntry.insert(0,'enter flat no ')
flatEntry.bind('<FocusIn>',user_flat)


depEntry=Entry(add,text='enter deposit amount ',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
depEntry.place(x=400,y=410)
depEntry.insert(0,'enter deposit amount ')
depEntry.bind('<FocusIn>',user_dep)


imgEntry=Entry(add,text='upload image ',width=18,font=('Microsoft Yahei UI Light',18,'bold'))
imgEntry.place(x=800,y=410)
imgEntry.insert(0,'upload image ')
imgEntry.bind('<FocusIn>',user_img)

addButton=Button(add,text='add',font=('Microsoft Yahei UI Light',18,'bold'),command=abc)
addButton.place(x=890,y=50)


gobackButton=Button(add,text='go back',font=('Microsoft Yahei UI Light',18,'bold'),command=back)
gobackButton.place(x=100,y=50)
add.mainloop()

                                                                                  