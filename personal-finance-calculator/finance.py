class FinanceTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Доход должен быть положительным числом")
        self.incomes.append(amount)

    def add_expense(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Расход должен быть положительным числом")
        self.expenses.append(amount)

    def total_income(self):
        return sum(self.incomes)

    def total_expenses(self):
        return sum(self.expenses)

    def balance(self):
        return self.total_income() - self.total_expenses()
