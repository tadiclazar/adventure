from entity import Entity
from helper_funcs import get_class_as_str


class Mage(Entity):
    def __init__(self, name, e_class, hp, mp, damage, armor, mage_spells, gold=0):
        super().__init__(name, e_class, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.mage_spells = mage_spells

    def __str__(self):
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

    def cast_spell(self, spell, target):
        if self.mp < spell.cost:
            print(f"\n{self.name} doesn't have enough mana to cast {spell.name}!\n")
        else:
            print(f"{self.name} casts {spell.name} and loses {spell.cost} mana!")
            self.mp -= spell.cost
            spell.function(self, target, spell.power)

    def learn_spell(self, spell):
        if spell in self.mage_spells:
            print(f"{self.name} already knows {spell.name}!\n")
        else:
            print(f"{self.name} memorizes {spell.name} in the spellbook!\n")
            self.mage_spells.append(spell)

    def rejuvenate(self, amount):
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp


class SummonedCreature(Entity):
    def __init__(self, name, e_class, hp, mp, damage, armor, gold=0):
        super().__init__(name, e_class, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.is_summoned = True

    def unsummon(self, party):
        self.is_summoned = False
        self.hp = 0
        party.remove(self)
