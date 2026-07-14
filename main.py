option="0"

while option != "3":
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Calculate Total Spent")
    print("4. Exit")

    option = input("Select an action : ( 1 / 2 / 3 / 4 ) ")

    match option:
        case "1":
            description= input("Enter the expense's name: ")
            amount= float(input("Enter the expense's amount: "))
            expenses.add_expense(description,amount)
    
        case "2":
            expenses.show_expenses()
            print("=============================================")
            print("[                 EXPENSES                  ]")
            print("---------------------------------------------")
            if len(expenses) <=0: 
                print("There are no expenses yet") 
            else: 
                for expense in expenses: 
                    print(expense)

        case "3":  
            expenses.calculate_total()
            print(total)

        case "4":
            print("Thanks for using the app, see you next time")

        case _:
            print("The selected option is not valid, enter it again")  