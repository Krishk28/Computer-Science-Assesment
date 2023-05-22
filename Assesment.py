import tkinter 
from tkinter import ttk 
from tkinter import messagebox

#create window
window = tkinter.Tk()
#window title 
window.title("Julie's Party Hire")

#frame
frame = tkinter.Frame(window)
frame.pack()
party_hire_frame = tkinter.LabelFrame(frame, text="Julie's Party Hire", font = ("",20))
party_hire_frame.grid(row= 0, column= 0, pady=20, padx=20)
