from entity import Entity
from spell import Spell


class Mage(Entity):
    """
    The Mage class. Instances of this class can cast spells.
    """
    def __init__(self, name, hp, mp, damage, armor, mage_spells, gold=0):
        """
        :param name: Name of the mage.
        :type name: str
        :param hp: The hit point of the mage.
        :type hp: int
        :param mp: The starting mana of the mage.
        :type mp: int
        :param damage: The base damage output of the mage.
        :type damage: int
        :param armor: The armor class of the mage.
        :type armor: int
        :param mage_spells: The spells the mage starts with, if any.
        :type mage_spells: list[Spell]
        :param gold: The gold worth of the mage, if it's an enemy.
        :type gold: int
        """
        super().__init__(name, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.mage_spells = mage_spells

    def __str__(self):
        if self.mage_spells:
            known_spells = "\n".join(f"{spell.name}" for spell in self.mage_spells)
        else:
            known_spells = "None"

        return f"Name: {self.name}\tClass: {self.e_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n" \
               f"Current Mana: {self.mp}\tMax. Mana: {self.max_mp}\n" \
               f"Known Spells:\n{known_spells}"

    def cast_spell(self, spell, target):
        """
        Cast the chosen spell on target.

        :param spell: Spell to cast.
        :type spell: Spell
        :param target: The target of the spell.
        :type target: Entity
        :return: Nothing.
        :rtype: None
        """
        if self.mp < spell.cost:
            print(f"\n{self.name} doesn't have enough mana to cast {spell.name}!\n")
        else:
            print(f"{self.name} casts {spell.name} and loses {spell.cost} mana!")
            self.mp -= spell.cost
            spell.function(self, target, spell.power)

    def learn_spell(self, spell):
        """
        Learn the spell and place it into the spellbook.

        :param spell: The spell to learn.
        :type spell: Spell
        :return: Nothing.
        :rtype: None
        """
        if spell in self.mage_spells:
            print(f"{self.name} already knows {spell.name}!\n")
        else:
            print(f"{self.name} memorizes {spell.name} in the spellbook!\n")
            self.mage_spells.append(spell)

    def rejuvenate(self, amount):
        """
        Restore mana to the caster by specified amount.

        :param amount: The amount of mana to restore.
        :type amount: int
        :return: Nothing.
        :rtype: None
        """
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp


class SummonedCreature(Entity):
    """
    Represents summoned creatures. They can be summoned by mages or bosses.
    """
    def __init__(self, name, hp, mp, damage, armor, gold=0):
        """
        :param name: Name of the summoned creature
        :type name: str
        :param hp: The hit points of the creature.
        :type hp: int
        :param mp: Mana points of the creature, if any.
        :type mp: int
        :param damage: The base damage output of the creature.
        :type damage: int
        :param armor: The armor class of the creature.
        :type armor: int
        :param gold: The gold worth of the creature, if any.
        :type gold: int
        """
        super().__init__(name, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.e_class = "Summoned Creature"
        self.is_summoned = True

    def unsummon(self, party):
        """
        Unsummon the creature and remove it from the party.

        :param party: The party the creature belongs to.
        :type party: list[Entity | Mage]
        :return: Nothing.
        :rtype: None
        """
        self.is_summoned = False
        self.hp = 0
        party.remove(self)
