from enum import Enum, auto
from typing import Callable
from mage import Mage
from entity import Entity
    

SpellFuncType = Callable[[Mage, Entity | Mage | list[Entity | Mage]], None]


class SpellType(Enum):
    Offensive = auto()
    Defensive = auto()
    Summoning = auto()
    Global = auto()


class Spell:
    __slots__ = ("name", "stype", "cost", "power", "desc", "function")

    def __init__(self, name: str, stype: SpellType, cost: int, power: int, desc: str, function: SpellFuncType):
        self.name = name
        self.stype = stype
        self.cost = cost
        self.power = power
        self.desc = desc
        self.function = function

    def __str__(self) -> str:
        return f"Name: {self.name}\tMana Cost: {self.cost}\n" \
               f"Power: {self.power}\nDescription:\n{self.desc}\n"
