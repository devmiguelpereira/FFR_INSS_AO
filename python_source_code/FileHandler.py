import csv
import os

import FileLayout as fl
import pandas as pd

file_path = 'november_inss_2022.csv'

# imports data from a csv file


def import_from_file(file_path):
    error_messages = {
        FileNotFoundError: f"Error: file {file_path} not found.",
        csv.Error: f"Error reading CSV file {file_path}: %s",
        pd.errors.ParserError: f"Error reading Excel file {file_path}: %s",
        Exception: f"Error reading file {file_path}: %s",
        KeyError: f"Error: header row not found in {file_path}."
    }

    if not os.path.isfile(file_path):
        print(error_messages[FileNotFoundError])
        return None

    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.csv':
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                headers = next(reader)  # skip the header row
                employee_data_list = [row for row in reader]
            return employee_data_list
        except tuple(error_messages.keys()) as e:
            print(error_messages[type(e)] % str(e))
        except Exception as e:
            print(error_messages[Exception] % str(e))

    elif file_extension in ('.xlsx', '.xls'):
        try:
            with pd.ExcelFile(file_path, engine='openpyxl') as xls:
                sheet_name = xls.sheet_names[0]
                employee_data = pd.read_excel(xls, sheet_name)
                employee_data_list = employee_data.values.tolist()
            return employee_data_list
        except tuple(error_messages.keys()) as e:
            print(error_messages[type(e)] % str(e))
        except Exception as e:
            print(error_messages[Exception] % str(e))

    else:
        print(f"Error: file {file_path} is not a CSV or Excel file.")
        return None



def create_file():
    # imports employee data from a CSV file
    employee_data_list = import_from_file()

    # handle errors during data import
    if employee_data_list is None:
        print("Error importing employee data. File may be empty or malformed.")
        return

    # write employee data to a file
    file_name = fl.File_name() + ".txt"
    with open(file_name, "w+") as file:
        file.write(fl.Header() + "\n")
        for employee_data in employee_data_list:
            file.write(fl.employee_remunaration_details(employee_data) + "\n")
            print(f"{employee_data[1]} was recorded in file with INSS standards.\n")
        file.write(fl.finalization_of_file_information())
        print(f"File {file_name} successfully created.")
