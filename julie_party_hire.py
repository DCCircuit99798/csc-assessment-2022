'''
This program asks for the customer's full name, receipt number, the item hired,
and the quantity hired and prints it on a GUI. The program also gives the option
to delete a chosen row when a customer returns an item.
'''

# import required modules
import tkinter as tk
from tkinter import ttk

# create root window
root = tk.Tk()

# create separate frames for entry fields, print/delete buttons,
# and printed info
entry_frame = ttk.Frame(root)
entry_frame.pack()

button_frame = ttk.Frame(root)
button_frame.pack()

print_frame = ttk.Frame(root)
print_frame.pack()

# create title label for the program
title_label = ttk.Label(entry_frame, text="Julie's Party Hire")
title_label.grid(column=0, row=0, columnspan=4)

# create label for the "enter details" section
enter_details_label = ttk.Label(entry_frame, text='Enter Details')
enter_details_label.grid(column=0, row=1, columnspan=4)

# create labels and entry fields for user to input customer info
name_label = ttk.Label(entry_frame, text='Customer full name')
name_label.grid(column=0, row=2)

name_entry = ttk.Entry(entry_frame)
name_entry.grid(column=1, row=2)

receipt_label = ttk.Label(entry_frame, text='Receipt number')
receipt_label.grid(column=0, row=3)

receipt_entry = ttk.Entry(entry_frame)
receipt_entry.grid(column=1, row=3)

item_label = ttk.Label(entry_frame, text='Item hired')
item_label.grid(column=0, row=4)

item_entry = ttk.Entry(entry_frame)
item_entry.grid(column=1, row=4)

quantity_label = ttk.Label(entry_frame, text='Quantity hired')
quantity_label.grid(column=0, row=5)

quantity_entry = ttk.Entry(entry_frame)
quantity_entry.grid(column=1, row=5)

# add buttons to print/delete details and quit program
print_button = ttk.Button(entry_frame, text='Print Details')
print_button.grid(column=3, row=2, sticky=tk.E)

delete_label = ttk.Label(entry_frame, text='Row to delete:')
delete_label.grid(column=2, row=3, sticky=tk.W)

delete_entry = ttk.Entry(entry_frame)
delete_entry.grid(column=3, row=3, sticky=tk.E)

delete_button = ttk.Button(entry_frame, text='Delete Details')
delete_button.grid(column=3, row=4, sticky=tk.E)

quit_button = ttk.Button(entry_frame, text='Quit')
quit_button.grid(column=3, row=5, sticky=tk.E)

root.mainloop()
