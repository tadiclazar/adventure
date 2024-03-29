import random
from entity import Entity, EntityClasses


def cast_raise_dead(caster, party, spell_power):
    skeleton_hp = spell_power * 2
    skeleton_dmg = spell_power // 2 + 1
    skeleton_armor = spell_power // 3

    skeleton = Entity("Skeleton", EntityClasses.Summoned, skeleton_hp, 0, skeleton_dmg, skeleton_armor, is_summoned=True)
    print(f"\n{caster.name} casts Raise Dead! A Skeleton rises from it's earthen grave to fight!\n")
    party.append(skeleton)


def cast_firebolt(caster, target, spell_power):
    if not target:
        print("\nThere is no target!\n")
        return None

    spell_damage = random.randint(spell_power, spell_power * 3)
    saving_throw = random.random() > ((spell_power / 100) + 0.10)
    if saving_throw:
        spell_damage //= 2
        print(f"\n{target.name} saves against the spell!\n")

    print(f"{caster.name} casts Firebolt on {target.name}!\n"
        f"{target.name} takes {spell_damage} damage!\n")
    target.hp -= spell_damage


def charm_kiss(caster, target, spell_power):
    if not target:
        print("\nThere is no target!\n")
        return None

    saving_throw = random.random() > ((spell_power / 100) + 0.15)
    effect = spell_power // 2
    print(f"{caster.name} tries to seduce {target.name}!")

    if saving_throw:
        print(f"{target.name} saves against the spell and is unaffected!\n")
    else:
        if target.armor == 1:
            target.armor = 0
            print(f"{target.name} is seduced and has lowered defenses to 0!\n")
        elif target.armor >= effect:
            target.armor -= effect
            print(f"{target.name} is seduced and has lowered defenses by {effect}!\n")
        elif target.armor == 0:
            print(f"{target.name} has no armor but a will of a warrior! The charm is resisted!\n")
            return None


def cast_healing(caster, target, spell_power):
    if target.hp == target.max_hp:
        return None

    print(f"{caster.name} casts Healing on {target.name}, healing it for {spell_power} hit points!\n")
    target.heal(spell_power)


# TODO: GLOBAL SPELL, FIND A WAY TO SEPARATE THESE
def cast_black_miasma(caster, target, spell_power):
    dmg = 0
    for pm in target:
        saving_throw = 1 if (pm.hp > (pm.max_hp // 2 + random.randint(0, pm.armor))) else 0
        if saving_throw:
            dmg = int(spell_power / 2)
            print(f"{pm.name} saves against Black Miasma! The damage is halved!\n")
        else:
            dmg = int(spell_power)

        pm.hp -= int(dmg)
        print(f"Black Miasma does {dmg} damage to {pm.name}, chocking the life force from the body.\n")
