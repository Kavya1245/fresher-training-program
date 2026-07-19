"""
Exercise 9 - Final + @final - the BROKEN version (illegal override present)
Run: mypy ex9_final_check_BROKEN.py
This file exists ONLY to capture the mypy error for the notes.
Do not run this with plain python - it demonstrates a mypy-time error, not a runtime one.
"""
from typing import Final, final


class Model:
    DEFAULT_THRESHOLD: Final[float] = 0.5

    def __init__(self, name):
        self.name = name

    @final
    def save(self):
        print(f"Saving {self.name}")


class CNNModel(Model):
    def save(self):  # ILLEGAL: overriding a method marked @final in the parent
        print("Custom save for CNN - mypy should flag this line")
