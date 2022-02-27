from enum import Enum, auto

class SpellType(Enum):
    Offensive = auto()
    Defensive = auto()
    Summoning = auto()
    Global = auto()


class Spell:
    __slots__ = ("name", "stype", "cost", "power", "desc", "function")

    def __init__(self, name, stype, cost, power, desc, function):
        self.name = name
        self.stype = stype
        self.cost = cost
        self.power = power
        self.desc = desc
        self.function = function

    def __str__(self):
        return f"Name: {self.name}\tMana Cost: {self.cost}\n" \
               f"Power: {self.power}\nDescription:\n{self.desc}\n"
