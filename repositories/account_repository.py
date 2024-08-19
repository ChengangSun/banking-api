from utils.exceptions import DuplicateAccountError

class Account:
    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance

class Transaction:
    def __init__(self, from_account_id: str, to_account_id: str, amount: float):
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id
        self.amount = amount

class AccountRepository:
    def __init__(self):
        self.accounts = {}
        self.transactions = {}

    def create_account(self, account_id: str, initial_balance: float):
        if account_id in self.accounts:
            raise DuplicateAccountError(f"Account with ID {account_id} already exists.")
        self.accounts[account_id] = Account(account_id, initial_balance)
        self.transactions[account_id] = []

    def get_account(self, account_id: str):
        return self.accounts.get(account_id)

    def transfer_funds(self, from_account_id: str, to_account_id: str, amount: float):
        from_account = self.accounts[from_account_id]
        to_account = self.accounts[to_account_id]

        from_account.balance -= amount
        to_account.balance += amount

        transaction = Transaction(from_account_id, to_account_id, amount)
        self.transactions[from_account_id].append(transaction)
        self.transactions[to_account_id].append(transaction)

    def get_transaction_history(self, account_id: str):
        return self.transactions.get(account_id, [])
