import tkinter
from tkinter import ttk 
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
from tkcalendar import DateEntry

def clear_item():
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, "1")
    desc_entry.delete(0, tkinter.END)
    price_spinbox.delete(0, tkinter.END)
    price_spinbox.insert(0, "0.0")

invoice_list = []
def add_item():
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]
    tree.insert('',0, values=invoice_item)
    clear_item()
    
    invoice_list.append(invoice_item)

    
def new_invoice():
    name_entry.delete(0, tkinter.END)
    name1_entry.delete(0, tkinter.END)
    address_entry.delete(0, tkinter.END)
    address1_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    phone1_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    email1_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    
    invoice_list.clear()
    
def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = name_entry.get()
    name1 = name1_entry.get()
    date = date_entry.get()
    date1 = date1_entry.get()
    phone = phone_entry.get()
    phone1 =phone1_entry.get()
    address = address_entry.get()
    address1 = address1_entry.get()
    email =email_entry.get()
    email1 =email1_entry.get()
    subtotal = sum(item[3] for item in invoice_list) 
    discount = 0.1
    vat = 0.05
    shipping = 0.03
    total = (subtotal*(1-discount))+(subtotal*vat)+(subtotal*shipping)
    
    doc.render({"name":name,
                "shipname":name1,
                "date":date,
                "shipdate":date1,
                "phone":phone,
                "shipphone":phone1,
                "address":address,
                "shipaddress":address1,
                "email":email,
                "shipemail":email1,
                "invoice_list": invoice_list,
                "subtotal":subtotal,
                "discount":(subtotal*0.1),
                "vat":(subtotal*0.05),
                "shipping":(subtotal*0.03),
                "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
    new_invoice()
    

window = tkinter.Tk()
window.title("Invoice Generator Form")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

billing_label = tkinter.Label(frame, text="BILLING DETAILS:")
billing_label.grid(row=0, column=0)

name_label = tkinter.Label(frame, text="NAME")
name_label.grid(row=1, column=0)
name_entry = tkinter.Entry(frame)
name_entry.grid(row=1, column=1)

date_label = tkinter.Label(frame, text="DATE")
date_label.grid(row=2, column=0)
date_entry = DateEntry(frame, width =15, bg="darkblue", fg="white", year=2023)
date_entry.grid(row=2,column=1)

address_label = tkinter.Label(frame, text="ADDRESS")
address_label.grid(row=3, column=0)
address_entry = tkinter.Entry(frame)
address_entry.grid(row=3, column=1)

phone_label = tkinter.Label(frame, text="PHONE NO")
phone_label.grid(row=4, column=0)
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=4, column=1)

email_label = tkinter.Label(frame, text="EMAIL")
email_label.grid(row=5, column=0)
email_entry = tkinter.Entry(frame)
email_entry.grid(row=5, column=1)

shipping_label = tkinter.Label(frame, text="SHIPPING DETAILS:")
shipping_label.grid(row=0, column=2)

name1_label = tkinter.Label(frame, text="NAME")
name1_label.grid(row=1, column=2)
name1_entry = tkinter.Entry(frame)
name1_entry.grid(row=1, column=3)

date1_label = tkinter.Label(frame, text="DATE")
date1_label.grid(row=2, column=2)
date1_entry = DateEntry(frame, width =15, bg="darkblue", fg="white", year=2023)
date1_entry.grid(row=2,column=3)

address1_label = tkinter.Label(frame, text="ADDRESS")
address1_label.grid(row=3, column=2)
address1_entry = tkinter.Entry(frame)
address1_entry.grid(row=3, column=3)

phone1_label = tkinter.Label(frame, text="PHONE NO")
phone1_label.grid(row=4, column=2)
phone1_entry = tkinter.Entry(frame)
phone1_entry.grid(row=4, column=3)

email1_label = tkinter.Label(frame, text="EMAIL")
email1_label.grid(row=5, column=2)
email1_entry = tkinter.Entry(frame)
email1_entry.grid(row=5, column=3)

label = tkinter.Label(frame, text="")
label.grid(row=6, column=0)

product_label = tkinter.Label(frame, text="PRODUCT DETAILS:")
product_label.grid(row=7, column=0)


qty_label = tkinter.Label(frame, text="Qty")
qty_label.grid(row=8, column=0)
qty_spinbox = tkinter.Spinbox(frame, from_=1, to=100)
qty_spinbox.grid(row=9, column=0)

desc_label = tkinter.Label(frame, text="Description")
desc_label.grid(row=8, column=1)
desc_entry = tkinter.Entry(frame)
desc_entry.grid(row=9, column=1)

price_label = tkinter.Label(frame, text="Unit Price")
price_label.grid(row=8, column=2)
price_spinbox = tkinter.Spinbox(frame, from_=0.0, to=500, increment=0.5)
price_spinbox.grid(row=9, column=2)

add_item_button = tkinter.Button(frame, text = "Add item", command = add_item)
add_item_button.grid(row=9, column=3)

columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")

    
tree.grid(row=11, column=0, columnspan=4, padx=20, pady=10)


save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
save_invoice_button.grid(row=12, column=0, columnspan=4, sticky="news", padx=20, pady=5)
new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=13, column=0, columnspan=4, sticky="news", padx=20, pady=5)



window.mainloop()