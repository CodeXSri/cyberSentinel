from tkinter import *
from tkinter import messagebox

def toggle_username():
    if username_entry.cget('show') == '':
        username_entry.config(show='●')
        username_eye_btn.config(text='🙈')
    else:
        username_entry.config(show='')
        username_eye_btn.config(text='👁️')

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        password_eye_btn.config(text='🙈')
    else:
        password_entry.config(show='')
        password_eye_btn.config(text='👁️')
 
def access_system():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Missing Info", "Please enter both username and password.")
    elif username == "admin" and password == "admin123":
        messagebox.showinfo("Access Granted", "Welcome to CyberSentinel!")
    else:
        messagebox.showerror("Access Denied", "Username and password do not match. Please try again.")

root = Tk()
root.title("CyberSentinel Access Engine")
root.geometry("600x450")
root.configure(bg="#0b1f3a")

# Title
title_label = Label(root, text="🔐 CyberSentinel Access Engine", font=("Helvetica", 20, "bold"),
                    bg="#0b1f3a", fg="white")
title_label.pack(pady=20)

input_frame = Frame(root, bg="#0b1f3a")
input_frame.pack(pady=10)

# Username
username_label = Label(input_frame, text="Username:", fg="white", bg="#0b1f3a", font=("Helvetica", 14))
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

username_box = Frame(input_frame)
username_box.grid(row=0, column=1, pady=10)

username_entry = Entry(username_box, font=("Helvetica", 14, "bold"), show="●", width=25)
username_entry.pack(side=LEFT)

username_eye_btn = Button(username_box, text='🙈', command=toggle_username, bg="white", relief=FLAT)
username_eye_btn.pack(side=RIGHT, padx=(5, 0))

# Password
password_label = Label(input_frame, text="Password:", fg="white", bg="#0b1f3a", font=("Helvetica", 14))
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)

password_box = Frame(input_frame)
password_box.grid(row=1, column=1, pady=10)

password_entry = Entry(password_box, font=("Helvetica", 14, "bold"), show="*", width=25)
password_entry.pack(side=LEFT)

password_eye_btn = Button(password_box, text='🙈', command=toggle_password, bg="white", relief=FLAT)
password_eye_btn.pack(side=RIGHT, padx=(5, 0))

# Access Button
access_button = Button(input_frame, text="Access", command=access_system,
                       font=("Helvetica", 14), bg="#1e90ff", fg="white", width=25)
access_button.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
