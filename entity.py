from __future__ import annotations

import random
from enum import Enum, auto
from typing import TYPE_CHECKING
from helper_funcs import get_class_as_str

if TYPE_CHECKING:
    from mage import Mage


class EntityClasses(Enum):
    BaseEntity = auto()
    Warrior = auto()
    Rogue = auto()
    Mage = auto()
    Summoned = auto()
    BossMonster = auto()


class Entity:
    def __init__(self, name: str, e_class: EntityClasses, hp: int, damage: int, armor: int, gold: int = 0):
        self.name = name
        self.e_class = e_class
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.armor = armor
        self.gold = gold

    def __str__(self) -> str:
        the_class = get_class_as_str(self.e_class)

        return f"Name: {self.name}\tClass: {the_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n"

    def is_dead(self) -> bool:
        if self.hp <= 0:
            return True
        return False

    def heal(self, amount: int) -> None:
        max_hp = self.max_hp

        if self.hp + amount < max_hp:
            self.hp += amount
        else:
            self.hp = max_hp

    def attack(self, target: "Entity" | Mage) -> None:
        dmg = self.damage - target.armor
        if dmg <= 0:
            print(f"The {self.name} does no damage to {target.name}!")

        defending = random.randint(0, 1) if (random.randint(target.armor * 10 - 1, 100)
                                             > random.randint((self.damage * 10) // 2 - 1, 100)) else 0

        if defending:
            print(f"{target.name} parries the {self.name}'s assault! The damage is lowered.\n")
            dmg //= 2
        if dmg > (target.armor * 2) and random.random() > 0.65:
            print(f"{self.name} scores a critical hit! The damage is doubled!\n")
            dmg *= 2

        print(f"{self.name} does {dmg} damage to {target.name}!\n")
        target.hp -= dmg
