# Part B Checklist – Kavya S (ML Model theme)

All 10 exercises implemented in `ml_model_oop.py`, tested by running the file directly.

- [x] Ex 1 — `total_models` class attribute confirmed shared (reads `3` from both instance and class after creating 3 models)
- [x] Ex 2 — `Model.from_config()` classmethod + `Model.normalize_name()` staticmethod, staticmethod called directly off the class with no instance
- [x] Ex 3 — `__weights` private, exposed only via computed read-only `accuracy` property (no setter)
- [x] Ex 4 — `CNNModel(Model)` calls `super().__init__()`, `isinstance(cnn, Model)` confirmed `True`
- [x] Ex 5 — 3-level chain `Model → CNNModel → TransferLearningCNN`, isinstance confirmed at all 3 levels
- [x] Ex 6 — `SerializableMixin` used via multiple inheritance in `SerializableCNN`, `__mro__` printed and explained
- [x] Ex 7 — `AbstractModel(ABC)`, two concrete subclasses with different `predict()`, `evaluate()` works via duck typing on both
- [x] Ex 8 — `__lt__` (by accuracy) and `__repr__` implemented, `sorted(models_list)` works with no extra arguments
- [x] Ex 9 — `Final` constant + `@final` method, mypy-verified (see below)
- [x] Ex 10 — `Trainer` has-a `Model` (composition), `ModelError → NotTrainedError` exception hierarchy, `TrainingSession` context manager confirmed to reset `is_training` after the block

## Exercise 9 — mypy Evidence

**Broken state** (`ex9_final_check_BROKEN.py` — `CNNModel` illegally overrides `Model.save()`):
```
$ mypy ex9_final_check_BROKEN.py
ex9_final_check_BROKEN.py:22: error: Cannot override final attribute "save" (previously declared in base class "Model")  [misc]
Found 1 error in 1 file (checked 1 source file)
```

**Clean state** (`ml_model_oop.py` — no illegal override present):
```
$ mypy ml_model_oop.py
Success: no issues found in 1 source file
```

## Exercise 6 — One-Sentence MRO Explanation
The mixin's method appears after the main parent chain in `__mro__` because Python resolves left-to-right through the bases listed in the class definition, and `Model`/`CNNModel` were listed before `SerializableMixin`.

## Exercise 10 — Exception Actually Triggered
```
Custom exception triggered as expected: net-b has not been trained yet
```
Confirmed via a fresh `Trainer` with `is_trained=False`, not just defined but actually raised and caught at runtime.
