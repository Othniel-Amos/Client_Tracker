import pandas as pd
from pandas import DataFrame
import os

def display(database):
    '''Displays the values of a dictionary in a field service format'''
    for index, day in enumerate(database["Date"]):
        print(f"Day:{database["Date"][index]}")
        print(f"Number of hours:{database["Hours"][index]}")
        print(f"Student:{database["Student"][index]}")
        print(f"Notes:{database["Notes"][index]}")
        print("\n")

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

def initalize(datafile):
    if __name__ != "__main__":
        if os.path.exists(datafile):
            pass
            return True
        else:
            with open(datafile, "w") as file:
                file.write("Date,Hours,Student,Notes")
            return False
































