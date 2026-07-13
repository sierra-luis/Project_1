option="0"

while option != "3":
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")

    option = input("Select an action : ( 1 / 2 / 3 ) ")

    match option:
        case "1":
            description= input("Enter the expense's name: ")
            amount= float(input("Enter the expense's amount: "))
            expenses.add_expense(description,amount)
    
        case "2":
            expenses.show_expenses()

        case "3":  
            print("Thanks for using the app, see you next time")

        case _:
            print("The selected option is not valid, enter it again")  



