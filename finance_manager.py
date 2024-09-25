def add_transaction(transactions, date, description, amount, transaction_type):
    if not description or not isinstance(amount, (int, float)) or amount == 0:
        raise ValueError("Invalid transaction data")

    transaction = {
        "date": date,
        "description": description,
        "amount": float(amount),  # Ensure amount is a float
        "type": transaction_type.lower()  # Lowercase for consistency
    }
    transactions.append(transaction)
    print(f"{transaction_type.capitalize()} added successfully!")
    
def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return transactions

    print("\nTransactions:")
    for idx, transaction in enumerate(transactions):
        print(
            f"{idx + 1}. {transaction['type'].capitalize()} - {transaction['description']} - ${transaction['amount']}")

    return transactions

def delete_transaction(transactions, description):
    for idx, transaction in enumerate(transactions):
        if transaction['description'].lower() == description.lower():
            deleted = transactions.pop(idx)
            print(
                f"Deleted {deleted['type'].capitalize()} of ${deleted['amount']} for {deleted['description']}.")
            return True
    print("Transaction not found.")
    return False

def main():
    transactions = []

    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter Income amount: "))
                description = input("Enter description: ")
                add_transaction(transactions, date, description, amount, 'Income')
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '2':
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter Expense amount: "))
                description = input("Enter description: ")
                add_transaction(transactions, date, description, -abs(amount), 'Expense')  # Negative amount for expenses
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '3':
            view_transactions(transactions)
        elif choice == '4':
            view_transactions(transactions)
            description = input("Enter the transaction description to delete: ")
            if not delete_transaction(transactions, description):
                print("Transaction could not be deleted.")



if __name__ == "__main__":
    main()