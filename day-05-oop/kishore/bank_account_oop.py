"""
Day 5 - OOP Practice - Kishore Kumar M R - Bank Account theme
Classes build cumulatively: Account -> SavingsAccount -> PremiumSavingsAccount
Run this file directly to see all "check yourself" demonstrations print out.
"""
from abc import ABC, abstractmethod
from typing import Final, final


# ---------------------------------------------------------------------------
# Exercise 1: self, __init__, class attribute vs instance attribute
# ---------------------------------------------------------------------------
class Account:
    total_accounts = 0  # class attribute - shared across every account

    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance  # Ex3: private from the start
        Account.total_accounts += 1

    # -----------------------------------------------------------------
    # Exercise 2: @classmethod factory vs @staticmethod validator
    # -----------------------------------------------------------------
    @classmethod
    def from_dict(cls, data: dict):
        """Alternate constructor - builds an Account from a dict payload."""
        return cls(data["id"], data.get("balance", 0))

    @staticmethod
    def validate_upi_id(upi: str) -> bool:
        """Pure validation - checks the UPI id has an '@' separator."""
        return isinstance(upi, str) and "@" in upi

    # -----------------------------------------------------------------
    # Exercise 3: Encapsulation - private balance, read-only property,
    # mutated only through deposit/withdraw (never a direct setter)
    # -----------------------------------------------------------------
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amt
        return self.__balance

    def withdraw(self, amt):
        if amt <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amt > self.__balance:
            raise InsufficientFundsError(f"Cannot withdraw {amt}, balance is only {self.__balance}")
        self.__balance -= amt
        return self.__balance

    # -----------------------------------------------------------------
    # Exercise 9: Final constant + @final method
    # -----------------------------------------------------------------
    MIN_BALANCE: Final[float] = 0.0

    @final
    def freeze(self):
        print(f"Account {self.id} frozen (this method cannot be overridden)")

    # -----------------------------------------------------------------
    # Exercise 8: dunder methods - Account itself isn't naturally
    # sortable by one field, so this is done on Transaction instead
    # (matches the PDF's instruction to use a "small Transaction class")
    # -----------------------------------------------------------------
    def __repr__(self):
        return f"Account(id={self.id!r}, balance={self.balance})"


# ---------------------------------------------------------------------------
# Exercise 4: single inheritance + super()
# ---------------------------------------------------------------------------
class SavingsAccount(Account):
    def __init__(self, id, balance, rate):
        super().__init__(id, balance)
        self.interest_rate = rate


# ---------------------------------------------------------------------------
# Exercise 5: multilevel inheritance (3-level chain)
# ---------------------------------------------------------------------------
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, id, balance, rate, bonus_rate):
        super().__init__(id, balance, rate)
        self.bonus_rate = bonus_rate


# ---------------------------------------------------------------------------
# Exercise 6: multiple inheritance via mixin + MRO
# ---------------------------------------------------------------------------
class AuditMixin:
    """Behaviour-only mixin - independent of Account's internal state."""
    def audit_log(self):
        print(f"[AUDIT] account {self.id} balance={self.balance}")


class AuditedSavings(SavingsAccount, AuditMixin):
    pass


# ---------------------------------------------------------------------------
# Exercise 7: abstraction, overriding, duck typing
# ---------------------------------------------------------------------------
class AbstractAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        ...


class FixedRateAccount(AbstractAccount):
    def __init__(self, balance, rate):
        self.balance = balance
        self.rate = rate

    def calculate_interest(self):
        return self.balance * self.rate


class TieredRateAccount(AbstractAccount):
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        # tiered: higher balances earn a slightly better rate
        rate = 0.05 if self.balance > 100000 else 0.03
        return self.balance * rate


def report(acc):
    """Duck-typed: works on anything with .calculate_interest(), not just AbstractAccount."""
    return acc.calculate_interest()


# ---------------------------------------------------------------------------
# Exercise 8: dunder methods on a small Transaction class
# ---------------------------------------------------------------------------
class Transaction:
    def __init__(self, account_id, amount, timestamp):
        self.account_id = account_id
        self.amount = amount
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __repr__(self):
        return f"Transaction(account={self.account_id!r}, amount={self.amount}, ts={self.timestamp})"


# ---------------------------------------------------------------------------
# Exercise 10: composition, custom exceptions, context manager
# ---------------------------------------------------------------------------
class BankError(Exception):
    """Base exception for all bank-level problems."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal would take an account below its minimum balance."""


class Bank:
    """Has-a list of Accounts (composition, not inheritance)."""
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)


class TransactionSession:
    """Context manager: rolls the balance back if an exception occurs inside it."""
    def __init__(self, account: Account):
        self.account = account
        self.starting_balance = None

    def __enter__(self):
        self.starting_balance = self.account.balance
        print(f"Transaction session started for {self.account.id}, balance={self.starting_balance}")
        return self.account

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # roll back: re-deposit the difference to restore original balance
            diff = self.starting_balance - self.account.balance
            if diff > 0:
                self.account.deposit(diff)
            print(f"Rolled back {self.account.id} to balance={self.account.balance} after {exc_type.__name__}")
        else:
            print(f"Transaction session closed cleanly for {self.account.id}")
        return True  # suppress the exception - we've handled the rollback


# ---------------------------------------------------------------------------
# Demonstrations - the "Check Yourself" boxes from the PDF
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Exercise 1: class attribute shared across instances ---")
    a1 = Account("acc-1", balance=1000)
    a2 = Account("acc-2", balance=2000)
    a3 = Account("acc-3", balance=500)
    print("total_accounts from instance:", a1.total_accounts)
    print("total_accounts from class:", Account.total_accounts)

    print("\n--- Exercise 2: classmethod + staticmethod ---")
    a4 = Account.from_dict({"id": "acc-4", "balance": 750})
    print("Built from dict:", a4)
    print("Static validator, no instance needed:", Account.validate_upi_id("kavya@upi"))

    print("\n--- Exercise 3: encapsulation ---")
    a1.deposit(500)
    print("Balance after deposit:", a1.balance)
    try:
        a1.withdraw(999999)
    except InsufficientFundsError as e:
        print("Withdrawal correctly rejected:", e)

    print("\n--- Exercise 4: single inheritance ---")
    sav = SavingsAccount("acc-5", balance=3000, rate=0.04)
    print("isinstance(sav, Account):", isinstance(sav, Account))

    print("\n--- Exercise 5: multilevel inheritance ---")
    prem = PremiumSavingsAccount("acc-6", balance=5000, rate=0.04, bonus_rate=0.01)
    print("isinstance checks:", isinstance(prem, PremiumSavingsAccount),
          isinstance(prem, SavingsAccount), isinstance(prem, Account))

    print("\n--- Exercise 6: mixin + MRO ---")
    audited = AuditedSavings("acc-7", balance=1200, rate=0.03)
    audited.audit_log()
    print("MRO:", [c.__name__ for c in AuditedSavings.__mro__])
    print("One-sentence explanation: AuditMixin's audit_log() appears after")
    print("SavingsAccount/Account in the MRO because those were declared first")
    print("in the class definition, and MRO resolves bases in that listed order.")

    print("\n--- Exercise 7: abstraction + duck typing ---")
    try:
        AbstractAccount()  # type: ignore[abstract]  # deliberate: proving Python refuses this
    except TypeError as e:
        print("Cannot instantiate abstract class as expected:", e)
    fixed, tiered = FixedRateAccount(10000, 0.05), TieredRateAccount(150000)
    print("report(FixedRateAccount):", report(fixed))
    print("report(TieredRateAccount):", report(tiered))

    print("\n--- Exercise 8: dunder methods ---")
    txns = [
        Transaction("acc-1", 500, "2026-07-19T10:00"),
        Transaction("acc-1", 200, "2026-07-18T09:00"),
        Transaction("acc-1", 900, "2026-07-20T11:00"),
    ]
    print("sorted by timestamp:", sorted(txns))

    print("\n--- Exercise 9: Final + @final ---")
    print("MIN_BALANCE (Final constant):", Account.MIN_BALANCE)
    a1.freeze()
    print("(see ex9_final_check_BROKEN.py + mypy output in checklist.md)")

    print("\n--- Exercise 10: composition + exceptions + context manager ---")
    bank = Bank("MyBank")
    bank.add_account(a1)
    with TransactionSession(a1) as acc:
        acc.withdraw(999999999)  # deliberately triggers InsufficientFundsError
    print("balance restored after rollback:", a1.balance)
