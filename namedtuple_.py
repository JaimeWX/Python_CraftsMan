from typing import NamedTuple

class Rectangle(NamedTuple):
    width: int
    height: int

rect = Rectangle(100,20)
print(rect.width)
print(rect.height)
print(rect)