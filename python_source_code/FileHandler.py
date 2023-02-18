import os
import csv
import FileLayout as fl

file_path = 'november_inss_2022.csv'

# imports data from a csv file


def import_from_file(file_path):
    employee_data_list = []

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            headers = next(reader)  # skip the header row
            for row in reader:
                employee_data_list.append(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except csv.Error as e:
        print(f"Error reading CSV file {file_path}: {e}")
        return None

    if not employee_data_list:
        print(f"No employee data found in file {file_path}")
        return None

    return employee_data_list



def create_file():
    # imports employee data from a CSV file
    employee_data_list = importFromFile()

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
