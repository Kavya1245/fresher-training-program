# Python OOP Concepts — Reference

Note: your source material (the attached doc) used C++ examples. Since your actual stack is Python, here's the same concepts translated correctly to Python syntax.

## 1. Class and Object

A **class** is a blueprint; an **object** is an instance created from it.

```python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Kavya")
print(s.name)  # Kavya
```

## 2. Encapsulation

Binding data and methods together, restricting direct access using naming conventions (`_protected`, `__private`) and exposing controlled access via `@property`.

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary  # private

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value
```

Python doesn't have true "private" — `__salary` gets name-mangled to `_Employee__salary`. It's a convention, not a lock.

## 3. Abstraction

Hides implementation details, exposing only essential behavior. Done via `abc.ABC` and `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        ...

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
```
You cannot create an instance of `Shape` directly — Python enforces this.

## 4. Inheritance

One class acquires properties/methods of another (parent → child relationship).

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()   # inherited
d.bark()    # own method
```

## 5. Polymorphism

Same method name, different behavior depending on the object.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

for a in [Dog(), Cat()]:
    a.speak()
```

## 6. Class Attributes vs Instance Attributes

```python
class Model:
    total_models = 0   # class attribute — shared by ALL instances

    def __init__(self, name):
        self.name = name          # instance attribute — unique per object
        Model.total_models += 1
```

## 7. `@classmethod` vs `@staticmethod`

```python
class Model:
    @classmethod
    def from_config(cls, cfg):
        return cls(cfg["name"])       # receives the class itself, can build instances

    @staticmethod
    def normalize_name(name):
        return name.strip().lower()   # no self/cls — a plain utility function grouped in the class
```

## 8. `super()`

Calls the parent class's method — most commonly used in `__init__` to avoid rewriting shared setup logic.

```python
class CNNModel(Model):
    def __init__(self, name, layers):
        super().__init__(name)   # runs Model's __init__ first
        self.layers = layers
```

## Summary Table

| Concept | Keyword/Tool | Purpose |
|---|---|---|
| Class/Object | `class`, `__init__` | Blueprint and instance |
| Encapsulation | `__private`, `@property` | Controlled access to data |
| Abstraction | `ABC`, `@abstractmethod` | Hide implementation, show essentials |
| Inheritance | `class Child(Parent)` | Reuse and extend behavior |
| Polymorphism | Method overriding | Same interface, different behavior |
| Class attribute | Defined outside `__init__` | Shared across all instances |
| `@classmethod` | `cls` | Alternate constructor |
| `@staticmethod` | no self/cls | Utility function grouped in class |
