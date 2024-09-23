# Tests/test_finance_manager.py

import unittest
from finance_manager import add_transaction, view_transactions, delete_transaction

class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        # Set up a fresh environment for each test
        self.transactions = []

    def test_add_valid_transaction(self):
        # Test adding a valid transaction
        add_transaction(self.transactions, '2024-09-23', 'Salary', 1000.0, 'income')
        self.assertEqual(len(self.transactions), 1)
        self.assertEqual(self.transactions[0]['description'], 'Salary')
        self.assertEqual(self.transactions[0]['amount'], 1000.0)
        self.assertEqual(self.transactions[0]['type'], 'income')

    def test_add_transaction_missing_description(self):
        # Test adding a transaction with missing description
        with self.assertRaises(ValueError):
            add_transaction(self.transactions, '2024-09-23', '', 1000.0, 'income')

    def test_add_transaction_invalid_amount(self):
        # Test adding a transaction with invalid amount
        with self.assertRaises(ValueError):
            add_transaction(self.transactions, '2024-09-23', 'Groceries', 'invalid_amount', 'expense')

    def test_view_transactions(self):
        # Test viewing all transactions
        add_transaction(self.transactions, '2024-09-23', 'Salary', 1000.0, 'income')
        add_transaction(self.transactions, '2024-09-24', 'Groceries', -50.0, 'expense')
        result = view_transactions(self.transactions)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['description'], 'Salary')
        self.assertEqual(result[1]['description'], 'Groceries')

    def test_delete_existing_transaction(self):
        # Test deleting an existing transaction
        add_transaction(self.transactions, '2024-09-23', 'Salary', 1000.0, 'income')
        result = delete_transaction(self.transactions, 'Salary')
        self.assertTrue(result)
        self.assertEqual(len(self.transactions), 0)

    def test_delete_nonexistent_transaction(self):
        # Test deleting a transaction that does not exist
        add_transaction(self.transactions, '2024-09-23', 'Salary', 1000.0, 'income')
        result = delete_transaction(self.transactions, 'Groceries')
        self.assertFalse(result)
        self.assertEqual(len(self.transactions), 1)

    def test_delete_from_empty_list(self):
        # Test deleting from an empty transaction list
        result = delete_transaction(self.transactions, 'Nonexistent')
        self.assertFalse(result)
        self.assertEqual(len(self.transactions), 0)

    def test_view_empty_transactions(self):
        # Test viewing transactions when the list is empty
        result = view_transactions(self.transactions)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
