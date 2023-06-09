import tkinter 
from tkinter import ttk 
from tkinter import messagebox

#creating window
window = tkinter.Tk()
#windows title 
window.title("Julie's Party Hire")

#creating a frame inside the window for all the widgets to go inside of 
frame = tkinter.Frame(window)
frame.pack()
party_hire_frame = tkinter.LabelFrame(frame, text="Julie's Party Hire", font = ("",23))
party_hire_frame.grid(row= 0, column= 0, pady=15, padx=20, ipady=4)

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

#adding a combobox
Number_hired_label = tkinter.Label(party_hire_frame, text="Number of Items Hired")
Number_hired_combobox = ttk.Combobox(party_hire_frame, values = list(range(0, 501)))

Number_hired_label.grid (row=1, column=3)
Number_hired_combobox.grid (row=3, column=3)

#padding for the tk boxes 
for widget in party_hire_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#Submit Button
button_add= tkinter.Button(party_hire_frame, text = "Submit Data",command=lambda: add_data())
button_add.grid(row=5,column = 1)

#Delete Button
button_delete= tkinter.Button(party_hire_frame, text = "Delete Data",command=lambda: delete())
button_delete.grid(row=5,column = 2)


#creating a table frame for the treeview table 
table_frame=tkinter.Frame(window)
table_frame.pack(pady=10)
#defining the column names  
columns = ("Customer Name", "Receipt Number", "Hired Item", "Amount Hired")
treeview = ttk.Treeview(table_frame, columns=columns, show="headings")
treeview.pack(side=tkinter.LEFT)


#adjusting column sizes
treeview.column("Customer Name", width=200)
treeview.column("Receipt Number", width=200)
treeview.column("Hired Item", width=200)
treeview.column("Amount Hired", width=200)

#headings 
for col in columns:
    treeview.heading(col,text=col)




#defining the clear function (what it should do)
def clear_entry_boxes():
    Customer_entry.delete(0, tkinter.END)
    Receipt_entry.delete(0, tkinter.END)
    hired_item_entry.delete(0, tkinter.END)
    Number_hired_combobox.set('')


#Defining data to submit it 
def add_data():

    #Information
    Name = Customer_entry.get()
    Receipt = Receipt_entry.get()
    Item = hired_item_entry.get()
    Amount = Number_hired_combobox.get()

    #Check if Name is empty
    if Name == "":
        messagebox.showwarning("Error",message="Please enter a name.")
        return

    # Check if Name contains only letters
    if not Name.replace(" ", "").isalpha():
        messagebox.showwarning("Error", message="Please enter a valid name using letters only.")
        return

    #Check if Receipt is empty
    if Receipt == "":
        messagebox.showwarning("Error",message="Please enter a receipt number.")
        return

    #Check if Receipt Number is a valid number
    try:
        Receipt = int(Receipt)
    except ValueError:
        messagebox.showwarning("Error",message="Please enter a valid Receipt Number.")
        return

    #Check if Item is empty
    if Item == "":
        messagebox.showwarning("Error",message="Please enter an item.")
        return

        # Check if Hired Item contains only Letters
    if not Item.replace(" ", "").isalpha():
        messagebox.showwarning("Error", message="Please enter a valid Item using letters only.")
        return

    # Check if Amount is within the desired range
    try:
        Amount = int(Amount)
        if Amount < 1 or Amount > 500:
            messagebox.showwarning("Error", message="Please enter a value between 1 and 500.")
            return False
    #Check if amount is a proper integer 
    except ValueError:
        messagebox.showwarning("Error", message="Please enter a valid amount.")
        return False

    #Insert data inside the table 
    treeview.insert("", index="end", values=(Name, Receipt, Item, Amount))

    #run the variable "clear_data()" once submit button is clicked
    clear_entry_boxes()



#Delete the selected data
def delete():
   # Get selected item to Delete
   selected_item = treeview.selection()[0]
   treeview.delete(selected_item)


#loop so the code will run 
window.mainloop()