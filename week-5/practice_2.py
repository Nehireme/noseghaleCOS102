import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def welcomeMessage(username):
#create a Tkinter window
 window = tk.Toplevel(root)
 window.title("Admin Box")
 window.geometry("500x200")

 label_1 = tk.Label(windoow, text=f"Welcome {username}\n")
 lable_1.pack()
 label_2.tk.Label(window, text="This is python GUI with Tkinter")
 lable_2.pack()

 #run the event loop sh
 root.mainloop()

 def submit():
  username = username_entry.get()
  passwordd = password_entry.get()

  if username == "Nehi" and password == "cos102":
   welcomeMessage(username)
  else:
   messagebox.showerror("Login","Invalid username or password") 