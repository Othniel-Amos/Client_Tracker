import time
import functions
import copy
from functions import check_if_dict_empty

DATA_FILE = "data_values.csv"
functions.csv_exists(DATA_FILE)
field_service = functions.csv_to_dict(DATA_FILE)

print("This is the field service app:")
print("Use this to keep track of your clients")
choice = ""

while choice != "6":

    #Prevents a lot of issues by blocking some options if the record is empty
    if not check_if_dict_empty(field_service):
        print("The record is empty so limited options available")
        choice = input("Add(4), Quit(6): ").strip()
        if choice in ["1","2","3","5"]:
            print("ERROR:These numbers cannot be accepted")
            continue
    else:
        choice = input("Edit (1), View (2), Delete(3), Add(4), Search(5), Quit(6): ").strip()

    #Add function
    if choice == "1":
        functions.display(field_service)
        date_edit = input("Please enter the date you would like to edit:")
        #Searches for the date in the larger dictionary
        try:
            temp_field_service,index,found = functions.search(field_service,date_edit)
        except Exception as exception:
            done = False
        else:
            functions.display(temp_field_service)
            done = True

        while done:
            print("Date (1), Hours (2), Student (3), Notes (4)")
            var_to_edit = int(input("Please select the number you wish to edit:"))

            #find the specific key value correlating to the choice the user selected in var_to_edit
            word = list(temp_field_service.keys())[var_to_edit-1]

            change = input(f"Change {str(temp_field_service[word]).strip("''[]")} to...")


            temp_field_service_2 = copy.deepcopy(temp_field_service)
            temp_field_service_2[word][0] = str(change)

            valid,error_message = functions.validate_dict(temp_field_service_2)

            if valid:
                temp_field_service = temp_field_service_2
                functions.update_dict_temp(field_service, temp_field_service, index)
            else:
                print(f"ERROR:{error_message} in {change}")
                if var_to_edit == 1:
                    print("Valid date format:DD/MM/YYYY")
                else:
                    print("Hours must be in a numerical value")
                    print("Example:34")

            done = input("Would you like to edit this date again (Y/N):")
            if done == "N":
                done = False


        #Updates the field service dict





    elif choice == "2":
        functions.display(field_service)

    #Deletion choice
    elif choice == "3":
        date_edit = input("Please enter the date you would like to delete:")
        try:
            temp_field_service,index,found = functions.search(field_service,date_edit)
        except TypeError:
            print(f"{date_edit} does not exist in the records\n")
        else:
            functions.display(temp_field_service)
            choice = input("Please confirm the deletion protocol (Y/N):")

            if choice == "Y":
                for key in field_service.keys():
                    del field_service[key][index]
            print("Deletion was successful")

    elif choice == "4":
        add_again = True

        while add_again:
            temp_field = []
            temp_field_dict = {"Date":[],"Hours":[],"Student":[],"Notes":[]}
            current_date = input("Please input date or type 'Y' to input current date:")
            if current_date == "Y":
                current_date = time.strftime("%d/%m/%Y")

            temp_field.append(current_date)

            questions = ["Number of Hours:","Student Name:","Notes:"]


            for question in questions:
                add_it = input(f"{question}")
                temp_field.append(add_it)

            for index, key in enumerate(field_service.keys()):
                temp_field_dict[key] = temp_field[index]

            valid,error_message = functions.validate_dict(temp_field_dict)
            if valid:
                #Adds the values to the field_service dictionary
                for index, key in enumerate(field_service.keys()):
                    field_service[key].append(temp_field[index])
            else:
                print(f"{error_message}")

            add_again = input("Would you like to add again (Y/N):").strip().upper()

            if add_again == "Y":
                add_again = True
            else:
                add_again = False

    elif choice == "5":
        #Searches the dictionary for all values
        print("Date (1), Hours (2), Student (3), Notes (4)")
        var_to_search = ""

        while type(var_to_search) != int:
            try:
                var_to_search = int(input("Please select the number you wish to search by:").strip())
            except:
                print("Please enter an integer value")


        while var_to_search not in [1,2,3,4]:
            print("ERROR:Invalid variable")
            var_to_search = int(input("Please select the number you wish to search by:"))

        search_again = False
        search_value = input("Please enter the searchable value:").strip()
        if var_to_search == 1:
            temp_field_service, index, found = functions.search(field_service,search_value,"Date",False)
        elif var_to_search == 2:
            temp_field_service, index, found = functions.search(field_service,search_value,"Hours",True)
        elif var_to_search == 3:
            temp_field_service, index, found = functions.search(field_service,search_value,"Student",True)
        else:
            temp_field_service, index, found= functions.search(field_service,search_value,"Notes",True)

        #Checks if to display the field or not

        if found and var_to_search == 1:
            functions.display(temp_field_service)
        elif found:
            [functions.display(dict_iter) for dict_iter in temp_field_service]
        else:
            print(f"{search_value} was not found")

    elif choice != "6":
        print("Please enter a valid number")


    functions.dict_to_csv(field_service,DATA_FILE)



























