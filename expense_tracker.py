expenses = []
while True:
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "4":
        break
    elif choice == "1":
        description = input("Enter a description: ")
        amount = float(input("Enter the amount: "))
        category = input("Enter a category: ")
        expense = {"description": description, "amount": amount, "category": category }
        expenses.append(expense)
        print("Expense added!")
    elif choice == "2":
        for expense in expenses:
            expense["description"]
            expense["amount"]
            expense["category"]
            print(f"Description: {expense['description']}")
            print(f"Amount: {expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Total spent: {total:.2f}")
        
print("Program ended")