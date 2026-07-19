# Part B Checklist – Vinothkumar (Task Orchestration theme)

All 10 exercises implemented in `task_orchestration_oop.py`, tested by running the file directly.

- [x] Ex 1 — `total_created` class attribute confirmed shared (reads `3` from both instance and class after creating 3 tasks)
- [x] Ex 2 — `Task.from_dict()` classmethod (validates via the staticmethod internally) + `Task.validate_priority()` staticmethod called directly off the class
- [x] Ex 3 — `__status` private, exposed via `@property status` with a `.setter` that only allows `pending`/`running`/`done`, raises `ValueError` otherwise
- [x] Ex 4 — `UrgentTask(Task)` calls `super().__init__()`, `isinstance(ut, Task)` confirmed `True`
- [x] Ex 5 — 3-level chain `Task → UrgentTask → ScheduledUrgentTask`, isinstance confirmed at all 3 levels
- [x] Ex 6 — `LoggableMixin` used via multiple inheritance in `FinalTask`, `__mro__` printed and explained
- [x] Ex 7 — `AbstractTask(ABC)`, two concrete subclasses (`ShellCommandTask`, `HttpRequestTask`) with different `run()`, `process()` works via duck typing on both
- [x] Ex 8 — `__lt__` (by priority) and `__repr__` implemented, `sorted(tasks_list)` works with no extra arguments
- [x] Ex 9 — `Final` constant + `@final` method, mypy-verified (see below)
- [x] Ex 10 — `Worker` has-a list of `Task`s (composition), `TaskError → RetryError` exception hierarchy, `WorkerSession` context manager confirmed to close cleanly after the block

## Exercise 9 — mypy Evidence

**Broken state** (`ex9_final_check_BROKEN.py` — `UrgentTask` illegally overrides `Task.mark_done()`):
```
$ mypy ex9_final_check_BROKEN.py
ex9_final_check_BROKEN.py:21: error: Cannot override final attribute "mark_done" (previously declared in base class "Task")  [misc]
Found 1 error in 1 file (checked 1 source file)
```

**Clean state** (`task_orchestration_oop.py` — no illegal override present):
```
$ mypy task_orchestration_oop.py
Success: no issues found in 1 source file
```

## Exercise 6 — One-Sentence MRO Explanation
`LoggableMixin`'s `log()` appears after `Task` in the MRO because Python checks classes in the order listed in the class definition, and `UrgentTask`/`Task` were listed before the mixin.

## Exercise 10 — Exception Actually Triggered
```
Custom exception triggered as expected: worker-1 exceeded max retries on task t-1
```
Confirmed by looping `worker.attempt()` past `Task.MAX_RETRIES`, not just defined but actually raised and caught at runtime.
