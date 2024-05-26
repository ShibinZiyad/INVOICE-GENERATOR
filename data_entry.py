import tkinter
from tkinter import ttk
from tkinter import messagebox
import openpyxl

def enter_data():
    title = title_combobox.get()
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()

    Companyname = company_name_entry.get()
    companytype = company_type_entry.get()
    phonenumber = company_phone_entry.get()
    email = company_email_entry.get()
    website = company_website_entry.get()

    filepath = r"C:\Users\91702\Documents\projects\invoice generator\Book1.xlsx"
            
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([title, firstname, lastname, age, nationality, Companyname, companytype, phonenumber, email, website ])
    workbook.save(filepath)
    messagebox.showinfo("DATA ENTRY", "SUCCUSSFULL")

    title_combobox.delete(0, tkinter.END)
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    age_spinbox.delete(0, tkinter.END)
    nationality_combobox.delete(0, tkinter.END)
    company_name_entry.delete(0, tkinter.END)
    company_type_entry.delete(0, tkinter.END)
    company_phone_entry.delete(0, tkinter.END)
    company_email_entry.delete(0, tkinter.END)
    company_website_entry.delete(0, tkinter.END)
                
window = tkinter.Tk()
window.title("Client Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Clients Information:")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.","Mrs.", "Ms.", "Dr."])
title_label.grid(row=0, column=0)
title_combobox.grid(row=1, column=0)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=1)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["India", "UAE", "USA", "KSA", "ITAY", "GERMANY", "SPAIN"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

company_info_frame =tkinter.LabelFrame(frame, text="Company Details:")
company_info_frame.grid(row= 4, column=0, padx=20, pady=10)

company_name_label = tkinter.Label(company_info_frame, text="Company Name")
company_name_label.grid(row=5, column=0)
company_type_label = tkinter.Label(company_info_frame, text="Company Type")
company_type_label.grid(row=5, column=1)

company_name_entry = tkinter.Entry(company_info_frame)
company_type_entry = tkinter.Entry(company_info_frame)
company_name_entry.grid(row=6, column=0)
company_type_entry.grid(row=6, column=1)

company_phone_label = tkinter.Label(company_info_frame, text="Phone Number")
company_phone_label.grid(row=5, column=2)
company_email_label = tkinter.Label(company_info_frame, text="Email")
company_email_label.grid(row=7, column=0)

company_phone_entry = tkinter.Entry(company_info_frame)
company_email_entry = tkinter.Entry(company_info_frame)
company_phone_entry.grid(row=6, column=2)
company_email_entry.grid(row=8, column=0)

company_website_label = tkinter.Label(company_info_frame, text="Website")
company_website_label.grid(row=7, column=1)
company_website_entry = tkinter.Entry(company_info_frame)
company_website_entry.grid(row=8, column=1)

for widget in company_info_frame.winfo_children():
    widget.grid_configure(padx=16, pady=5)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=9, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()