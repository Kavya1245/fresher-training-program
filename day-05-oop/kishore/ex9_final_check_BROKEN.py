"""
Exercise 9 - Final + @final - the BROKEN version (illegal override present)
Run: mypy ex9_final_check_BROKEN.py
This file exists ONLY to capture the mypy error for the notes.
"""
from typing import Final, final


class Account:
    MIN_BALANCE: Final[float] = 0.0

    def __init__(self, id):
        self.id = id

    @final
    def freeze(self):
        print(f"Account {self.id} frozen")


class SavingsAccount(Account):
    def freeze(self):  # ILLEGAL: overriding a method marked @final in the parent
        print("Custom freeze for savings accounts - mypy should flag this line")
