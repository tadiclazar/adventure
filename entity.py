import random
from enum import Enum, auto
from helper_funcs import get_class_as_str


class EntityClasses(Enum):
    BaseEntity = auto()
    Warrior = auto()
    Rogue = auto()
    Mage = auto()
    Summoned = auto()
    BossMonster = auto()


class Entity:
    def __init__(self, name, e_class, hp, mp, damage, armor, mage_spells=None, gold=0, is_summoned=False):
        self.name = name
        self.e_class = e_class
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.armor = armor
        self.gold = gold
        self.mp = mp
        self.max_mp = mp
        self.mage_spells = mage_spells
        self.is_summoned = is_summoned

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
               f"Known Spells:\n{known_spells}\n"

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

    def heal(self, amount):
        max_hp = self.max_hp

        if self.hp + amount < max_hp:
            self.hp += amount
        else:
            self.hp = max_hp

    def attack(self, target):
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

    def replenish(self, amount):
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp
        
        self.heal(amount)

    def unsummon(self, party):
        self.is_summoned = False
        self.hp = 0
        party.remove(self)
