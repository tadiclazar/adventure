from __future__ import annotations

from typing import TYPE_CHECKING
from entity import Entity
from helper_funcs import get_class_as_str

if TYPE_CHECKING:
    from entity import EntityClasses
    from spell import SpellFuncType
    from spell import Spell


class Mage(Entity):
    def __init__(self, name: str, e_class: EntityClasses, hp: int, mp: int, damage: int,
                 armor: int, mage_spells: list[SpellFuncType], gold: int = 0):
        super().__init__(name, e_class, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.mage_spells = mage_spells

    def __str__(self) -> str:
        the_class = get_class_as_str(self.e_class)

        if self.mage_spells:
            known_spells = "\n".join(f"{spell.name}" for spell in self.mage_spells)
        else:
            known_spells = "None"

        return f"Name: {self.name}\tClass: {the_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n" \
               f"Current Mana: {self.mp}\tMax. Mana: {self.max_mp}\n" \
               f"Known Spells:\n{known_spells}"

    def cast_spell(self, spell: Spell, target: "Entity" | "Mage") -> None:
        if self.mp < spell.cost:
            print(f"\n{self.name} doesn't have enough mana to cast {spell.name}!\n")
        else:
            print(f"{self.name} casts {spell.name} and loses {spell.cost} mana!")
            self.mp -= spell.cost
            spell.function(self, target, spell.power)

    def learn_spell(self, spell: Spell) -> None:
        if spell in self.mage_spells:
            print(f"{self.name} already knows {spell.name}!\n")
        else:
            print(f"{self.name} memorizes {spell.name} in the spellbook!\n")
            self.mage_spells.append(spell)

    def rejuvenate(self, amount: int) -> None:
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp


class SummonedCreature(Entity):
    def __init__(self, name: str, e_class: EntityClasses, hp: int, mp: int, damage: int, armor: int, gold: int = 0):
        super().__init__(name, e_class, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.is_summoned = True

    def unsummon(self, party: list[Mage | "SummonedCreature"]) -> None:
        self.is_summoned = False
        self.hp = 0
        party.remove(self)
