import csv
import os

import FileLayout as fl
import pandas as pd

import tkinter as tk
from tkinter import filedialog


# Selects a file on the directory
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


# imports data from a csv or excel file
def import_from_file(file_path):

    if not os.path.isfile(file_path):
        print(f"Error: file {file_path} not found.")
        return None

    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.csv':
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                headers = next(reader)  # skip the header row
                employee_data_list = [row for row in reader]
            return employee_data_list
        except FileNotFoundError:
            print(f"Error: file {file_path} not found.")
        except csv.Error as e:
            print(f"Error reading CSV file {file_path}: {e}")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    elif file_extension == '.xlsx' or file_extension == '.xls':
        try:
            employee_data = pd.read_excel(file_path, engine='openpyxl', skiprows=[0])
            employee_data_list = employee_data.values.tolist()
            return employee_data_list
        except FileNotFoundError:
            print(f"Error: file {file_path} not found.")
        except Exception as e:
            print(f"Error reading Excel file {file_path}: {e}")
    else:
        print(f"Error: file {file_path} is not a CSV or Excel file.")
        return None



def create_file(file_path, overwrite=False, verbose=False):

    # imports employee data from a file
    employee_data_list = import_from_file(file_path)

    # handle errors during data import
    if employee_data_list is None:
        print("Error importing employee data. File may be empty or malformed.")
        return

    # check if the output file already exists
    if os.path.isfile(fl.File_name() + ".txt") and not overwrite:
        print("Error: output file already exists. Use the --overwrite option to overwrite the file.")
        return

    # write employee data to a file
    mode = 'w' if overwrite else 'x'
    with open(fl.File_name() + ".txt", mode) as file:
        file.write(fl.Header() + "\n")
        for employee_data in employee_data_list:
            file.write(fl.employee_remunaration_details(employee_data) + "\n")
            if verbose:
                print(f"{employee_data[1]} was recorded in file with INSS standards.")
        file.write(fl.finalization_of_file_information())

    print(f"File {fl.File_name() + '.txt'} successfully created.")

file_path = select_file()