import pandas as pd
import os
from datetime import datetime


def display(database):
    """Displays the values of a dictionary in a readable format"""
    index = 0
    for day in database["Date"]:
        print(f"Day:{database["Date"][index]}")
        print(f"Number of hours:{database["Hours"][index]}")
        print(f"Student:{database["Student"][index]}")
        print(f"Notes:{database["Notes"][index]}")
        print("\n", end = "")
        index += 1

def search(database,date_edit,dict_key="Date",multiple=False):
    """Searches a dictionary based on the date given.
    It can also search by using other parameters of the dictionary:
    'Hours', 'Students' & 'Notes'.
    With multiple set to false it will return only the last instance of the specified searchable
    (this isn't a problem for dates as dates are expected to be unique and never repeat)."""
    try:
        temp_field_service ={}
        dict_list = []
        found = False
        corrupt = True

        for index, date in enumerate(database[dict_key]):
            temp_field_service = {}
            if dict_key == "Hours":
                date = int(date)
                date_edit = int(date_edit)

            if date == date_edit:
                for key in database.keys():
                    temp_field_service.update({key: [database[key][index]]})
                    corrupt = False

                if dict_key == "Date":
                    break
                if multiple:
                    dict_list.append(dict(temp_field_service))
        if corrupt:
            raise KeyError
    except KeyError:
        print(f"ERROR INVALID {dict_key.upper()}:The {dict_key.upper()} may not have been typed correctly")
        return temp_field_service, index, found
    else:
        found = True
        if multiple:
            return dict_list, index, found
        else:
            return temp_field_service, index,found

def update_dict_temp(database,temp_database,index):
    """Updates a dictionary based on the values of another dictionary
    (It will add a temporary dictionary to the main dictionary)"""
    for key in database.keys():
        add_to = str(temp_database[key]).strip("''[]")
        database[key][index] = add_to

def csv_to_dict(datafile):
    """Converts a csv file to a dictionary
    (This'll be a nested dictionary with keys and lists as values)"""
    df = pd.read_csv(datafile)
    database = df.to_dict(orient="list")
    return database

def dict_to_csv(database,datafile):
    """Converts a dictionary to a csv file (used after altering the dictionary)"""
    df = pd.DataFrame(database)
    df.to_csv(datafile, index=False)

def check_if_dict_empty(database):
    """Checks if a dictionary is empty and returns true or false"""
    if any(database.values()):
        return True
    else:
        return False

def validate_dict(database):
    """Validates if the user is using the right type of values"""
    error_message = ""
    valid = True

    for key,value in database.items():
        if len(value) <= 1 or type(value) == str:
            value = str(value).strip("''[]")
            if key == "Date":
                try:
                    datetime.strptime(value, "%d/%m/%Y")
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
        else:
            for value_iter in value:
                value_iter = str(value_iter).strip("''[]")
                if key == "Date":
                    try:
                        datetime.strptime(value_iter, "%d/%m/%Y" )
                    except:
                        error_message = "Invalid date format"
                        valid = False
                        break
                elif key == "Hours":
                    try:
                        float(value_iter)
                    except:
                        error_message = "Invalid hour format"
                        valid = False
                        break

    return valid,error_message

def csv_exists(datafile):
    """Check if a csv file exist and if not it is created"""
    if os.path.exists(datafile):
        pass
    else:
        with open(datafile,"w") as file:
            file.write("Date,Hours,Student,Notes")































