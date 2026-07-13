class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self,description,amount):
        expense = Expense(description,amount)
        self.expenses.append(expense)    

    def show_expenses(self):
        if len(self.expenses)==0:
            print("-------There are no registred expenses-------")   
        else:
            print("=============================================")
            print("[                 EXPENSES                  ]")
            print("---------------------------------------------")
            for expense in self.expenses:
                print(f"Expense:{expense.description}  Amount: ${expense.amount:.2f}")

    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        print(f"The expense's total is ${total:.2f}")    