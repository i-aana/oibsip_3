import tkinter as tk
from tkinter import StringVar, BooleanVar, messagebox,IntVar
import random

lowerCaseCharacters = "abcdefghijklmnopqrstuvwxyz"
upperCaseCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialCharacters = "@#$%^&*()-_=+|{};:/?.>"
spaceCharacters = " "
numbers = "0123456789"

def generate_password():
    characters = ""
    if lowercase_var.get():
        characters += lowerCaseCharacters
    if uppercase_var.get():
        characters += upperCaseCharacters
    if specialcase_var.get():
        characters += specialCharacters
    if whitespace_var.get():
        characters += spaceCharacters
    if number_var.get():
        characters += numbers

    if characters:
        length=length_var.get()
        if length<=0:
            messagebox.showwarning("Input Error","please input the length of password")
        password = get_random_characters(characters,length)
        password_var.set(password)
    else:
        messagebox.showwarning("Input Error", "Please select at least one character set")

def get_random_characters(characters,length):
    
    password = ""
    while len(password) < length:
        get_random_index = random.randint(0, len(characters) - 1)
        if removeduplicate_var.get() and characters[get_random_index] in password:
            continue
        password += characters[get_random_index]
    return password

root = tk.Tk()
root.title("Password Generator")

lowercase_var = BooleanVar()
uppercase_var = BooleanVar()
specialcase_var = BooleanVar()
whitespace_var = BooleanVar()
removeduplicate_var = BooleanVar()
number_var = BooleanVar()
password_var = StringVar()
length_var=IntVar()

tk.Checkbutton(root, text="Lowercase", variable=lowercase_var).pack()
tk.Checkbutton(root, text="Uppercase", variable=uppercase_var).pack()
tk.Checkbutton(root, text="Special Characters", variable=specialcase_var).pack()
tk.Checkbutton(root, text="Whitespace", variable=whitespace_var).pack()
tk.Checkbutton(root, text="Remove Duplicate", variable=removeduplicate_var).pack()
tk.Checkbutton(root, text="Numbers", variable=number_var).pack()

tk.Label(root, text="Length of Password:").pack()
tk.Entry(root, textvariable=length_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()

tk.Entry(root, textvariable=password_var, width=30).pack()

root.mainloop()