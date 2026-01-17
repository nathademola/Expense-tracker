print("Welcome to Expense Tracker")

expenses = []

while True:
    user_input = input("Enter an expense amount or type 'done' to finish: ")

    if user_input.lower() == "done":
        break

    expense = float(user_input)
    expenses.append(expense)

total = sum(expenses)

print("\nExpense Summary")
print("Expenses:", expenses)
print("Total Spent: ₦", total)