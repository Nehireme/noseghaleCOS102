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

#start the event loop
root.mainloop()