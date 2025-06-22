from dataclasses import dataclass


@dataclass
class Account:
    id: str
    user_id: str
    currency_type: str
    balance: float
