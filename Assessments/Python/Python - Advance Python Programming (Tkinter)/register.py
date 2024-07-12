from tkinter import *
from tkinter import ttk
from databaseconnector import *

class RegistrationForm:

    def __init__(self,master,role):
        self.master = master
        self.master.title('Registration Window')
        self.master.geometry('400x400')
        self.role = role

    def create_registration_form(self):
        # Name
        self.lbl_name = Label(self.master, text="Name*:",font=20)
        self.lbl_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Contact
        self.lbl_contact = Label(self.master, text="Contact*:",font=20)
        self.lbl_contact.grid(row=1, column=0, padx=10, pady=5)
        self.entry_contact = Entry(self.master)
        self.entry_contact.grid(row=1, column=1, padx=10, pady=5)

        # Email
        self.lbl_email = Label(self.master, text="Email*:",font=20)
        self.lbl_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = Entry(self.master)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        # Gender
        self.lbl_gender = Label(self.master, text="Gender*:",font=20)
        self.lbl_gender.grid(row=3, column=0, padx=10, pady=5)
        self.entry_gender = Entry(self.master)
        self.entry_gender.grid(row=3, column=1, padx=10, pady=5)

        #city
        self.lbl_city = Label(self.master,text='City*',font=20)
        self.lbl_city.grid(row=4,column=0,padx=10,pady=10)
        self.entry_city = Entry(self.master)
        self.entry_city.grid(row=4,column=1)
    
        # Register Button
        self.btn_register = Button(self.master, text="Register", command=self.register_data)
        self.btn_register.grid(row=6, column=1, padx=10, pady=5)


    def register_data(self):
        name = self.entry_name.get()
        contact = self.entry_contact.get()
        email = self.entry_email.get()
        gender = self.entry_gender.get()
        city = self.entry_city.get()

        if not name or not contact or not email or not gender or not city:
            Label(self.master, text='Please fill all required fields', fg='red').grid(row=5, column=1)
            return

        if not name.isalpha():
            Label(self.master, text='Invalid name', fg='red').grid(row=0, column=2)
            return
        
        if not contact.isdigit():
            Label(self.master, text='Invalid contact number', fg='red').grid(row=1, column=2)
            return

        if gender.lower() not in ['male', 'female']:
            Label(self.master, text='Invalid gender', fg='red').grid(row=3, column=2)
            return

        if self.role == 'Customer':
            table_name = 'Customer'
        else:
            table_name = 'Product_Manager'

        sql = f"""INSERT INTO {table_name} (Name, Contact, Email, Gender, City) VALUES (%s, %s, %s, %s, %s)"""
        value = (name, contact, email, gender, city)

        try:
            mycursor.execute(sql, value)
            conn.commit()
            print("Data inserted successfully.")
            Label(self.role,text='Registration Done!!',fg='green').grid(row=6,column=2)
            
            # Clear the input fields after successful insertion
            self.entry_name.delete(0, 'end')
            self.entry_contact.delete(0, 'end')
            self.entry_email.delete(0, 'end')
            self.entry_gender.delete(0, 'end')
            self.entry_city.delete(0, 'end')
        except Exception as e:
            print("Error:", type(e).__name__)
            print("Duplicate entry for contact:", contact)
