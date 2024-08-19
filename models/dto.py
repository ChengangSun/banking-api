from dataclasses import dataclass

@dataclass
class CreateAccountDTO:
    account_id: str
    initial_balance: float

@dataclass
class TransferFundsDTO:
    from_account_id: str
    to_account_id: str
    amount: float
