# Part B Checklist – Kishore Kumar M R (Bank Account theme)

All 10 exercises implemented in `bank_account_oop.py`, tested by running the file directly.

- [x] Ex 1 — `total_accounts` class attribute confirmed shared (reads `3` from both instance and class after creating 3 accounts)
- [x] Ex 2 — `Account.from_dict()` classmethod + `Account.validate_upi_id()` staticmethod called directly off the class
- [x] Ex 3 — `__balance` private, exposed via read-only `balance` property; `deposit()`/`withdraw()` validate amount and update state (no direct setter, as instructed)
- [x] Ex 4 — `SavingsAccount(Account)` calls `super().__init__()`, `isinstance(sav, Account)` confirmed `True`
- [x] Ex 5 — 3-level chain `Account → SavingsAccount → PremiumSavingsAccount`, isinstance confirmed at all 3 levels
- [x] Ex 6 — `AuditMixin` used via multiple inheritance in `AuditedSavings`, `__mro__` printed and explained
- [x] Ex 7 — `AbstractAccount(ABC)`, two concrete subclasses (`FixedRateAccount`, `TieredRateAccount`) with different `calculate_interest()`, `report()` works via duck typing on both
- [x] Ex 8 — `__lt__` (by timestamp) and `__repr__` implemented on a separate small `Transaction` class, `sorted(txns)` works with no extra arguments
- [x] Ex 9 — `Final` constant + `@final` method, mypy-verified (see below)
- [x] Ex 10 — `Bank` has-a list of `Account`s (composition), `BankError → InsufficientFundsError` exception hierarchy, `TransactionSession` context manager rolls the balance back on exception

## Exercise 9 — mypy Evidence

**Broken state** (`ex9_final_check_BROKEN.py` — `SavingsAccount` illegally overrides `Account.freeze()`):
```
$ mypy ex9_final_check_BROKEN.py
ex9_final_check_BROKEN.py:21: error: Cannot override final attribute "freeze" (previously declared in base class "Account")  [misc]
Found 1 error in 1 file (checked 1 source file)
```

**Clean state** (`bank_account_oop.py` — no illegal override present):
```
$ mypy bank_account_oop.py
Success: no issues found in 1 source file
```

## Exercise 6 — One-Sentence MRO Explanation
`AuditMixin`'s `audit_log()` appears after `SavingsAccount`/`Account` in the MRO because those were declared first in the class definition, and MRO resolves bases in that listed order.

## Exercise 10 — Exception Actually Triggered
```
Transaction session started for acc-1, balance=1500
Rolled back acc-1 to balance=1500 after InsufficientFundsError
balance restored after rollback: 1500
```
Deliberately triggered `InsufficientFundsError` inside a `with` block and confirmed `__exit__` still ran and restored the balance correctly.
