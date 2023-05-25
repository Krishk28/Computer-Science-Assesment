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

#Labels and headings 
customer_fullname_label = tkinter.Label(party_hire_frame,text="Customer Full Name")
customer_fullname_label.grid(row=1,column=0)

Receipt_label = tkinter.Label(party_hire_frame, text = "Receipt Number")
Receipt_label.grid(row=1,column=1)

#adding entry boxes and spin boxes 
group_leader_entry = tkinter.Entry(party_hire_frame)
Receipt_label_entry = tkinter.Entry(party_hire_frame)

#placing said boxes onto frame using grid
group_leader_entry.grid(row=3,column=0)
Receipt_label_entry.grid(row=3,column=1)

#adding the rest of the boxes 
hired_item_label = tkinter.Label(party_hire_frame, text="Hired Item")
hired_item_entry = tkinter.Entry(party_hire_frame)

hired_item_label.grid(row=1, column=2)
hired_item_entry.grid(row=3, column=2)


Number_hired_label = tkinter.Label(party_hire_frame, text="Number of Items Hired")
Number_hired = ttk.Combobox(party_hire_frame, values = list(range(0, 501)),state="readonly")


Number_hired_label.grid (row=1, column=3)
Number_hired.grid (row=3, column=3)

    #padding for the tk boxes 
for widget in party_hire_frame.winfo_children():
    widget.grid_configure(padx=10,pady=3)







#loop  
window.mainloop()