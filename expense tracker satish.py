import datetime

class Expense:
    def __init__(self, amount, description, category):
        self.date = datetime.date.today()
        self.amount = amount
        self.description = description
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.categories.add(expense.category)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}, Category: {expense.category}")

    def view_category_expenses(self, category):
        for expense in self.expenses:
            if expense.category == category:
                print(f"Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}, Category: {expense.category}")

    def view_monthly_summary(self):
        current_month = datetime.date.today().month
        monthly_expenses = [expense for expense in self.expenses if expense.date.month == current_month]
        total_expenses = sum([expense.amount for expense in monthly_expenses])
        print(f"Total Expenses in {datetime.date.today().strftime('%B')}: {total_expenses}")

    def view_category_wise_summary(self):
        current_month = datetime.date.today().month
        monthly_expenses = [expense for expense in self.expenses if expense.date.month == current_month]
        category_wise_expenses = {}
        for expense in monthly_expenses:
            if expense.category in category_wise_expenses:
                category_wise_expenses[expense.category] += expense.amount
            else:
                category_wise_expenses[expense.category] = expense.amount
        for category, amount in category_wise_expenses.items():
            print(f"Category: {category}, Expenses: {amount}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Category Expenses")
        print("4. View Monthly Summary")
        print("5. View Category-wise Summary")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            expense = Expense(amount, description, category)
            tracker.add_expense(expense)
        elif choice == 2:
            tracker.view_expenses()
        elif choice == 3:
            category = input("Enter category: ")
            tracker.view_category_expenses(category)
        elif choice == 4:
            tracker.view_monthly_summary()
        elif choice == 5:
            tracker.view_category_wise_summary()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()