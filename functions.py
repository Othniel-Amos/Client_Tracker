def display(database):
    for index, day in enumerate(database["Date"]):
        print(f"Day:{database["Date"][index]}")
        print(f"Number of hours:{database["Hours"][index]}")
        print(f"Student:{database["Student"][index]}")
        print(f"Notes:{database["Notes"][index]}")
        print("\n")
