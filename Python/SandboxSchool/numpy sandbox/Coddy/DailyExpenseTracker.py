print("Welcome to the Daily Expense Tracker!\n")

isRunning = True
expenses = []

# menu display
def display_menu():
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")

# calculate total of the list passed in
def calc_total(lyst):
    total_sum = 0

    for i in lyst:
        total_sum += i
    return total_sum

# calculate average expenses
def avg_expense(lyst):
    return calc_total(lyst) / len(lyst)

# add a new expense
def add_expense(amount_spent):
    expenses.append(amount_spent)

# view expenses
def view_expenses():
    count = 0
    print("Your expenses:")
    for expense in expenses:
        print(f"{count+1}. {expense}")
        count += 1

# clear all expenses
def clear_all_expenses():
    expenses.clear()

display_menu()
while isRunning:
    user_input = int(input())

    while user_input < 1 or user_input > 5:
        print("Invalid choice. Please try again.")
        user_input = int(input())

    if user_input == 1:
        amount = float(input())
        add_expense(amount)
        print("Expense added successfully!")
    elif user_input == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            view_expenses()
    elif user_input == 3:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print(f"Total expense: {calc_total(expenses)}")
            print(f"Average expense: {avg_expense(expenses)}")
    elif user_input == 4:
        clear_all_expenses()
        print("All expenses cleared.")

    if user_input == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        isRunning = False