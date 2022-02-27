from enum import Enum, auto


class SpellType(Enum):
    Offensive = auto()
    Defensive = auto()
    Summoning = auto()
    Global = auto()


class Spell:
    """
    Represents instances of spells.
    """
    __slots__ = ("name", "stype", "cost", "power", "desc", "function")

    def __init__(self, name, stype, cost, power, desc, function):
        """
        :param name: Name of the spell.
        :type name: str
        :param stype: Spell type (Offensive, Defensive, etc.).
        :type stype: SpellType
        :param cost: The mana cost of the spell.
        :type cost: int
        :param power: The power of the spell.
        :type power: int
        :param desc: The spell description.
        :type desc: str
        :param function: The actual function of the spell.
        """
        self.name = name
        self.stype = stype
        self.cost = cost
        self.power = power
        self.desc = desc
        self.function = function

    def __str__(self):
        return f"Name: {self.name}\tMana Cost: {self.cost}\n" \
               f"Power: {self.power}\nDescription:\n{self.desc}\n"
