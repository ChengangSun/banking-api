from repositories.account_repository import AccountRepository
from utils.exceptions import InsufficientFundsError, AccountNotFoundError

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, account_id: str, initial_balance: float):
        self.account_repository.create_account(account_id, initial_balance)

    def transfer_funds(self, from_account_id: str, to_account_id: str, amount: float):
        from_account = self.account_repository.get_account(from_account_id)
        to_account = self.account_repository.get_account(to_account_id)
        
        # Raise error if the from_account is not found
        if from_account is None:
            raise AccountNotFoundError(f"Account with ID {from_account_id} not found.")
        
        # Raise error if the to_account is not found
        if to_account is None:
            raise AccountNotFoundError(f"Account with ID {to_account_id} not found.")

        if from_account.balance < amount:
            raise InsufficientFundsError(f"Insufficient funds in account with ID {from_account_id}.")

        self.account_repository.transfer_funds(from_account_id, to_account_id, amount)

    def get_transaction_history(self, account_id: str):
        account = self.account_repository.get_account(account_id)

        if account is None:
            raise AccountNotFoundError(f"Account with ID {account_id} not found.")
        
        return self.account_repository.get_transaction_history(account_id)
