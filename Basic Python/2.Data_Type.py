"""
##!    Python DataTypes => Integer, Float, String, Boolean, None

##!    Python Sequencial DataTypes => List, Tuple, Set, Dictionary

"""

a = 5        # intiger
print("Type of a =", type(a))

b = 5.4      # float
print("Type of b =", type(b))


c = "rakib"  # string
print("Type of c =", type(c))



d = True   # or False  # Boolean
print("Value of d =", d)
print("Type of d =", type(d))



e = (5, 6, 8, "hassan", 8, 2)      # Tuple 
print("Type of e =", type(e))

f = [12, 45.50, 'muna', 12]        # List
print("Type of f =", type(f))

g = {5, 7, 9}                      # Set
print("Type of g =", type(g))


h = {"name": "rakib", "roll":12}  # Dictionary
print("Type of a =", type(h))


# Type Custing

ab = float(a)
print("Value of ab =", ab)
print("Type of ab  =", type(ab))



ab = int(a)
print("Value of ab =", ab)
print("Type of ab  =", type(ab))


##! To format a floating-point number in Python
a = 10.545456456564

##? 1. Using round() function
rounded_a = round(a, 2)
print(rounded_a)   ## Result = 10.55


##? 2. Using string formatting with format()
formatted_a = "{:.2f}".format(a)
print(formatted_a)  ## Result = 10.55


##? 3. Using f-strings (formatted string literals)
formatted_a = f"{a:.2f}"
print(formatted_a)  ## Result = 10.55


##? 4. Using Decimal from decimal module
from decimal import Decimal, ROUND_HALF_UP

a = Decimal("10.545456456564")
formatted_a = a.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(formatted_a)   ## Result = 10.55





##! Define Python Data Types
from typing import List, Dict, Tuple, Set, Optional, Union, Callable

# Basic Types
a: int = 10
b: float = 10.5
c: str = "Hello"
d: bool = True

# Complex Types
e: List[int] = [1, 2, 3]
f: Tuple[int, float, str] = (1, 2.5, "Hello")
g: Set[str] = {"apple", "banana", "cherry"}
h: Dict[str, int] = {"one": 1, "two": 2}

# Optional and Union Types
i: Optional[int] = None
j: Union[int, str] = "Hello"

a: List[Union[str, int, float, Dict[str, Union[float, str]]]] = ['rakib', 10, 'dhaka', 3.36, {'ssc': 3.5, 'school': 'LMSC'}]



# # Callable Type
# def add(a: int, b: int) -> int:
#     return a + b

# k: Callable[[int, int], int] = add

# # Custom Class Type
# class MyClass:
#     def __init__(self, value: int):
#         self.value = value

# l: MyClass = MyClass(10)