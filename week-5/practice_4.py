import tkinter as tk
from tkinter import messagebox as msgbox

#handling button clicking event
def button_click():

#show an info mesage box 
 msgbox.showinfo("INFO","Welcome to COS 102 GUI App!\n")

#ask for user confirmation
 result = msgbox.askyesno("Confirmation","Do you want to continue?")

#create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

#add a label widget
label = tk.Label(root, text="Hello Friend\n")
label.pack()

#add a button widget
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

#style the button
button.config(fg="white", bg="purple")


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

 def submit():
  username = username_entry.get()
  passwordd = password_entry.get()

  if username == "Nehi" and password == "cos102":
   welcomeMessage(username)
  else:
   messagebox.showerror("Login","Invalid username or password") 

root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

#username label entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#password lebel and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

#create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()