class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    

    def add_expense(self,description,amount):
        expense = Expense(description,amount)
        self.expenses.append(expense)    


    def print_expenses(self,expense):
        print(f"{expense}")


    def show_expenses(self):
        if len(self.expenses)==0:
            print("-------There are no registred expenses-------")   
        else:
            print("=============================================")
            print("[                 EXPENSES                  ]")
            print("---------------------------------------------")
            for expense in self.expenses:
                expense.print_expenses()


    
               




        