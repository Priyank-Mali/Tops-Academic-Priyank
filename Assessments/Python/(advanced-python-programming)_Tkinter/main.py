from tkinter import *
from registration import Registrations


def open_registration(window, role):
    registration_window = Toplevel(window)
    reg_form = Registrations(registration_window, role)
    reg_form.RegistrationForm()

# ----window size------
window = Tk()
window.title("Registration Form")
window.geometry("300x300")
window.resizable(0,0) # this is for lock window screen
window.configure(bg='black')

# ----manager and customer button------

manager_bt = Button(window,text="Manager",font=60, command=lambda: open_registration(window, "manager"))
manager_bt.pack(pady=60,anchor='center')

customer_bt = Button(window,text="Customer",font=60,command=lambda: open_registration(window, "customer"))
customer_bt.pack(anchor='center')




# # ----window Frame------

# frame = Frame(window,width=500,height=500,bg="black",bd=8)
# frame.place(x=0,y=0)

# # ----Lable and Entry Field------
# heading = Label(frame,text="Registration Form",fg="white",bg="black",font=20)
# heading.place(x=50,y=3)



window.mainloop()