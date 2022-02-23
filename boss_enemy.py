from __future__ import annotations

import random
from typing import TYPE_CHECKING, Callable

from entity import Entity
from mage import Mage
from helper_funcs import get_class_as_str

if TYPE_CHECKING:
    from entity import EntityClasses

AbilityFunc = Callable[[Entity], None]


class BossEnemy(Entity):
    def __init__(self, name: str, e_class: EntityClasses, hp: int, mp: int, damage: int,
                 armor: int, abilities: list[AbilityFunc], gold: int = 0):
        super().__init__(name, e_class, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.abilities = abilities

    def __str__(self) -> str:
        the_class = get_class_as_str(self.e_class)

        return f"Name: {self.name}\tClass: {the_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n"

    def use_special(self, target: Entity) -> None:
        chosen_ability = random.choice(self.abilities)

        if chosen_ability is not None:
            chosen_ability(target)
            self.mp -= 4

    def replenish(self, amount: int) -> None:
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp
        
        self.heal(amount)
