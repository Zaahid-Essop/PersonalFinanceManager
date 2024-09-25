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
    
