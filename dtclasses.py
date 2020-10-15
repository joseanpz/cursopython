from dataclasses import dataclass, field


class Person:
    
    def __init__(self, name:str, gender:str, age:int):
        self.name = name
        self.gender = gender
        self.age = age


class Person:
    
    def __init__(self, name:str, gender:str, age:int):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return (self.__class__.__qualname__ + 
            f"(name={self.name}, gender={self.gender}, age={self.age})")

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.gender, self.age) == (other.name, other.gender, other.age)
        return NotImplemented    

    
class PersonOrdered(A):
    
    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.gender, self.age) < (other.name, other.gender, other.age)
        return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.gender, self.age) <= (other.name, other.gender, other.age)
        return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.gender, self.age) > (other.name, other.gender, other.age)
        return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.gender, self.age) >= (other.name, other.gender, other.age)
        return NotImplemented


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class PersonDC:
    name: str
    gender: str
    age: int




