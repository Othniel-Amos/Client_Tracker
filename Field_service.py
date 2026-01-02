import time
import functions
import pandas as pd

DATA_FILE = "data_values.csv"
field_service = functions.csv_to_dict(DATA_FILE)

print("This is the field service app:")
print("Use this to keep track of your clients")
choice = ""

while choice != "5":
    choice = input("Edit (1), View (2), Delete(3), Add(4), Quit(5): ").strip()

    if choice == "1":
        functions.display(field_service)
        date_edit = input("Please enter the date you would like to edit:")
        #Searches for the date in the larger dictionary
        try:
            temp_field_service,index = functions.search(field_service,date_edit)
        except:
            done = False
        else:
            functions.display(temp_field_service)
            done = True

        while done:
            print("Date (1), Hours (2), Student (3), Notes (4)")
            var_to_edit = int(input("Please select the number you wish to edit:"))

            #find the specific key value correlating to the choice the user selected in var_to_edit
            word = list(temp_field_service.keys())[var_to_edit-1]

            change = input(f"Change {str(temp_field_service[word])[2:-2]} to...")
            temp_field_service[word][0] = str(change)
            done = input("Would you like to edit this date again (Y/N):")
            if done == "N":
                done = False
            functions.update_dict_temp(field_service, temp_field_service, index)


        #Updates the field service dict





    elif choice == "2":
        functions.display(field_service)

    elif choice == "3":
        date_edit = input("Please enter the date you would like to delete:")
        temp_field_service,index = functions.search(field_service,date_edit)
        functions.display(temp_field_service)
        choice = input("Please confirm the deletion protocol (Y/N):")

        if choice == "Y":
            for key in field_service.keys():
                del field_service[key][index]


        print("Deletion was successful")

    elif choice == "4":
        temp_field = []
        current_date = input("Please input date or type 'Y' to input current date:")
        if current_date == "Y":
            current_date = time.strftime("%d/%m/%Y")

        temp_field.append(current_date)

        questions = ["Number of Hours:","Student Name:","Notes:"]

        for question in questions:
            add_it = input(f"{question}")
            temp_field.append(add_it)

        #Adds the values to the field_service dictionary
        for index, key in enumerate(field_service.keys()):
            field_service[key].append(temp_field[index])

    elif choice != 5:
        print("Please enter a valid number")


    functions.dict_to_csv(field_service,DATA_FILE)














