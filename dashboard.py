from tkinter import *


def back():
    import test
    dashboard.destroy()



def appar():

    import dashboard_3
    dashboard.destroy()


dashboard=Tk()
dashboard.title('dashboard')
dashboard.geometry('990x660+50+50')


heading=Label(dashboard,text='Welcome ',font=('Microsoft Yahei UI Light',35,'bold'))
heading.place(x=400,y=50)


selectAPPButton=Button(dashboard,text='Building',font=('Microsoft Yahei UI Light',18,'bold'),command=appar)
selectAPPButton.place(x=100,y=250)


selectAPPButton=Button(dashboard,text='Total rent',font=('Microsoft Yahei UI Light',18,'bold'))
selectAPPButton.place(x=100,y=350)



selectAPPButton=Button(dashboard,text='current tenant',font=('Microsoft Yahei UI Light',18,'bold'))
selectAPPButton.place(x=100,y=450)



selectAPPButton=Button(dashboard,text='All tenants',font=('Microsoft Yahei UI Light',18,'bold'))
selectAPPButton.place(x=100,y=550)

gobackButton=Button(dashboard,text='go back',font=('Microsoft Yahei UI Light',18,'bold'),command=back)
gobackButton.place(x=100,y=50)


dashboard.mainloop()