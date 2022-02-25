import random

from entity import Entity
from mage import Mage
from helper_funcs import get_class_as_str


class BossEnemy(Entity):
    def __init__(self, name, e_class, hp, mp, damage, armor, abilities, gold=0):
        super().__init__(name, e_class, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.abilities = abilities

    def __str__(self):
        the_class = get_class_as_str(self.e_class)

        return f"Name: {self.name}\tClass: {the_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n"

    def use_special(self, target):
        chosen_ability = random.choice(self.abilities)

        if chosen_ability is not None:
            chosen_ability(target)
            self.mp -= 4

    def replenish(self, amount):
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp
        
        self.heal(amount)
