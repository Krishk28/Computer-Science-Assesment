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
party_hire_frame = tkinter.LabelFrame(frame, text="Julie's Party Hire", font = ("",23))
party_hire_frame.grid(row= 0, column= 0, pady=15, padx=20, ipady=5)


#Labels and headings 
customer_fullname_label = tkinter.Label(party_hire_frame,text="Customer Full Name")
customer_fullname_label.grid(row=1,column=0)

Receipt_label = tkinter.Label(party_hire_frame, text = "Receipt Number")
Receipt_label.grid(row=1,column=1)

#adding entry boxes and spin boxes 
Customer_entry = tkinter.Entry(party_hire_frame)
Receipt_entry = tkinter.Entry(party_hire_frame)

#placing said boxes onto frame using grid
Customer_entry.grid(row=3,column=0)
Receipt_entry.grid(row=3,column=1)

#adding the rest of the boxes 
hired_item_label = tkinter.Label(party_hire_frame, text="Hired Item")
hired_item_entry = tkinter.Entry(party_hire_frame)

hired_item_label.grid(row=1, column=2)
hired_item_entry.grid(row=3, column=2)

#combobox
Number_hired_label = tkinter.Label(party_hire_frame, text="Number of Items Hired")
Number_hired_combobox = ttk.Combobox(party_hire_frame, values = list(range(0, 501)),state="readonly")

Number_hired_label.grid (row=1, column=3)
Number_hired_combobox.grid (row=3, column=3)


#padding for the tk boxes 
for widget in party_hire_frame.winfo_children():
    widget.grid_configure(padx=10,pady=3)


#Submit Button
button_add= tkinter.Button(frame, text = "Submit Data",command=lambda: add_data())
button_add.grid(row=2,column = 0)


#Delete Button
button_delete= tkinter.Button(frame, text = "Delete Data",command=lambda: delete())
button_delete.grid(row=3,column = 0)


#database table frame
table_frame=tkinter.Frame(window)
table_frame.pack(pady=10)
#database columns 
columns = ("Row", "Customer Name", "Receipt Number", "Hired Item", "Amount Hired")
treeview = ttk.Treeview(table_frame, columns=columns, show="headings")
treeview.pack(side=tkinter.LEFT)


#adjusting column sizes
treeview.column("Row", width=75)
treeview.column("Customer Name", width=200)
treeview.column("Receipt Number", width=200)
treeview.column("Hired Item", width=200)
treeview.column("Amount Hired", width=200)

#headings 
for col in columns:
    treeview.heading(col,text=col)


iid = 1

def add_data():
    #Information
    Name = Customer_entry.get()
    Receipt = Receipt_entry.get()
    Item = hired_item_entry.get()
    Amount = Number_hired_combobox.get()

    #Check if Name is empty
    if Name == "":
        messagebox.showerror("Error",message="Please enter a name.")
        return

    #Check if Receipt is empty
    if Receipt == "":
        messagebox.showerror("Error",message="Please enter a receipt number.")
        return

    #Check if Item is empty
    if Item == "":
        messagebox.showerror("Error",message="Please enter an item.")
        return

    #Check if Amount is a valid number
    try:
        Amount = int(Amount)
    except ValueError:
        messagebox.showerror("Error",message="Please enter a valid amount.")
        return

    #insert data
    global iid 
    treeview.insert("", index="end", iid=iid, values=(iid,Name, Receipt, Item, Amount))
    iid +=1

#Delete data
def delete():
   # Get selected item to Delete
   selected_item = treeview.selection()[0]
   treeview.delete(selected_item)


#loop  
window.mainloop()

