import tkinter as tk
from tkinter import filedialog
import file_import as fi
import file_generator as fg

def open_file_dialog():
    # Create a file dialog to select the Excel file
    filetypes = [('Excel files', '*.xlsx'), ('All files', '*.*')]
    filename = filedialog.askopenfilename(filetypes=filetypes)
    
    # Call the read_excel_data function with the selected file
    if filename:
        try:
            company_dict, responsible_dict, employee_dict = fi.read_excel_data(filename)
            print("Data loaded successfully!")
            # Do something with the data, such as displaying it in a table
            #print(employee_dict)
            fg.create_file(company_dict, responsible_dict, employee_dict)


        except ValueError as e:
            print(f"Error reading Excel file: {str(e)}")
            # Display an error message to the user
            tk.messagebox.showerror("Error", f"Error reading Excel file: {str(e)}")
    
    
def main():
    # Create the GUI window
    root = tk.Tk()
    root.title("Excel Data Reader")
    
    # Create a button to open the file dialog
    open_button = tk.Button(root, text="Open Excel File", command=open_file_dialog)
    open_button.pack(pady=10)
    
    # Start the GUI event loop
    root.mainloop()


main()