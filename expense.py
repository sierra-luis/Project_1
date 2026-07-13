class Expense:
    def __init__(self,description,amount):
        self.description = description 
        self.amount = amount  

    def __str__(self):
        return f"Expense: {self.description} | Amount: ${self.amount:.2f}"