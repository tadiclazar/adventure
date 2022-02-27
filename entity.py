import random


class Entity:
    """
    Base entity class. Subclass it to make other types.
    """
    def __init__(self, name, hp, damage, armor, gold=0):
        """
        :param name: Name of the entity.
        :type name: str
        :param hp: Starting hit points.
        :type hp: int
        :param damage: Damage output of the entity.
        :type damage: int
        :param armor: Armor class of the enemy.
        :type armor: int
        :param gold: The gold worth of the enemy, if any.
        :type gold: int
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.armor = armor
        self.gold = gold
        self.e_class = "Warrior"

    def __str__(self):

        return f"Name: {self.name}\tClass: {self.e_class}\n" \
               f"Current HP: {self.hp}\tMax. HP: {self.max_hp}\tDamage: {self.damage}\n" \
               f"Armor Class: {self.armor}\n"

    def is_dead(self):
        """
        Check to see if the entity is dead or not.

        :return: True if the enemy is dead. False if not.
        :rtype: bool
        """
        if self.hp <= 0:
            return True
        return False

    def heal(self, amount):
        """
        Heals the entity by the given amount.

        :param amount: The amount to heal.
        :type amount: int
        :return: Nothing.
        :rtype: None
        """
        max_hp = self.max_hp

        if self.hp + amount < max_hp:
            self.hp += amount
        else:
            self.hp = max_hp

    def attack(self, target):
        """
        Attack the target entity. Deals physical damage.

        :param target: The target to attack.
        :type target: Entity
        :return: Nothing.
        :rtype: None
        """
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
