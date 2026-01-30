import time
import functions
import copy

DATA_FILE = "data_values.csv"
functions.csv_exists(DATA_FILE)
database_main = functions.csv_to_dict(DATA_FILE)

def main_edit():
    functions.display(database_main)
    date_edit = input("Please enter the date you would like to edit:")
    # Searches for the date in the larger dictionary
    try:
        temp_database_main, index, found = functions.search(database_main, date_edit)
    except Exception as exception:
        found = False
    else:
        if found:
            functions.display(temp_database_main)

    while found:
        print("Date (1), Hours (2), Student (3), Notes (4)")
        try:
            var_to_edit = int(input("Please select the number you wish to edit:").strip())
        except:
            print("Please type an integer value")
        else:
            # find the specific key value correlating to the choice the user selected in var_to_edit
            word = list(temp_database_main.keys())[var_to_edit - 1]

            change = input(f"Change {str(temp_database_main[word]).strip("''[]")} to...")

            temp_database_main_2 = copy.deepcopy(temp_database_main)
            temp_database_main_2[word][0] = str(change).strip("""""")

            valid, error_message = functions.validate_dict(temp_database_main_2)

            if valid:
                temp_database_main = temp_database_main_2
                functions.update_dict_temp(database_main, temp_database_main, index)
            else:
                print(f"ERROR:{error_message} in {change}")
                if var_to_edit == 1:
                    print("Valid date format:DD/MM/YYYY")
                else:
                    print("Hours must be in a numerical value")
                    print("Example:34")

            done = input("Would you like to edit this date again (Y/N):")
            if done == "N":
                found = False

def main_delete():
    date_edit = input("Please enter the date you would like to delete:")
    try:
        temp_database_main, index, found = functions.search(database_main, date_edit)
    except TypeError:
        print(f"{date_edit} does not exist in the records\n")
    else:
        if found:
            functions.display(temp_database_main)
            choice_delete = input("Please confirm the deletion protocol (Y/N):")

            if choice_delete == "Y":
                for key in database_main.keys():
                    del database_main[key][index]
            print("Deletion was successful")
        else:
            print("Unknown error (Date may have not been typed correctly)")

def main_add():
    add_again = True

    while add_again:
        temp_database = []
        temp_database_dict = {"Date": [], "Hours": [], "Student": [], "Notes": []}
        current_date = input("Please input date or type 'Y' to input current date:")
        if current_date == "Y":
            current_date = time.strftime("%d/%m/%Y")

        temp_database.append(current_date)

        questions = ["Number of Hours:", "Student Name:", "Notes:"]

        for question in questions:
            add_it = input(f"{question}")
            temp_database.append(add_it)

        for index, key in enumerate(database_main.keys()):
            temp_database_dict[key] = temp_database[index]

        valid, error_message = functions.validate_dict(temp_database_dict)
        if valid:
            # Adds the values to the database dictionary
            for index, key in enumerate(database_main.keys()):
                database_main[key].append(temp_database[index])
        else:
            print(f"{error_message}")

        add_again = input("Would you like to add again (Y/N):").strip().upper()

        if add_again == "Y":
            add_again = True
        else:
            add_again = False

def main_search():
    # Searches the dictionary for all values
    print("Date (1), Hours (2), Student (3), Notes (4)")
    var_to_search = ""

    while type(var_to_search) != int:
        try:
            var_to_search = int(input("Please select the number you wish to search by:").strip())
        except:
            print("Please enter an integer value")

    while var_to_search not in [1, 2, 3, 4]:
        print("ERROR:Invalid variable")
        var_to_search = int(input("Please select the number you wish to search by:"))

    search_again = True

    while search_again:
        search_value = input("Please enter the searchable value:").strip()
        if var_to_search == 1:
            temp_database_main, index, found = functions.search(database_main, search_value, "Date", False)
        elif var_to_search == 2:
            temp_database_main, index, found = functions.search(database_main, search_value, "Hours", True)
        elif var_to_search == 3:
            temp_database_main, index, found = functions.search(database_main, search_value, "Student", True)
        else:
            temp_database_main, index, found = functions.search(database_main, search_value, "Notes", True)

        # Checks if to display the database or not

        if found and var_to_search == 1:
            functions.display(temp_database_main)
        elif found:
            [functions.display(dict_iter) for dict_iter in temp_database_main]
        else:
            print(f"{search_value} was not found")

        search_again = input("Would you like to search again (Y/N):").strip().upper()

        if search_again == "Y":
            pass
        else:
            [print(f"Invalid parameter in {search_again}") if search_again != "N" else print("Search protocol terminated")]
            search_again = False



def validate_choice():
    global choice
    if not functions.check_if_dict_empty(database_main):
        print("The record is empty so limited options available")
        choice = input("Add(4), Quit(6): ").strip()
        if choice in ["1","2","3","5"]:
            print("ERROR:These numbers cannot be accepted")
            return False
        else:
            return True
    else:
        choice = input("Edit (1), View (2), Delete(3), Add(4), Search(5), Quit(6): ").strip()
        return True

print("This is the client tracker app:")
print("Use this to keep track of your clients")
choice = ""



while choice != "6":

    #Prevents a lot of issues by blocking some options if the record is empty
    if not validate_choice():
        continue

    #Add function
    if choice == "1":
        main_edit()

    elif choice == "2":
        functions.display(database_main)

    #Deletion choice
    elif choice == "3":
        main_delete()

    elif choice == "4":
        main_add()

    elif choice == "5":
        main_search()

    elif choice != "6":
        print("Please enter a valid number")


    functions.dict_to_csv(database_main, DATA_FILE)

print("\nProgram successfully terminated")


























