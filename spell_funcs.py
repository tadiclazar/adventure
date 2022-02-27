import random
from mage import SummonedCreature, Mage


def cast_raise_dead(caster, party, spell_power):
    """
    Spell function for Raise Dead spell. Raises one skeleton from the grave, to fight for the caster's party.

    :param caster: The mage caster.
    :type caster: Mage
    :param party: The party where to place skeleton.
    :type party: list
    :param spell_power: The power of the spell.
    :type spell_power: int
    :return: Nothing.
    :rtype: None
    """
    skeleton_hp = spell_power * 2
    skeleton_dmg = spell_power // 2 + 1
    skeleton_armor = spell_power // 3

    skeleton = SummonedCreature("Skeleton", skeleton_hp, 0, skeleton_dmg, skeleton_armor)
    print(f"\n{caster.name} casts Raise Dead! A Skeleton rises from it's earthen grave to fight!\n")
    party.append(skeleton)


def cast_firebolt(caster, target, spell_power):
    """
    The function for the Firebolt spell. Burns the target creature for spell damage points.

    :param caster: The mage caster.
    :type caster: Mage
    :param target: The target of the Firebolt spell.
    :type target: Mage
    :param spell_power: The power of the spell. Determines damage.
    :type spell_power: int
    :return: Nothing.
    :rtype: None
    """
    if not target:
        print("\nThere is no target!\n")
        return None

    spell_damage = random.randint(spell_power, spell_power * 3)
    saving_throw = random.random() > ((spell_power / 100) + 0.10)
    if saving_throw:
        spell_damage //= 2
        print(f"\n{target.name} saves against the Spell!\n")

    print(f"{caster.name} casts Firebolt on {target.name}!\n"
        f"{target.name} takes {spell_damage} damage!\n")
    target.hp -= spell_damage


def cast_healing(caster, target, spell_power):
    """
    The function for the Healing spell. Heals the friendly target. Amount is related to spell power.

    :param caster: The mage caster.
    :type caster: Mage
    :param target: The friendly target.
    :type target: Mage
    :param spell_power: The amount to heal.
    :type spell_power: int
    :return: Nothing.
    :rtype: None
    """
    if target.hp == target.max_hp:
        return None

    print(f"{caster.name} casts Healing on {target.name}, healing it for {spell_power} hit points!\n")
    target.heal(spell_power)


def cast_black_miasma(target):
    """
    The Boss ability function. Target suffers the chocking damage relative to the spell's power.

    :param target: The target of the ability.
    :type target: Mage
    :return: Nothing.
    :rtype: None
    """
    power = 16
    saving_throw = 1 if (target.hp > (target.max_hp // 2 + random.randint(1, target.armor))) else 0

    if saving_throw:
        power /= 2
        print(f"{target.name} saves against Black Miasma! The damage is halved!\n")

    target.hp -= power
    print(f"Black Miasma does {power} damage to {target.name}, chocking the life force from the body.\n")
