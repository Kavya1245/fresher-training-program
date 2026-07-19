"""
Day 5 - OOP Practice - Vinothkumar - Task Orchestration theme
Classes build cumulatively: Task -> UrgentTask -> ScheduledUrgentTask
Run this file directly to see all "check yourself" demonstrations print out.
"""
from abc import ABC, abstractmethod
from typing import Final, final


# ---------------------------------------------------------------------------
# Exercise 1: self, __init__, class attribute vs instance attribute
# ---------------------------------------------------------------------------
class Task:
    total_created = 0  # class attribute - shared across every Task ever made

    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
        self.__status = "pending"  # Ex3: private, starts pending
        Task.total_created += 1

    # -----------------------------------------------------------------
    # Exercise 2: @classmethod factory vs @staticmethod validator
    # -----------------------------------------------------------------
    @classmethod
    def from_dict(cls, data: dict):
        """Alternate constructor - builds a Task from a plain dict payload."""
        priority = data.get("priority", 0)
        if not cls.validate_priority(priority):
            raise ValueError(f"Invalid priority in payload: {priority}")
        return cls(data["id"], priority)

    @staticmethod
    def validate_priority(p) -> bool:
        """Pure validation logic - doesn't need any instance or class data."""
        return isinstance(p, (int, float)) and 0 <= p <= 10

    # -----------------------------------------------------------------
    # Exercise 3: Encapsulation via property + validated setter
    # -----------------------------------------------------------------
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        allowed = ("pending", "running", "done")
        if value not in allowed:
            raise ValueError(f"status must be one of {allowed}, got {value!r}")
        self.__status = value

    # -----------------------------------------------------------------
    # Exercise 9: Final constant + @final method
    # -----------------------------------------------------------------
    MAX_RETRIES: Final[int] = 3

    @final
    def mark_done(self):
        self.status = "done"
        print(f"Task {self.id} marked done (this method cannot be overridden)")

    # -----------------------------------------------------------------
    # Exercise 8: dunder methods for comparison and display
    # -----------------------------------------------------------------
    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(id={self.id!r}, priority={self.priority}, status={self.status!r})"


# ---------------------------------------------------------------------------
# Exercise 4: single inheritance + super()
# ---------------------------------------------------------------------------
class UrgentTask(Task):
    def __init__(self, id, priority, urgency_level):
        super().__init__(id, priority)
        self.urgency_level = urgency_level


# ---------------------------------------------------------------------------
# Exercise 5: multilevel inheritance (3-level chain)
# ---------------------------------------------------------------------------
class ScheduledUrgentTask(UrgentTask):
    def __init__(self, id, priority, urgency_level, scheduled_time):
        super().__init__(id, priority, urgency_level)
        self.scheduled_time = scheduled_time


# ---------------------------------------------------------------------------
# Exercise 6: multiple inheritance via mixin + MRO
# ---------------------------------------------------------------------------
class LoggableMixin:
    """Behaviour-only mixin - independent of Task's internal state."""
    def log(self, msg):
        print(f"[LOG] {msg}")


class FinalTask(UrgentTask, LoggableMixin):
    pass


# ---------------------------------------------------------------------------
# Exercise 7: abstraction, overriding, duck typing
# ---------------------------------------------------------------------------
class AbstractTask(ABC):
    @abstractmethod
    def run(self):
        ...


class ShellCommandTask(AbstractTask):
    def run(self):
        return "executed shell command"


class HttpRequestTask(AbstractTask):
    def run(self):
        return "sent HTTP request"


def process(x):
    """Duck-typed: runs anything with a .run() method, not just AbstractTask."""
    return x.run()


# ---------------------------------------------------------------------------
# Exercise 10: composition, custom exceptions, context manager
# ---------------------------------------------------------------------------
class TaskError(Exception):
    """Base exception for all task/worker problems."""


class RetryError(TaskError):
    """Raised when a task has exceeded its retry budget."""


class Worker:
    """Has-a list of Tasks (composition, not inheritance)."""
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.attempts = 0

    def add_task(self, task: Task):
        self.tasks.append(task)

    def attempt(self, task: Task):
        self.attempts += 1
        if self.attempts > Task.MAX_RETRIES:
            raise RetryError(f"{self.name} exceeded max retries on task {task.id}")
        return f"attempt {self.attempts} on task {task.id}"


class WorkerSession:
    """Context manager: opens the worker on enter, closes it on exit -
    even if an exception occurs inside the 'with' block."""
    def __init__(self, worker: Worker):
        self.worker = worker
        self.open = False

    def __enter__(self):
        self.open = True
        print(f"Worker session opened for {self.worker.name}")
        return self.worker

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open = False
        print(f"Worker session closed for {self.worker.name}")
        return False  # do not suppress exceptions


# ---------------------------------------------------------------------------
# Demonstrations - the "Check Yourself" boxes from the PDF
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Exercise 1: class attribute shared across instances ---")
    t1 = Task("t-1", priority=5)
    t2 = Task("t-2", priority=8)
    t3 = Task("t-3", priority=2)
    print("total_created from instance:", t1.total_created)
    print("total_created from class:", Task.total_created)

    print("\n--- Exercise 2: classmethod + staticmethod ---")
    t4 = Task.from_dict({"id": "t-4", "priority": 7})
    print("Built from dict:", t4)
    print("Static validator, no instance needed:", Task.validate_priority(11))

    print("\n--- Exercise 3: encapsulation ---")
    t1.status = "running"
    print("Valid status change accepted:", t1.status)
    try:
        t1.status = "cancelled"
    except ValueError as e:
        print("Invalid status rejected as expected:", e)

    print("\n--- Exercise 4: single inheritance ---")
    ut = UrgentTask("t-5", priority=9, urgency_level="high")
    print("isinstance(ut, Task):", isinstance(ut, Task))

    print("\n--- Exercise 5: multilevel inheritance ---")
    sut = ScheduledUrgentTask("t-6", priority=10, urgency_level="critical", scheduled_time="2026-07-20T09:00")
    print("isinstance checks:", isinstance(sut, ScheduledUrgentTask),
          isinstance(sut, UrgentTask), isinstance(sut, Task))

    print("\n--- Exercise 6: mixin + MRO ---")
    ft = FinalTask("t-7", priority=6, urgency_level="medium")
    ft.log("FinalTask created")
    print("MRO:", [c.__name__ for c in FinalTask.__mro__])
    print("One-sentence explanation: LoggableMixin's log() appears after Task in")
    print("the MRO because Python checks the classes in the order listed in the")
    print("class definition, and UrgentTask/Task were listed before the mixin.")

    print("\n--- Exercise 7: abstraction + duck typing ---")
    try:
        AbstractTask()  # type: ignore[abstract]  # deliberate: proving Python refuses this
    except TypeError as e:
        print("Cannot instantiate abstract class as expected:", e)
    shell_task, http_task = ShellCommandTask(), HttpRequestTask()
    print("process(ShellCommandTask):", process(shell_task))
    print("process(HttpRequestTask):", process(http_task))

    print("\n--- Exercise 8: dunder methods ---")
    tasks_list = [t1, t2, t3]
    print("sorted by priority:", sorted(tasks_list))

    print("\n--- Exercise 9: Final + @final ---")
    print("MAX_RETRIES (Final constant):", Task.MAX_RETRIES)
    t2.mark_done()
    print("(see ex9_final_check_BROKEN.py + mypy output in checklist.md)")

    print("\n--- Exercise 10: composition + exceptions + context manager ---")
    worker = Worker("worker-1")
    worker.add_task(t1)
    with WorkerSession(worker) as active:
        print("session open:", active is worker, "->", worker.attempts, "attempts so far")
        for _ in range(3):
            print(worker.attempt(t1))
    print("session marked open after block:", WorkerSession(worker).open)

    try:
        for _ in range(5):
            worker.attempt(t1)
    except RetryError as e:
        print("Custom exception triggered as expected:", e)
