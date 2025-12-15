import datetime as dt
import functions

field_service = {"Date":["05/05/2009","05/06/2007"],"Hours":["30","40"],
                 "Student":["Michael","Marcus"],"Notes":["Listened well","Barely Listened"]}

print("This is the field service app:")
print("Use this to keep track of your clients")
choice = input("Edit (1), View (2), Delete(3): ")

if choice == "1":
    functions.display(field_service)
    date_edit = input("Please enter the date you would like to edit:")
    #Searches for the date in the larger dictionary
    temp_field_service,index = functions.search(field_service,date_edit)

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


    #Updates the field service dict
    functions.update_dict(field_service,temp_field_service,index)


    print(field_service)




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







