import customtkinter as ctk
from PIL import ImageTk, Image

root = ctk.CTk()
root.geometry("500x500")
root.title("Client Management and Invoicing System")

canvas = ctk.CTkCanvas(root, width=650, height=650)
canvas.pack()

bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((650, 650), Image.LANCZOS)
bg_image_tk = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor="nw", image=bg_image_tk)

l = ctk.CTkLabel(canvas, text="Client Management and Invoicing System", font=ctk.CTkFont(weight="bold"),bg_color="#616666")
canvas.create_window(300, 50, window=l)

def invoice():
    import invoice

B1 = ctk.CTkButton(canvas, text="INVOICE GENERATOR", command=invoice, width=150, height=50,bg_color="#616666")
canvas.create_window(300, 150, window=B1)

def data_entry():
    import data_entry

B2 = ctk.CTkButton(canvas, text="DATA ENTRY FORM", command=data_entry, width=150, height=50,bg_color="#616666")
canvas.create_window(300, 220, window=B2)

def data_view():
    import data_view

B3 = ctk.CTkButton(canvas, text="CLIENT DETAILS", command=data_view, height=50, width=150,bg_color="#616666")
canvas.create_window(300, 290, window=B3)
   
root.mainloop()