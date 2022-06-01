'''
This program asks for the customer's full name, receipt number, the item hired,
and the quantity hired and prints it on a GUI. The program also gives the option
to delete a chosen row when a customer returns an item.
'''

# import required modules
import tkinter as tk
from tkinter import ttk

# subroutine to quit the program
def quit():
    root.destroy()

# subroutine to check the validity of user input when submitting customer info
def append_check():
    global name_valid, receipt_valid, item_valid, quantity_valid
    
    # check if name is empty
    if name_entry.get() == '':
        name_valid = False

    else:
        name_valid = True

    # check if receipt number is a number
    # (if the field is empty, it will not pass the check)
    if receipt_entry.get().isdigit() == False:
        receipt_valid = False

    else:
        receipt_valid = True

    # check if item is empty
    if item_entry.get() == '':
        item_valid = False

    else:
        item_valid = True

    # check if quantity is a number
    # (if the field is empty, it will not pass the check)
    if quantity_entry.get().isdigit() == False:
        quantity_valid = False

    elif int(quantity_entry.get()) < 1 or int(quantity_entry.get()) > 500:
        quantity_valid = False

    else:
        quantity_valid = True

    # checks each field and displays an error if it is invalid,
    # or clears the error if is it valid

    # checks name
    if name_valid == False:
        name_error = ttk.Label(entry_frame, text='Name cannot be empty')
        name_error.grid(column=1, row=2)

    else:
        name_error = ttk.Label(entry_frame, text='')
        name_error.grid(column=1, row=2)

    # checks receipt number
    if receipt_valid == False:
        receipt_error = ttk.Label(entry_frame,
                                  text='Receipt number must only contain numbers')
        receipt_error.grid(column=1, row=4)
        
    else:
        receipt_error = ttk.Label(entry_frame, text='')
        receipt_error.grid(column=1, row=4)

    # checks item
    if item_valid == False:
        item_error = ttk.Label(entry_frame, text='Item cannot be empty')
        item_error.grid(column=1, row=6)

    else:
        item_error = ttk.Label(entry_frame, text='')
        item_error.grid(column=1, row=6)

    # checks quantity
    if quantity_valid == False:
        quantity_error = ttk.Label(entry_frame,
                               text='Quantity must be an integer between 1-500 (inclusive)')
        quantity_error.grid(column=1, row=8)
        
    else:
        quantity_error = ttk.Label(entry_frame, text='')
        quantity_error.grid(column=1, row=8)
        

    # if all fields are valid, append the details
    if [name_valid, receipt_valid, item_valid, quantity_valid] == [True, True, True, True]:
        append_details()

    
# subroutine to append details
def append_details():

    # get information of customer to put into smaller list
    mini_list = [name_entry.get(),
                 receipt_entry.get(),
                 item_entry.get(),
                 quantity_entry.get()]

    # append smaller list into full info list with info of all customers
    info_list.append(mini_list)

    # clear entry fields
    name_entry.delete(0, 'end')
    receipt_entry.delete(0, 'end')
    item_entry.delete(0, 'end')
    quantity_entry.delete(0, 'end')

    # print details on window after appending info to list
    print_details()

# subroutine to print details after appending or deleting
def print_details():

    # loops through each item in info_list
    for i in range(0, len(info_list)):

        # create labels to output info
        row_output = ttk.Label(print_frame, text=str(i))
        row_output.grid(row=i+2, column=0)

        name_output = ttk.Label(print_frame, text=info_list[i][0])
        name_output.grid(row=i+2, column=1)

        receipt_output = ttk.Label(print_frame, text=info_list[i][1])
        receipt_output.grid(row=i+2, column=2)

        item_output = ttk.Label(print_frame, text=info_list[i][2])
        item_output.grid(row=i+2, column=3)

        output_output = ttk.Label(print_frame, text=info_list[i][3])
        output_output.grid(row=i+2, column=4)

# subroutine to check validity of user input when choosing a row to delete
def delete_check():
    global delete_valid, row_to_delete

    # get the chosen row to delete from the delete field
    row_to_delete = delete_entry.get()
    
    # check if input is an integer
    if row_to_delete.isdigit() == False:
        delete_valid = False

    # check if chosen row is not in the list
    elif int(row_to_delete) >= len(info_list):
        delete_valid = False

    else:
        delete_valid = True

    # if input to delete row is invalid, display an error
    if delete_valid == False:
        delete_error = ttk.Label(entry_frame,
                                 text='Chosen row does not exist in list')
        delete_error.grid(column=3, row=4)

    # if input is valid, clear the error and delete details of the chosen row
    else:
        delete_error = ttk.Label(entry_frame, text='')
        delete_error.grid(column=3, row=4)
        delete_details()
        
# subroutine to delete a chosen row
def delete_details():

    # delete the chosen "row" from the list
    info_list.pop(int(row_to_delete))

    # loops through all labels in print_frame
    for label in print_frame.grid_slaves():

        # deletes all labels below the headings
        if int(label.grid_info()['row']) > 1:
                label.destroy()

    # clear the delete entry field
    delete_entry.delete(0, 'end')

    # reprint all the details
    print_details()

# main function
def main():

    global root, entry_frame, print_frame, \
           name_entry, receipt_entry, item_entry, \
           quantity_entry, delete_entry, \
           info_list
    
    # create root window
    root = tk.Tk()

    # create separate frames for entry fields, print/delete buttons,
    # and printed info
    entry_frame = ttk.Frame(root)
    entry_frame['padding'] = (5, 5, 5, 15)
    entry_frame.pack()

    print_frame = ttk.Frame(root)
    print_frame['padding'] = (5, 5, 5, 5)
    print_frame.pack()

    # create list to keep customer information
    info_list = []

    # configure styles
    style = ttk.Style(root)

    style.configure('Heading.TLabel', width=20)

    # create title label for the program
    title_label = ttk.Label(entry_frame, text="Julie's Party Hire")
    title_label.grid(column=0, row=0, columnspan=4)

    # create label for the "enter details" section
    enter_details_label = ttk.Label(entry_frame, text='Enter Details')
    enter_details_label.grid(column=0, row=1, columnspan=4)

    # create labels and entry fields for user to input customer info
    name_label = ttk.Label(entry_frame, text='Customer full name')
    name_label.grid(column=0, row=3)

    name_entry = ttk.Entry(entry_frame)
    name_entry.grid(column=1, row=3)

    receipt_label = ttk.Label(entry_frame, text='Receipt number')
    receipt_label.grid(column=0, row=5)

    receipt_entry = ttk.Entry(entry_frame)
    receipt_entry.grid(column=1, row=5)

    item_label = ttk.Label(entry_frame, text='Item hired')
    item_label.grid(column=0, row=7)

    item_entry = ttk.Entry(entry_frame)
    item_entry.grid(column=1, row=7)

    quantity_label = ttk.Label(entry_frame, text='Quantity hired')
    quantity_label.grid(column=0, row=9)

    quantity_entry = ttk.Entry(entry_frame)
    quantity_entry.grid(column=1, row=9)

    # add buttons to print/delete details and quit program
    print_button = ttk.Button(entry_frame, text='Print Details', command=append_check)
    print_button.grid(column=3, row=3, sticky=tk.E)

    delete_label = ttk.Label(entry_frame, text='Row to delete:')
    delete_label.grid(column=2, row=5, sticky=tk.W)

    delete_entry = ttk.Entry(entry_frame)
    delete_entry.grid(column=3, row=5, sticky=tk.E)

    delete_button = ttk.Button(entry_frame, text='Delete Details', command=delete_check)
    delete_button.grid(column=3, row=7, sticky=tk.E)

    quit_button = ttk.Button(entry_frame, text='Quit', command=quit)
    quit_button.grid(column=3, row=9, sticky=tk.E)

    # create empty labels to display error messages when user input is invalid
    name_error = ttk.Label(entry_frame, text='')
    name_error.grid(column=1, row=2)

    receipt_error = ttk.Label(entry_frame, text='')
    receipt_error.grid(column=1, row=4)

    item_error = ttk.Label(entry_frame, text='')
    item_error.grid(column=1, row=6)

    quantity_error = ttk.Label(entry_frame, text='')
    quantity_error.grid(column=1, row=8)

    delete_error = ttk.Label(entry_frame, text='')
    delete_error.grid(column=3, row=4)

    # create label for the "printed details" section
    printed_details_label = ttk.Label(print_frame, text='Printed Details')
    printed_details_label.grid(column=0, row=0, columnspan=5)
    
    # create headings to print information under
    row_heading = ttk.Label(print_frame, text='Row #', style='Heading.TLabel')
    row_heading.grid(column=0, row=1)
    
    name_heading = ttk.Label(print_frame, text='Customer name', style='Heading.TLabel')
    name_heading.grid(column=1, row=1)

    receipt_heading = ttk.Label(print_frame, text='Receipt number', style='Heading.TLabel')
    receipt_heading.grid(column=2, row=1)

    item_heading = ttk.Label(print_frame, text='Item hired', style='Heading.TLabel')
    item_heading.grid(column=3, row=1)

    quantity_heading = ttk.Label(print_frame, text='Quantity hired', style='Heading.TLabel')
    quantity_heading.grid(column=4, row=1)



    root.mainloop()
    
main()
