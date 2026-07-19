"""
Day 5 - OOP Practice - Kavya S - ML Model theme
Classes build cumulatively: Model -> CNNModel -> TransferLearningCNN
Run this file directly to see all "check yourself" demonstrations print out.
"""
from abc import ABC, abstractmethod
from typing import Final, final


# ---------------------------------------------------------------------------
# Exercise 1: self, __init__, class attribute vs instance attribute
# ---------------------------------------------------------------------------
class Model:
    total_models = 0  # class attribute - shared across every instance

    def __init__(self, name, threshold, weights=None):
        self.name = name              # instance attribute
        self.threshold = threshold    # instance attribute
        self.__weights = weights if weights is not None else []  # Ex3: private
        Model.total_models += 1

    # -----------------------------------------------------------------
    # Exercise 2: @classmethod factory vs @staticmethod utility
    # -----------------------------------------------------------------
    @classmethod
    def from_config(cls, cfg: dict):
        """Alternate constructor - builds a Model from a config dict."""
        return cls(cfg["name"], cfg["threshold"], cfg.get("weights"))

    @staticmethod
    def normalize_name(name: str) -> str:
        """Utility - no self/cls needed, works off the class directly."""
        return name.strip().lower()

    # -----------------------------------------------------------------
    # Exercise 3: Encapsulation - private attribute + read-only computed property
    # -----------------------------------------------------------------
    @property
    def accuracy(self) -> float:
        """Computed, read-only. No setter - accuracy is derived, not assigned."""
        if not self.__weights:
            return 0.0
        return sum(self.__weights) / len(self.__weights)

    # -----------------------------------------------------------------
    # Exercise 9: Final constant + @final method
    # -----------------------------------------------------------------
    DEFAULT_THRESHOLD: Final[float] = 0.5

    @final
    def save(self):
        print(f"Saving model '{self.name}' (this method cannot be overridden)")

    # -----------------------------------------------------------------
    # Exercise 8: dunder methods for comparison and display
    # -----------------------------------------------------------------
    def __lt__(self, other):
        return self.accuracy < other.accuracy

    def __repr__(self):
        return f"Model(name={self.name!r}, accuracy={self.accuracy:.2f})"


# ---------------------------------------------------------------------------
# Exercise 4: single inheritance + super()
# ---------------------------------------------------------------------------
class CNNModel(Model):
    def __init__(self, name, threshold, layers, weights=None):
        super().__init__(name, threshold, weights)
        self.layers = layers


# ---------------------------------------------------------------------------
# Exercise 5: multilevel inheritance (3-level chain)
# ---------------------------------------------------------------------------
class TransferLearningCNN(CNNModel):
    def __init__(self, name, threshold, layers, pretrained_source, weights=None):
        super().__init__(name, threshold, layers, weights)
        self.pretrained_source = pretrained_source


# ---------------------------------------------------------------------------
# Exercise 6: multiple inheritance via mixin + MRO
# ---------------------------------------------------------------------------
class SerializableMixin:
    """Behaviour-only mixin - no __init__, no shared state with Model."""
    def to_json(self):
        return {"name": self.name, "accuracy": self.accuracy}


class SerializableCNN(CNNModel, SerializableMixin):
    pass


# ---------------------------------------------------------------------------
# Exercise 7: abstraction, overriding, duck typing
# ---------------------------------------------------------------------------
class AbstractModel(ABC):
    @abstractmethod
    def predict(self, x):
        ...


class LinearPredictor(AbstractModel):
    def predict(self, x):
        return x * 2  # toy linear behaviour


class ThresholdPredictor(AbstractModel):
    def predict(self, x):
        return "positive" if x > 0.5 else "negative"


def evaluate(m, x):
    """Duck-typed: works on ANYTHING with a .predict() method, not just AbstractModel."""
    return m.predict(x)


# ---------------------------------------------------------------------------
# Exercise 10: composition, custom exceptions, context manager
# ---------------------------------------------------------------------------
class ModelError(Exception):
    """Base exception for all model-related problems."""


class NotTrainedError(ModelError):
    """Raised when trying to use a model that hasn't been trained yet."""


class Trainer:
    """Has-a Model (composition, not inheritance)."""
    def __init__(self, model: Model):
        self.model = model
        self.is_training = False
        self.is_trained = False

    def predict(self, x):
        if not self.is_trained:
            raise NotTrainedError(f"{self.model.name} has not been trained yet")
        return x


class TrainingSession:
    """Context manager: sets training mode on enter, restores it on exit -
    even if an exception occurs inside the 'with' block."""
    def __init__(self, trainer: Trainer):
        self.trainer = trainer

    def __enter__(self):
        self.trainer.is_training = True
        print(f"Training started for {self.trainer.model.name}")
        return self.trainer

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.trainer.is_training = False
        print(f"Training session closed for {self.trainer.model.name}")
        return False  # do not suppress exceptions


# ---------------------------------------------------------------------------
# Demonstrations - the "Check Yourself" boxes from the PDF
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Exercise 1: class attribute shared across instances ---")
    m1 = Model("net-a", 0.5, weights=[0.8, 0.9])
    m2 = Model("net-b", 0.6, weights=[0.4, 0.5])
    m3 = Model("net-c", 0.7, weights=[0.9, 0.95])
    print("total_models from instance:", m1.total_models)
    print("total_models from class:", Model.total_models)

    print("\n--- Exercise 2: classmethod + staticmethod ---")
    m4 = Model.from_config({"name": "  ConfigNet  ", "threshold": 0.5, "weights": [0.7]})
    print("Built from config:", m4)
    print("Static utility, no instance needed:", Model.normalize_name("  MyModel  "))

    print("\n--- Exercise 3: encapsulation ---")
    try:
        print(m1._Model__weights)  # type: ignore[attr-defined]  # deliberate: showing name mangling, never rely on this
    except AttributeError as e:
        print("Direct private access failed as expected:", e)
    print("accuracy via computed property:", m1.accuracy)

    print("\n--- Exercise 4: single inheritance ---")
    cnn = CNNModel("cnn-1", 0.6, layers=5, weights=[0.6, 0.7])
    print("isinstance(cnn, Model):", isinstance(cnn, Model))

    print("\n--- Exercise 5: multilevel inheritance ---")
    tl_cnn = TransferLearningCNN("tl-cnn-1", 0.6, layers=8, pretrained_source="ImageNet", weights=[0.85, 0.9])
    print("isinstance checks:", isinstance(tl_cnn, TransferLearningCNN),
          isinstance(tl_cnn, CNNModel), isinstance(tl_cnn, Model))

    print("\n--- Exercise 6: mixin + MRO ---")
    ser_cnn = SerializableCNN("ser-cnn", 0.5, layers=4, weights=[0.5, 0.6])
    print("to_json():", ser_cnn.to_json())
    print("MRO:", [c.__name__ for c in SerializableCNN.__mro__])
    print("One-sentence explanation: the mixin's method appears after the main")
    print("parent chain in MRO because Python resolves left-to-right through the")
    print("bases you listed, and Model/CNNModel form the primary chain checked first.")

    print("\n--- Exercise 7: abstraction + duck typing ---")
    try:
        AbstractModel()  # type: ignore[abstract]  # deliberate: proving Python refuses this
    except TypeError as e:
        print("Cannot instantiate abstract class as expected:", e)
    lp, tp = LinearPredictor(), ThresholdPredictor()
    print("evaluate(LinearPredictor):", evaluate(lp, 4))
    print("evaluate(ThresholdPredictor):", evaluate(tp, 0.9))

    print("\n--- Exercise 8: dunder methods ---")
    models_list = [m1, m2, m3]
    print("sorted by accuracy:", sorted(models_list))

    print("\n--- Exercise 9: Final + @final ---")
    print("DEFAULT_THRESHOLD (Final constant):", Model.DEFAULT_THRESHOLD)
    m1.save()
    print("(see ex9_final_check.py + mypy_output.txt for the mypy-caught override)")

    print("\n--- Exercise 10: composition + exceptions + context manager ---")
    trainer = Trainer(cnn)
    with TrainingSession(trainer) as active:
        print("is_training inside the block:", active.is_training)
    print("is_training after the block:", trainer.is_training)

    try:
        untrained_trainer = Trainer(m2)  # fresh trainer, is_trained still False
        untrained_trainer.predict(1)
    except NotTrainedError as e:
        print("Custom exception triggered as expected:", e)
