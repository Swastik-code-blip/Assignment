

# ============================================================
# Q1. Explain the importance of Functions.
# ============================================================
"""
Functions break a program into small, reusable, testable blocks of
code. Benefits:
- Reusability: write once, call many times.
- Readability: gives a name to a chunk of logic.
- Maintainability: fix logic in one place.
- Abstraction: hides implementation details from the caller.
- Easier debugging and unit testing (isolated blocks).
- Avoids code duplication (DRY principle).
"""

# ============================================================
# Q2. Write a basic function to greet students.
# ============================================================
def greet_student(name):
    return f"Hello, {name}! Welcome to the class."

print(greet_student("Aarav"))


# ============================================================
# Q3. Difference between print and return statements
# ============================================================
"""
print():
- Just displays output to the console.
- Returns None; the printed value cannot be reused in code.

return:
- Sends a value back from a function to the caller.
- The value CAN be stored in a variable / used further in code.
- Ends the function's execution at that point.
"""
def demo_print():
    print("This is printed, not returned")

def demo_return():
    return "This is returned"

demo_print()
result = demo_return()
print(result)


# ============================================================
# Q4. What are *args and **kwargs?
# ============================================================
"""
*args  -> collects extra POSITIONAL arguments into a tuple.
**kwargs -> collects extra KEYWORD arguments into a dictionary.
They let a function accept a variable number of arguments.
"""
def demo_args_kwargs(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo_args_kwargs(1, 2, 3, name="Alice", age=25)


# ============================================================
# Q5. Explain the iterator function / iterators.
# ============================================================
"""
An iterator is an object representing a stream of data. It implements:
- __iter__() -> returns the iterator object itself.
- __next__() -> returns the next value, raises StopIteration when done.

iter() is used to get an iterator from an iterable, and next() is used
to fetch the next item from it.
"""
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))


# ============================================================
# Q6. Generator: squares of numbers from 1 to n
# ============================================================
def gen_squares(n):
    for i in range(1, n + 1):
        yield i * i

print(list(gen_squares(5)))


# ============================================================
# Q7. Generator: palindromic numbers up to n
# ============================================================
def gen_palindromes(n):
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            yield i

print(list(gen_palindromes(150)))


# ============================================================
# Q8. Generator: even numbers from 2 to n
# ============================================================
def gen_evens(n):
    for i in range(2, n + 1, 2):
        yield i

print(list(gen_evens(20)))


# ============================================================
# Q9. Generator: powers of two up to n
# ============================================================
def gen_powers_of_two(n):
    power = 1
    while power <= n:
        yield power
        power *= 2

print(list(gen_powers_of_two(100)))


# ============================================================
# Q10. Generator: prime numbers up to n
# ============================================================
def gen_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                return False
        return True

    for i in range(2, n + 1):
        if is_prime(i):
            yield i

print(list(gen_primes(30)))


# ============================================================
# Q11 / Q22. Lambda: sum of two numbers
# ============================================================
add = lambda a, b: a + b
print(add(4, 5))


# ============================================================
# Q12 / Q23. Lambda: square of a number
# ============================================================
square = lambda x: x * x
print(square(6))


# ============================================================
# Q13 / Q24. Lambda: check even or odd
# ============================================================
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))


# ============================================================
# Q15 / Q25. Lambda: concatenate two strings
# ============================================================
concat = lambda s1, s2: s1 + s2
print(concat("Hello, ", "World!"))


# ============================================================
# Q16 / Q26. Lambda: maximum of three numbers
# ============================================================
max_of_three = lambda a, b, c: max(a, b, c)
print(max_of_three(3, 9, 7))


# ============================================================
# Q17. Squares of even numbers from a given list
# ============================================================
def squares_of_evens(lst):
    return [x * x for x in lst if x % 2 == 0]

print(squares_of_evens([1, 2, 3, 4, 5, 6]))


# ============================================================
# Q18. Product of positive numbers from a given list
# ============================================================
def product_of_positives(lst):
    product = 1
    for x in lst:
        if x > 0:
            product *= x
    return product

print(product_of_positives([-2, 3, 4, -5, 6]))


# ============================================================
# Q19. Double the values of odd numbers from a given list
# ============================================================
def double_odds(lst):
    return [x * 2 if x % 2 != 0 else x for x in lst]

print(double_odds([1, 2, 3, 4, 5]))


# ============================================================
# Q20. Sum of cubes of numbers from a given list
# ============================================================
def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)

print(sum_of_cubes([1, 2, 3, 4]))


# ============================================================
# Q21. Filter out prime numbers from a given list
# ============================================================
def filter_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                return False
        return True
    return [x for x in lst if is_prime(x)]

print(filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# ============================================================
# Q27. What is encapsulation in OOP?
# ============================================================
"""
Encapsulation is the bundling of data (attributes) and the methods
that operate on that data into a single unit (class), while
restricting direct access to some of the object's components. In
Python this is achieved by convention using a single underscore
(_protected) or name mangling with a double underscore (__private).
It protects internal state and enforces controlled access via
methods (getters/setters).
"""

# ============================================================
# Q28. Access modifiers in Python classes
# ============================================================
"""
Python doesn't have strict access modifiers like Java/C++, it uses
naming conventions:
- public:    normal_name      -> accessible from anywhere
- protected: _single_leading  -> convention: internal use, still accessible
- private:   __double_leading -> name-mangled to _ClassName__name,
                                  harder to access from outside
"""
class AccessDemo:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def show_private(self):
        return self.__private_var

obj = AccessDemo()
print(obj.public_var)
print(obj._protected_var)
print(obj.show_private())


# ============================================================
# Q29. What is inheritance in OOP?
# ============================================================
"""
Inheritance allows a class (child/subclass) to acquire the
attributes and methods of another class (parent/superclass),
enabling code reuse and the creation of hierarchical relationships.
"""

# ============================================================
# Q30. Define polymorphism in OOP.
# ============================================================
"""
Polymorphism means "many forms" - the ability of different classes
to be treated through the same interface, where each class provides
its own implementation of a shared method (e.g. via method
overriding), and the correct version is called automatically based
on the actual object type.
"""

# ============================================================
# Q31. Explain method overriding in Python.
# ============================================================
"""
Method overriding happens when a subclass provides its own
implementation of a method that is already defined in its parent
class. The child's version replaces (overrides) the parent's
version when called on a child instance.
"""

# ============================================================
# Q32. Animal / Dog make_sound
# ============================================================
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

Animal().make_sound()
Dog().make_sound()


# ============================================================
# Q33. Override move() in Dog
# ============================================================
class Animal2:
    def move(self):
        print("Animal moves")

class Dog2(Animal2):
    def move(self):
        print("Dog runs")

Animal2().move()
Dog2().move()


# ============================================================
# Q34. Mammal + DogMammal (multiple inheritance)
# ============================================================
class Mammal:
    def reproduce(self):
        print("Giving birth to live young.")

class DogMammal(Dog2, Mammal):
    pass

d = DogMammal()
d.move()
d.reproduce()


# ============================================================
# Q35. GermanShepherd overriding make_sound
# ============================================================
class GermanShepherd(Dog):
    def make_sound(self):
        print("Bark!")

GermanShepherd().make_sound()


# ============================================================
# Q36. Constructors in Animal & Dog with different params
# ============================================================
class Animal3:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created")

class Dog3(Animal3):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog breed: {self.breed}")

Dog3("Rex", "Labrador")


# ============================================================
# Q37. What is abstraction in Python? How is it implemented?
# ============================================================
"""
Abstraction means hiding complex implementation details and showing
only the essential features of an object. In Python it's implemented
using abstract base classes (ABC module) and abstract methods, which
force subclasses to implement specific methods without exposing how
they work internally.
"""

# ============================================================
# Q38. Importance of abstraction in OOP
# ============================================================
"""
- Reduces complexity by hiding unnecessary details.
- Focuses on what an object does rather than how it does it.
- Improves maintainability - implementation can change without
  affecting code that depends on the abstract interface.
- Enforces a consistent interface across different subclasses.
"""

# ============================================================
# Q39. How are abstract methods different from regular methods?
# ============================================================
"""
An abstract method is declared in an abstract base class using the
@abstractmethod decorator but has NO implementation (or just
'pass'/raise NotImplementedError). It MUST be overridden by any
concrete subclass, and the abstract class itself cannot be
instantiated. A regular method has a full implementation and can be
used directly or optionally overridden.
"""

# ============================================================
# Q40. Achieving abstraction using interfaces (ABC) in Python
# ============================================================
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print(Square(4).area())
# Shape() would raise: TypeError: Can't instantiate abstract class


# ============================================================
# Q41. Abstraction as a common interface for related classes
# ============================================================
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

for method in (CreditCard(), UPI()):
    method.pay(500)


# ============================================================
# Q42. How does Python achieve polymorphism through overriding?
# ============================================================
"""
When a subclass redefines a method already present in its parent,
Python resolves the method call at runtime based on the actual
object's class (dynamic dispatch). Calling the same method name on
different subclass objects triggers each one's own overridden
version - this is runtime polymorphism.
"""

# ============================================================
# Q43. Base class with a method + subclass override
# ============================================================
class Base:
    def greet(self):
        print("Hello from Base")

class Derived(Base):
    def greet(self):
        print("Hello from Derived")

Base().greet()
Derived().greet()


# ============================================================
# Q44. Base class + multiple subclasses with overridden methods
# ============================================================
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def info(self):
        print("This is a car")

class Bike(Vehicle):
    def info(self):
        print("This is a bike")

for v in (Vehicle(), Car(), Bike()):
    v.info()


# ============================================================
# Q45. How does polymorphism improve readability & reusability?
# ============================================================
"""
Polymorphism lets you write generic code that works with objects of
different classes through a common interface (e.g. a single loop
calling obj.info() on many different types). This avoids repetitive
if/elif type-checking, makes code easier to read, and lets new
classes be added without modifying the calling code (reusability).
"""

# ============================================================
# Q46. How Python supports polymorphism with duck typing
# ============================================================
"""
Duck typing: "If it walks like a duck and quacks like a duck, it's a
duck." Python doesn't check an object's type before calling a
method - it just calls it. If the object has the required method,
it works, regardless of its class or inheritance hierarchy.
"""
class Duck:
    def sound(self):
        print("Quack!")

class Person:
    def sound(self):
        print("I'm imitating a duck: Quack!")

for thing in (Duck(), Person()):
    thing.sound()  # works for both, no shared base class needed


# ============================================================
# Q47. How do you achieve encapsulation in Python?
# ============================================================
"""
By marking attributes as protected (_attr) or private (__attr), and
exposing controlled access through public methods or @property
getters/setters, instead of allowing direct external access/modification.
"""

# ============================================================
# Q48. Can encapsulation be bypassed in Python? If so, how?
# ============================================================
"""
Yes. Python's privacy is by convention, not enforcement.
- _protected attributes can be accessed directly.
- __private attributes are name-mangled to _ClassName__attr, and can
  still be accessed using that mangled name (e.g. obj._ClassName__attr).
So encapsulation in Python relies on discipline, not hard restriction.
"""
class Bypass:
    def __init__(self):
        self.__secret = 42

b = Bypass()
print(b._Bypass__secret)  # bypasses "private" access


# ============================================================
# Q49. BankAccount with private balance
# ============================================================
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.check_balance())


# ============================================================
# Q50. Person class with private name/email + get/set
# ============================================================
class Person2:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

p = Person2("Riya", "riya@example.com")
p.set_email("riya.new@example.com")
print(p.get_name(), p.get_email())


# ============================================================
# Q51. Why is encapsulation considered a pillar of OOP?
# ============================================================
"""
Because it protects an object's internal state from unintended or
invalid modification, hides implementation details, enables
validation logic before changing data (through setters), and allows
internal implementation to change without breaking external code
that uses the class - all essential to robust, maintainable OOP design.
"""

# ============================================================
# Q52. Decorator: print message before and after function execution
# ============================================================
def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()


# ============================================================
# Q53. Decorator that accepts arguments and prints function name
# ============================================================
def named_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@named_decorator
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 4))


# ============================================================
# Q54. Two decorators applied to a single function, in order
# ============================================================
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One: before")
        result = func(*args, **kwargs)
        print("Decorator One: after")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two: before")
        result = func(*args, **kwargs)
        print("Decorator Two: after")
        return result
    return wrapper

@decorator_one
@decorator_two
def multiply(a, b):
    print("Multiplying")
    return a * b

# Execution order: decorator_one wraps decorator_two which wraps multiply
print(multiply(3, 5))


# ============================================================
# Q55. Decorator that accepts and passes function arguments
# ============================================================
def passthrough_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Args received: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@passthrough_decorator
def subtract(a, b):
    return a - b

print(subtract(10, 4))


# ============================================================
# Q56. Decorator that preserves metadata of the original function
# ============================================================
import functools

def metadata_preserving_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@metadata_preserving_decorator
def example_func():
    """This is an example function."""
    pass

print(example_func.__name__)  # 'example_func' (preserved, not 'wrapper')
print(example_func.__doc__)   # docstring preserved


# ============================================================
# Q57. Calculator class with static method add
# ============================================================
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 7))


# ============================================================
# Q58. Employee class with class method get_employee_count
# ============================================================
class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.count

e1 = Employee("Sam")
e2 = Employee("Tara")
print(Employee.get_employee_count())


# ============================================================
# Q59. StringFormatter class with static method reverse_string
# ============================================================
class StringFormatter:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

print(StringFormatter.reverse_string("hello"))


# ============================================================
# Q60. Circle class with class method calculate_area
# ============================================================
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def calculate_area(cls, radius):
        return cls.pi * radius ** 2

print(Circle.calculate_area(5))


# ============================================================
# Q61. TemperatureConverter with static method celsius_to_fahrenheit
# ============================================================
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))


# ============================================================
# Q62. Purpose of __str__()
# ============================================================
"""
__str__() defines the "informal"/readable string representation of
an object, used by print() and str(). It should be user-friendly.
"""
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

print(Book("Python 101"))


# ============================================================
# Q63. How does __len__() work?
# ============================================================
"""
__len__() lets a custom object work with the built-in len() function
by returning an integer representing the object's "length".
"""
class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

print(len(Cart(["apple", "banana", "cherry"])))


# ============================================================
# Q64. Usage of __add__()
# ============================================================
"""
__add__() overloads the '+' operator for custom objects, defining
what happens when two instances (or an instance and a value) are added.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)


# ============================================================
# Q65. Purpose of __getitem__()
# ============================================================
"""
__getitem__() allows an object to support indexing/subscripting
(obj[key]), like a list or dictionary.
"""
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

ml = MyList([10, 20, 30])
print(ml[1])


# ============================================================
# Q66. __iter__() and __next__() with example
# ============================================================
"""
__iter__() returns the iterator object (usually self); __next__()
returns the next value each time it is called, and raises
StopIteration when there are no more items. Together they let a
custom class be used in a for loop.
"""
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in CountUpTo(5):
    print(num, end=" ")
print()


# ============================================================
# Q67. Getter method using property decorators
# ============================================================
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Getter for price"""
        return self._price

prod = Product(100)
print(prod.price)  # accessed like an attribute, no parentheses


# ============================================================
# Q68. Setter methods with property decorators
# ============================================================
class Product2:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

p = Product2(100)
p.price = 150  # uses the setter
print(p.price)


# ============================================================
# Q69. Purpose of @property decorator
# ============================================================
"""
@property lets a method be accessed like an attribute (no
parentheses needed), enabling controlled, computed, or validated
access to data while keeping a simple attribute-like interface.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print(r.area)  # computed on the fly, accessed like an attribute


# ============================================================
# Q70. @<property>.deleter decorator
# ============================================================
class Account:
    def __init__(self, owner):
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @owner.deleter
    def owner(self):
        print("Deleting owner attribute")
        del self._owner

acc2 = Account("John")
print(acc2.owner)
del acc2.owner  # triggers the deleter


# ============================================================
# Q71. How encapsulation relates to property decorators
# ============================================================
"""
Property decorators (@property, @x.setter, @x.deleter) are Python's
clean way of implementing encapsulation: the underlying attribute
stays "private" (prefixed with an underscore), while access,
validation, and deletion are all routed through controlled methods -
yet the calling code still uses simple attribute syntax (obj.attr),
combining data protection with a clean interface.
"""
class Employee2:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

emp = Employee2(50000)
emp.salary = 60000
print(emp.salary)
