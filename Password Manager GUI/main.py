from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
#pyperclip module is used to copy the generated password to your clipboard when you click on the Generate Password Button.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():

    password_list = []

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(numbers) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(END, string=password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_collect():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "Email": email,
            "Password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

def find_password():
    try:
        website_required = website_entry.get().title()
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email_required = data[website_required]["Email"]
            password_required = data[website_required]["Password"]
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exists")
    else:
        messagebox.showinfo(title=website_required, message=f"Email: {email_required}\nPassword: {password_required}")
    finally:
        website_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.config(pady=2)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.config(pady=2)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.config(pady=2)
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

search = Button(text="Search", command=find_password)
search.grid(column=2, row=1, sticky="EW")

email_entry = Entry(width=35)
email_entry.insert(END, "testtesttest@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

pwd_button = Button(text="Generate Password", command=password_generator)
pwd_button.grid(column=2, row=3, sticky="EW")

add = Button(text="Add", width=30, command=data_collect)
add.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()