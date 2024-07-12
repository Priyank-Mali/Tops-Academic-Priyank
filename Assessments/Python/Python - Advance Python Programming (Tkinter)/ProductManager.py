from tkinter import *
from register import *
from login import *


def Manager_window():
    manager_screen = Tk()
    manager_screen.title('Product Manager window')
    manager_screen_width = 400
    manager_screen_height = 400
    manager_screen.geometry(f'{manager_screen_width}x{manager_screen_height}')
    
    manager_lable = Label(manager_screen,text='Manager Window',font=20,fg='black',bg='orange')
    manager_lable.pack(pady=30,fill=X)
    
    register_bt = Button(manager_screen,text='Register',font=20,anchor='center',bg='skyblue',fg='red',command=main)
    register_bt.pack(pady=3)
    login_bt = Button(manager_screen,text='Login',font=20,width=7,anchor='center',bg='skyblue',fg='red',command=Login)
    login_bt.pack(pady=3)
    view_bt = Button(manager_screen,text='View all',font=20,bg='skyblue',fg='red',anchor='center')
    view_bt.pack(pady=3)
    
    manager_screen.mainloop()
