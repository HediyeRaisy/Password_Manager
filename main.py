from tkinter import *
from tkinter import messagebox
import random
import json
# -------------------------------- SEARCH --------------------------------------- #
def search():

    try:
        with open("pass.json",mode="r") as file:
            data = json.load(file)
            if web_input.get() in data:
                messagebox.showinfo(title="Information", message=f"Web: {web_input.get()}\n"
                                                                 f"Email:   {data[web_input.get()]['email']}\n"
                                                                 f"Password: {data[web_input.get()]['pass']}")
            else:
                messagebox.showerror(title="NOT FOUND",message="Website information not found!")
    except:
        messagebox.showerror(title="EROR!",message="NO Data File Found :(")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    new_data = {
        web_input.get(): {
            "email": f"{email_input.get()}",
            "pass": f"{pass_input.get()}"
        }
    }
    if email_input.get() == "" or pass_input.get() == "" or web_input == "":
        messagebox.showerror()
    else:
        is_ok = messagebox.askokcancel(title=f"{web_input.get()}",
                                       message=f"Your Info is:\nEmail: {email_input.get()}\n"
                                               f"Pass: {pass_input.get()}")
        if is_ok:
            try:
                with open("pass.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)

            except:
                with open("pass.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
                    web_input.delete(0, END)
                    # email_input.delete(0, END)
                    pass_input.delete(0, END)
            else:
                with open("pass.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                    web_input.delete(0, END)
                    # email_input.delete(0, END)
                    pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, bg="black")

canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web = Label(text="Website:", font=("Arial", 15), bg="black")
web.grid(row=1, column=0)

web_input = Entry(width=21, bg="white", highlightthickness=0, fg="black", insertbackground="black")
web_input.focus()
web_input.grid(row=1, column=1)

search = Button(text="Search",bg="black", highlightbackground="black", highlightthickness=3,width=10,command=search)
search.grid(row=1,column=2)

email = Label(text="Email/Username:", font=("Arial", 15), bg="black")
email.grid(row=2, column=0)

email_input = Entry(width=35, bg="white", highlightthickness=0, fg="black", insertbackground="black")
email_input.insert(0, "hedoyeraisy@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", font=("Arial", 15), bg="black")
password.grid(row=3, column=0)

pass_input = Entry(width=21, bg="white", highlightthickness=0, fg="black", insertbackground="black")
pass_input.grid(row=3, column=1)

generate = Button(text="Generate Pass", bg="black", highlightbackground="black", highlightthickness=0,
                  command=make_password)
generate.grid(row=3, column=2)

add = Button(text="Add", bg="black", highlightbackground="black", width=32, highlightthickness=0, command=add_pass)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
