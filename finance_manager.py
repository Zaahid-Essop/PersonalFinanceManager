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