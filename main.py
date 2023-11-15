from random import randint
import random
import string
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()

root.title("Password Generator")
root.geometry("500x500")

meter = ImageTk.PhotoImage(Image.open(r"D:\Meenu\Projects\password generator tkinter\password pic.jpg"))
meter_img=Label(root, image=meter, bd=0)
meter_img.pack(pady=50)

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    pw_ent.delete(0, END)
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    #return password
    pw_ent.insert(0, password)

def generate_password_gui():
    try:
        length = int(psw_len.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            pw_ent.config(text="Generated Password: " + password)
        else:
            pw_ent.config(text="Password generation failed.")
    except ValueError:
        passwd="Enter length in numbers"
        pw_ent.delete(0, END)
        pw_ent.insert(0,passwd)

def copy():
    root.clipboard_clear()
    root.clipboard_append(pw_ent.get())

psw_len=customtkinter.CTkEntry(master=root,
                               placeholder_text="Password Length",
                               width=200,
                               height=30,
                               border_width=1,
                               corner_radius=10)

psw_len.pack(pady=20)

bg_color="#1a1a1a"
pw_ent=tk.Entry(root, text="", font=("Helvetica", 20), bd=0, bg=bg_color, fg="white")
pw_ent.pack(pady=10)

letters_var = customtkinter.BooleanVar()
letters_checkbox = customtkinter.CTkCheckBox(root, text="Include Letters", variable=letters_var, checkbox_height=18, checkbox_width=18)
letters_checkbox.pack(pady=10)

numbers_var = customtkinter.BooleanVar()
numbers_checkbox = customtkinter.CTkCheckBox(master=root, text="Include Numbers", variable=numbers_var, checkbox_height=18, checkbox_width=18)
numbers_checkbox.pack(pady=10)

symbols_var = customtkinter.BooleanVar()
symbols_checkbox = customtkinter.CTkCheckBox(root, text="Include Symbols", variable=symbols_var, checkbox_height=18, checkbox_width=18)
symbols_checkbox.pack(pady=10)

btn_1=customtkinter.CTkButton(master=root,
                              text="Generate Password",
                              width=190,
                              height=40,
                              compound="top",
                              command=generate_password_gui)
btn_1.pack(pady=20)

btn_2=customtkinter.CTkButton(master=root,
                              text="Copy To Clipbpard",
                              width=190,
                              height=40,
                              fg_color="#D35858",
                              hover_color="#C77C78",
                              command=copy)
btn_2.pack(pady=20)

root.mainloop()
