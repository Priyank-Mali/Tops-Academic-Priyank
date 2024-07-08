from tkinter import *

class Registrations:
    def __init__(self,master,role):
        self.master = master
        self.master.title("Registration Form")
        self.master.geometry("400x400")
        self.master.resizable(0,0)
        self.master.configure(bg='black')
        self.role = role

    def RegistrationForm(self):
        # ------name------
        self.lbl_name = Label(self.master, text="Name*:",font=20)
        self.lbl_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # ------contact-------
        self.lbl_contact = Label(self.master, text="Contact*:",font=20)
        self.lbl_contact.grid(row=1, column=0, padx=10, pady=5)
        self.entry_contact = Entry(self.master)
        self.entry_contact.grid(row=1, column=1, padx=10, pady=5)

        # ------email---------
        self.lbl_email = Label(self.master, text="Email*:",font=20)
        self.lbl_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = Entry(self.master)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        # ------gender--------
        self.lbl_gender = Label(self.master, text="Gender*:",font=20)
        self.lbl_gender.grid(row=3, column=0, padx=10, pady=5)
        self.entry_gender = Entry(self.master)
        self.entry_gender.grid(row=3, column=1, padx=10, pady=5)

        # -------city----------
        self.lbl_city = Label(self.master,text='City*',font=20)
        self.lbl_city.grid(row=4,column=0,padx=10,pady=10)
        self.entry_city = Entry(self.master)
        self.entry_city.grid(row=4,column=1)
    
        # ---------registration-button-----------
        self.btn_register = Button(self.master, text="Register")
        self.btn_register.grid(row=6, column=1, padx=10, pady=5)


