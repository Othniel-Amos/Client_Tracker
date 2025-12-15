import datetime as dt
import functions
temp_field_service = {}

field_service = {"Date":["05/05/2009","05/06/2007"],"Hours":[30,40],
                 "Student":["Michael","Marcus"],"Notes":["Listened well","Barely Listened"]}

print("This is the field service app:")
choice = input("Edit (1) or View (2): ")

if choice == "1":
    functions.display(field_service)
    date_edit = input("Please enter the date you would like to edit:")
    for index, date in enumerate(field_service["Date"]):
        if date == date_edit:
            for key in field_service.keys():
                temp_field_service.update({key:[field_service[key][index]]})
            break
    print(temp_field_service)


elif choice == "2":
    functions.display(field_service)

