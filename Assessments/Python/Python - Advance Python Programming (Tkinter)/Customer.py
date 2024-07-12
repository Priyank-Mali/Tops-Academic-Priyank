from tkinter import *
from register import *

def main():
    root = Tk()
    obj = RegistrationForm(root,'Customer')
    obj.create_registration_form()
    root.mainloop()

def cutomer_window():
    customer_screen = Tk()
    customer_screen.title('Customer window')
    customer_screen.geometry('400x400')
    
    customer_lable = Label(customer_screen,text='Customer Window',font=20,fg='black',bg='orange')
    customer_lable.pack(pady=30,fill=X)
    
    register_bt = Button(customer_screen,text='Register',font=20,anchor='center',bg='skyblue',fg='red',command=main)
    register_bt.pack(pady=3)
    login_bt = Button(customer_screen,text='Login',font=20,width=7,anchor='center',bg='skyblue',fg='red')
    login_bt.pack(pady=3)
    view_bt = Button(customer_screen,text='View all',font=20,bg='skyblue',fg='red',anchor='center')
    view_bt.pack(pady=3)
    
    customer_screen.mainloop()

