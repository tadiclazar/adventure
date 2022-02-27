import random

from entity import Entity


class BossEnemy(Entity):
    """
    This class represents the boss enemies of the game.
    """
    def __init__(self, name, hp, mp, damage, armor, abilities, gold=0):
        """
        :param name: The name of the boss.
        :type name: str
        :param hp: Starting hit points of the boss.
        :type hp: int
        :param mp: Starting mana of the boss.
        :type mp: int
        :param damage: The damage output of the boss.
        :type damage: int
        :param armor: Armor class of the boss.
        :type armor: int
        :param abilities: special abilities of the boss.
        :type abilities: list
        :param gold: The amount of gold that boss is worth. Make it big.
        :type: gold: int
        """
        super().__init__(name, hp, damage, armor, gold)
        self.mp = mp
        self.max_mp = mp
        self.abilities = abilities
        self.e_class = "Boss Enemy"

    def __str__(self):

        return f"Name: {self.name}\tClass: {self.e_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n"

    def use_special(self, target):
        """
        Use the special ability of the boss on the target.

        :param target: The target of the ability.
        :type target: Entity
        :return: Nothing.
        :rtype: None
        """
        chosen_ability = random.choice(self.abilities)

        if chosen_ability is not None:
            chosen_ability(target)
            self.mp -= 4

    def replenish(self, amount):
        """
        special ability of the boss. replenishes both hit points and mana by given amount.
        :param amount: The amount replenished.
        :type amount: int
        :return: Nothing.
        :rtype: None
        """
        max_mp = self.max_mp

        if self.mp + amount < max_mp:
            self.mp += amount
        else:
            self.mp = max_mp
        
        self.heal(amount)
