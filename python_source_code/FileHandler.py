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
    # tries to Open or creates a txt file write the data collected
    _EmployeesData = importFromFile()

    print(type(_EmployeesData))

    file = open(fl.File_name()+".txt", "w+")

    file.write(fl.Header()+"\n")

    for Employee in _EmployeesData:
        # print(Employee,"Employee Data \n")

        file.write(fl.employee_remunaration_details(Employee)+"\n")
        print(Employee[1] +" was recorded in file with inss standards \n")

    file.write(fl.finalization_of_file_information())