import pandas as pd
from pandas import DataFrame
from datetime import datetime


def display(database):
    '''Displays the values of a dictionary in a field service format'''
    for index, day in enumerate(database["Date"]):
        print(f"Day:{database["Date"][index]}")
        print(f"Number of hours:{database["Hours"][index]}")
        print(f"Student:{database["Student"][index]}")
        print(f"Notes:{database["Notes"][index]}")
        print("\n", end = "")

def search(database,date_edit):
    '''Searches a dictionary based on the date given'''
    try:
        temp_field_service ={}
        corrupt = True
        for index, date in enumerate(database["Date"]):
            if date == date_edit:
                for key in database.keys():
                    temp_field_service.update({key:[database[key][index]]})
                    corrupt = False
                break
        if corrupt:
            raise KeyError
    except KeyError:
        print("ERROR INVALID DATE:The date may not have been typed correctly")
    else:
        return temp_field_service, index

def update_dict_temp(database,temp_database,index):
    '''Updates a dictionary based on the values of another dictionary'''
    for key in database.keys():
        add_to = str(temp_database[key])[2:-2]
        database[key][index] = add_to

def csv_to_dict(datafile):
    """Converts a csv file to a dictionary"""
    df = pd.read_csv(datafile)
    database = df.to_dict(orient="list")
    return database

def dict_to_csv(database,datafile):
    """Converts a dictionary to a csv file (Used after altering the dictionary)"""
    df = pd.DataFrame(database)
    df.to_csv(datafile, index=False)

def check_if_dict_empty(database):
    if any(database.values()):
        return True
    else:
        return False

def validate_dict(database):
    '''Validates if the user is using the right type of values'''
    error_message = ""
    valid = True

    for key,value in database.items():
        for value_iter in value:
            value = str(value).strip("''[]")
            if key == "Date":
                try:
                    datetime.strptime(value, "%d/%m/%Y" )
                except:
                    error_message = "Invalid date format"
                    valid = False
                    break
            elif key == "Hours":
                try:
                    float(value)
                except:
                    error_message = "Invalid hour format"
                    valid = False
                    break

    return valid,error_message
































