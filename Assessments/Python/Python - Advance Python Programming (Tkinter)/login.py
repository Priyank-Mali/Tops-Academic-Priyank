# gui.py

import tkinter as tk

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Product Management Application')
        self.master.geometry('400x300')
        self.create_login_form()

    def create_login_form(self):
        self.lbl_contact = tk.Label(self.master, text="Contact:")
        self.lbl_contact.grid(row=0, column=0, padx=10, pady=5)
        self.entry_contact = tk.Entry(self.master)
        self.entry_contact.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_gender = tk.Label(self.master, text="Gender:")
        self.lbl_gender.grid(row=1, column=0, padx=10, pady=5)
        self.entry_gender = tk.Entry(self.master, show="*")
        self.entry_gender.grid(row=1, column=1, padx=10, pady=5)

        self.btn_login = tk.Button(self.master, text="Login", command=self.login)
        self.btn_login.grid(row=2, column=1, padx=10, pady=5)

    def login(self):
        contact = self.entry_contact.get()
        gender = self.entry_gender.get()

        # Check if email and password are valid
        # Instantiate the appropriate user (ProductManager or Customer)
        # Redirect to the respective functionality based on user type
