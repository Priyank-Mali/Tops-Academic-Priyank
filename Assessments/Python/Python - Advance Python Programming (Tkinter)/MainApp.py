from tkinter import *
from register import *
from login import *
from Customer import cutomer_window  


def main():
    root = Tk()
    obj = RegistrationForm(root,'Product_Manager')
    obj.create_registration_form()
    root.mainloop()

def Login():
    root = Tk()
    app = GUI(root)
    app.create_login_form()
    root.mainloop()

screen = Tk()

screen_width = screen.winfo_screenwidth() 
screen_height = screen.winfo_screenheight()
app_width = screen_width
app_height = screen_height

screen.title('MainApp')
screen.geometry(f'{app_width}x{app_height}')

screen_lable = Label(screen,text='Product Management System',font=('arial', 20),fg='black',bg='orange')
screen_lable.grid(row=0, column=0, columnspan=2, pady=20)

manager_login_bt = Button(screen, text='Manager Login', font=('arial', 20), bg='skyblue', fg='red',command=Login)
manager_login_bt.grid(row=1, column=0, padx=10, pady=10)

manager_register_bt = Button(screen, text='Manager Registration', font=('arial', 20), command=main, bg='skyblue', fg='red')
manager_register_bt.grid(row=1, column=1, padx=10, pady=10)

customer_login_bt = Button(screen, text='Customer Registration', font=('arial', 20), command=main, bg='skyblue', fg='red')
customer_login_bt.grid(row=2, column=0, padx=10, pady=10)

customer_register_bt = Button(screen, text='Customer Login', font=('arial', 20), command=Login, bg='skyblue', fg='red')
customer_register_bt.grid(row=2, column=1, padx=10, pady=10)

exit_bt = Button(screen, text='Exit', font=('arial', 20), command=screen.quit, bg='skyblue', fg='red')
exit_bt.grid(row=3, column=0, columnspan=2, pady=20)

screen.mainloop()
