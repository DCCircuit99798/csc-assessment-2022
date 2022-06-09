'''
This program asks for the customer's full name, receipt number, the item hired,
and the quantity hired and prints it on a GUI. The program also gives the option
to delete a chosen row when a customer returns an item.
'''

# import required modules
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# subroutine to quit the program
def quit():

    # create a messagebox
    quit_confirm = messagebox.askquestion('Quit Program', \
                              'Are you sure you want to close the program? Customer info will be lost!', \
                              icon='warning')

    # if user selects yes, quit the program
    if quit_confirm == 'yes':
        root.destroy()

    # if user selects no, don't quit
    else:
        pass
    

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
        name_message.set('Name cannot be empty')

    else:
        name_message.set('')

    # checks receipt number
    if receipt_valid == False:
        receipt_message.set('Receipt number must only contain numbers')
        
    else:
        receipt_message.set('')

    # checks item
    if item_valid == False:
        item_message.set('Item cannot be empty')
        
    else:
        item_message.set('')

    # checks quantity
    if quantity_valid == False:
        quantity_message.set('Quantity must be an integer between 1-500 (inclusive)')
        
    else:
        quantity_message.set('')


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
        delete_message.set('Chosen row does not exist in list')
        
    # if input is valid, clear the error and delete details of the chosen row
    else:
        delete_message.set('')
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
           name_message, receipt_message, item_message, \
           quantity_message, delete_message, \
           info_list
    
    # create root window and set title
    root = tk.Tk()
    root.wm_title("Julie's Party Hire")

    # create separate frames for entry fields, print/delete buttons,
    # and printed info
    entry_frame = ttk.Frame(root)
    entry_frame['padding'] = (5, 5, 5, 20)
    entry_frame.pack()

    print_frame = ttk.Frame(root)
    print_frame['padding'] = (5, 5, 5, 5)
    print_frame.pack()
    

    # create list to keep customer information
    info_list = []

    # configure styles and fonts
    style = ttk.Style(root)

    style.configure('Title.TLabel',
                    font=('Sofia Pro', 24, 'bold'),
                    anchor='center')

    style.configure('Heading1.TLabel', # headings for each frame
                    font=('Verdana', 18),
                    anchor='center')
    
    style.configure('Heading2.TLabel', # heading to print customer info under
                    font=('Tahoma', 13),
                    anchor='center',
                    width=20)

    style.configure('Error.TLabel',
                    font=('Tahoma', 8))

    entry_font = {'font': ('Tahoma', 11)}

    style.configure('TLabel', font=('Tahoma', 11))
    style.configure('TEntry', width=500)
    style.configure('TButton', font=('Tahoma', 11))

    # create title label for the program
    title_label = ttk.Label(entry_frame, text="Julie's Party Hire", style='Title.TLabel')
    title_label.grid(column=0, row=0, columnspan=4)

    # create label for the "enter details" section
    enter_details_label = ttk.Label(entry_frame, text='Enter Details', style='Heading1.TLabel')
    enter_details_label.grid(column=0, row=1, columnspan=4)

    # create labels and entry fields for user to input customer info
    name_label = ttk.Label(entry_frame, text='Customer full name')
    name_label.grid(column=0, row=3)

    name_entry = ttk.Entry(entry_frame, width=35, **entry_font)
    name_entry.grid(column=1, row=3)

    receipt_label = ttk.Label(entry_frame, text='Receipt number')
    receipt_label.grid(column=0, row=5)

    receipt_entry = ttk.Entry(entry_frame, width=35, **entry_font)
    receipt_entry.grid(column=1, row=5)

    item_label = ttk.Label(entry_frame, text='Item hired')
    item_label.grid(column=0, row=7)

    item_entry = ttk.Entry(entry_frame, width=35, **entry_font)
    item_entry.grid(column=1, row=7)

    quantity_label = ttk.Label(entry_frame, text='Quantity hired')
    quantity_label.grid(column=0, row=9)

    quantity_entry = ttk.Entry(entry_frame, width=35, **entry_font)
    quantity_entry.grid(column=1, row=9)

    # create empty label widget to separate entry fields and buttons
    separator_label = ttk.Label(entry_frame, width=5)
    separator_label.grid(column=2, row=2)

    # add buttons to print/delete details and quit program
    print_button = ttk.Button(entry_frame, text='Print Details', command=append_check)
    print_button.grid(column=4, row=3, sticky=tk.E)

    delete_label = ttk.Label(entry_frame, text='Row to delete:')
    delete_label.grid(column=3, row=5, sticky=tk.W)

    delete_entry = ttk.Entry(entry_frame, width=20, **entry_font)
    delete_entry.grid(column=4, row=5, sticky=tk.E)

    delete_button = ttk.Button(entry_frame, text='Delete Details', command=delete_check)
    delete_button.grid(column=4, row=7, sticky=tk.E)

    quit_button = ttk.Button(entry_frame, text='Quit', command=quit)
    quit_button.grid(column=4, row=9, sticky=tk.E)

    # create string variables to configure error messages
    name_message = tk.StringVar(entry_frame, '')
    receipt_message = tk.StringVar(entry_frame, '')
    item_message = tk.StringVar(entry_frame, '')
    quantity_message = tk.StringVar(entry_frame, '')
    delete_message = tk.StringVar(entry_frame, '')

    # create empty labels to display error messages when user input is invalid
    name_error = ttk.Label(entry_frame, textvariable=name_message, style='Error.TLabel')
    name_error.grid(column=1, row=2, sticky=tk.EW)

    receipt_error = ttk.Label(entry_frame, textvariable=receipt_message, style='Error.TLabel')
    receipt_error.grid(column=1, row=4, sticky=tk.EW)

    item_error = ttk.Label(entry_frame, textvariable=item_message, style='Error.TLabel')
    item_error.grid(column=1, row=6, sticky=tk.EW)

    quantity_error = ttk.Label(entry_frame, textvariable=quantity_message, style='Error.TLabel')
    quantity_error.grid(column=1, row=8, sticky=tk.EW)

    delete_error = ttk.Label(entry_frame, textvariable=delete_message, style='Error.TLabel')
    delete_error.grid(column=4, row=4, sticky=tk.EW)

    # create label for the "printed details" section
    printed_details_label = ttk.Label(print_frame, text='Printed Details', style='Heading1.TLabel')
    printed_details_label.grid(column=0, row=0, columnspan=5)
    
    # create headings to print information under
    row_heading = ttk.Label(print_frame, text='Row #', style='Heading2.TLabel')
    row_heading.grid(column=0, row=1)
    
    name_heading = ttk.Label(print_frame, text='Customer name', style='Heading2.TLabel')
    name_heading.grid(column=1, row=1)

    receipt_heading = ttk.Label(print_frame, text='Receipt number', style='Heading2.TLabel')
    receipt_heading.grid(column=2, row=1)

    item_heading = ttk.Label(print_frame, text='Item hired', style='Heading2.TLabel')
    item_heading.grid(column=3, row=1)

    quantity_heading = ttk.Label(print_frame, text='Quantity hired', style='Heading2.TLabel')
    quantity_heading.grid(column=4, row=1)
    

    root.mainloop()
    
main()
