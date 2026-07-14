class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self,description,amount):
        expense = Expense(description,amount)
        self.expenses.append(expense)    

    def show_expenses(self):
        return self.expenses

    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total   