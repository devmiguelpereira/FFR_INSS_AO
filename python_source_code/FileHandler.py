import os
import csv
import FileLayout as fl

file_path = 'november_inss_2022.csv'

# imports data from a csv file


def importFromFile(file_path=file_path):
    set = []

    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        valueLines = csv.reader(csvfile, delimiter=',')
        for line in valueLines:
            set.append(line)

    #set.pop(0)  # deleting the first line with headers

    return set


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