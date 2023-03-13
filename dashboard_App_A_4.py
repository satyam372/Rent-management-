from tkinter import * 




def back():
    import dashboard_3
    dashbord_App_A.destroy()
    

def add():
    
    import add_tenant
    dashbord_App_A.destroy()





dashbord_App_A = Tk()
dashbord_App_A.title("dashboard")
dashbord_App_A.geometry('990x660+50+50')


Welcomelabel=Label(dashbord_App_A,text='Welcome to appartment A',font=('Microsoft Yahei UI Light',35,'bold'))
Welcomelabel.place(x=290,y=50)

selectLabel=Label(dashbord_App_A,text='-> Options:',font=('Microsoft Yahei UI Light',30,'bold'))
selectLabel.place(x=60,y=170)

searchButton=Button(dashbord_App_A,text='Search Teanant',font=('Microsoft Yahei UI Light',18,'bold'))
searchButton.place(x=150,y=270)

emptyButton=Button(dashbord_App_A,text='empty rooms',font=('Microsoft Yahei UI Light',18,'bold'))
emptyButton.place(x=150,y=370)


vacantButton=Button(dashbord_App_A,text='vacant place',font=('Microsoft Yahei UI Light',18,'bold'))
vacantButton.place(x=150,y=470)


totalButton=Button(dashbord_App_A,text='total rent from apartment',font=('Microsoft Yahei UI Light',18,'bold'))
totalButton.place(x=150,y=570)



addButton=Button(dashbord_App_A,text='add tenant',font=('Microsoft Yahei UI Light',18,'bold'),command=add)
addButton.place(x=650,y=270)



seeButton=Button(dashbord_App_A,text='see flats',font=('Microsoft Yahei UI Light',18,'bold'))
seeButton.place(x=650,y=370)



paymentButton=Button(dashbord_App_A,text='add payment',font=('Microsoft Yahei UI Light',18,'bold'))
paymentButton.place(x=650,y=470)



remainButton=Button(dashbord_App_A,text='remaining payment',font=('Microsoft Yahei UI Light',18,'bold'))
remainButton.place(x=650,y=570)


gobackButton=Button(dashbord_App_A,text='go back',font=('Microsoft Yahei UI Light',18,'bold'),command=back)
gobackButton.place(x=100,y=50)




dashbord_App_A.mainloop()