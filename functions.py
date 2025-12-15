def display(database):
    for index, day in enumerate(database["Date"]):
        print(f"Day:{database["Date"][index]}")
        print(f"Number of hours:{database["Hours"][index]}")
        print(f"Student:{database["Student"][index]}")
        print(f"Notes:{database["Notes"][index]}")
        print("\n")

def search(database,date_edit):
    temp_field_service ={}
    for index, date in enumerate(database["Date"]):
        if date == date_edit:
            for key in database.keys():
                temp_field_service.update({key:[database[key][index]]})
            break
    return temp_field_service,index

def update_dict_temp(database,temp_database,index):
    for key in database.keys():
        add_to = str(temp_database[key])[2:-2]
        database[key][index] = add_to

