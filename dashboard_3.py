from tkinter import * 
from tkinter import messagebox 

import pymysql

#import signup as a



#def con():

def back():
    import dashboard
    dashbord_window.destroy()
  
# def abc():

    
#     try:
#      con=pymysql.connect(host='localhost',user='root',password='satyam@4545')
#      mycursor=con.cursor()
#      print(con)
     

#     except:
#         messagebox.showerror('Error','connection failed')
#         return

#     try:
#      query='use userdata'
#      mycursor.execute(query)
#      query='create table adres(id int auto_increment primary key not null, name varchar(100), appartment varchar(50),)'
#      mycursor.execute(query)
#     except:
#      query='use userdata'
#      mycursor.execute(query)
#      query='insert into adres(name , address ) values(%s,%s)'
#      mycursor.execute(query,('satyam','satyam'
#      'satyam','satyam'))
#      messagebox.showinfo('successful','appartment is registered')
#      con.commit()
#      con.close()

def front():
    import dashboard_App_A_4
    dashbord_window.destroy()


def add():

    import addappartme
 

    

#  try:
#      query='use userdata'
#      mycursor.execute(query)
#      query='create tabel addapartment(id int auto_increment primary key not null,name varchar(50), address varchar(100), )'

    
#  except:

    


        

dashbord_window = Tk()
dashbord_window.title("dashboard")
dashbord_window.geometry('990x660+50+50')

heading=Label(dashbord_window,text='Welcome ',font=('Microsoft Yahei UI Light',35,'bold'))
heading.place(x=400,y=50)
#frame = Tk.Frame(dashbord_window)
# #frame.pack()
# text_disp=Button(dashbord_window, text="FLOORS" )
# text_disp.place(relx=0.1,rely=0.1)
# #text_disp.pack(side=tk.LEFT)
# view_button =Button(dashbord_window, text="VIEW")       
# view_button.place(relx=0.1,rely=0.2)

selectApp=Label(dashbord_window,text='-> Select Appartment:',font=('Microsoft Yahei UI Light',18,'bold'))
selectAPPButton=Button(dashbord_window,text='Appartment A',font=('Microsoft Yahei UI Light',18,'bold'),command=front)
selectAPPButton.place(x=100,y=250)
selectApp.place(x=60,y=170)

selectApp2=Button(dashbord_window,text='Apartmenr B',font=('Microsoft Yahei UI Light',18,'bold'))
selectApp2.place(x=450,y=250)


addButton=Button(dashbord_window,text='Add apartment',font=('Microsoft Yahei UI Light',18,'bold'),command=add)
addButton.place(x=750,y=250)
# dashbord_window.mainloop()

searchLabel=Label(dashbord_window,text='-> Search tenant',font=('Microsoft Yahei UI Light',18,'bold'))
searchLabel.place(x=60,y=390)



gobackButton=Button(dashbord_window,text='go back',font=('Microsoft Yahei UI Light',18,'bold'),command=back)
gobackButton.place(x=100,y=50)
dashbord_window.mainloop()






# from tkinter import Tk, Frame, Menu

# class Example(Frame):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         self.master.title("Submenu")

#         menubar = Menu(self.master)
#         self.master.config(menu=menubar)

#         fileMenu = Menu(menubar)

#         submenu = Menu(fileMenu)
#         submenu.add_command(label="New feed",command=self)
#         submenu.add_command(label="Bookmarks")
#         submenu.add_command(label="Mail")
#         fileMenu.add_cascade(label='Import', menu=submenu, underline=0)

#         fileMenu.add_separator()

#         fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
#         menubar.add_cascade(label="File", underline=0, menu=fileMenu)


#     def onExit(self):

#         self.quit()


# def main():

#     root = Tk()
#     root.geometry("250x150+300+300")
#     app = Example()
#     root.mainloop()


# if __name__ == '__main__':
#     main()






