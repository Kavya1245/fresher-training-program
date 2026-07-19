"""
Exercise 9 - Final + @final - the BROKEN version (illegal override present)
Run: mypy ex9_final_check_BROKEN.py
This file exists ONLY to capture the mypy error for the notes.
"""
from typing import Final, final


class Task:
    MAX_RETRIES: Final[int] = 3

    def __init__(self, id):
        self.id = id

    @final
    def mark_done(self):
        print(f"Task {self.id} done")


class UrgentTask(Task):
    def mark_done(self):  # ILLEGAL: overriding a method marked @final in the parent
        print("Custom mark_done for urgent tasks - mypy should flag this line")
