import random

from entity import Entity, EntityClasses
from boss_enemy import BossEnemy
from spell import Spell, SpellType
from mage import Mage, SummonedCreature
from spell_funcs import cast_firebolt, cast_raise_dead, cast_black_miasma, charm_kiss
from helper_funcs import number_key_dict


def add_enemies(location):
    if location == "Graveyard":
        return [
            Entity("Skeleton", EntityClasses.Warrior, 25, 6, 1, gold=15),
            Entity("Skeleton", EntityClasses.Warrior, 25, 6, 1, gold=15),
            Entity("Skeleton Warrior", EntityClasses.Warrior, 30, 8, 2, gold=25),
        ]
    elif location == "Abandoned Mine":
        return [
            Entity("Gnome", EntityClasses.Warrior, 20, 5, 0, gold=10),
            Entity("Gnome", EntityClasses.Warrior, 20, 5, 0, gold=10),
            Mage("Gnome Rune-master", EntityClasses.Warrior, 28, 6, 6, 1, mage_spells=[
                Spell("Firebolt", SpellType.Offensive, 2, 8, "The Firebolt Spell of Gnome Rune-master.", cast_firebolt)
            ], gold=30),
        ]
    elif location == "Derelict Shrine":
        return [
            Entity("Acolyte", EntityClasses.Mage, 18, 5, 0, gold=15),
            Entity("Acolyte", EntityClasses.Mage, 18, 5, 0, gold=15),
            Mage("Necromancer", EntityClasses.Mage, 27, 8, 7, 1, mage_spells=[
                Spell("Raise Dead", SpellType.Summoning, 4, 9,
                             "This spell raises one Skeleton from it's earthen grave.", cast_raise_dead)
            ], gold=35)
        ]
    elif location == "Mausoleum":
        return [BossEnemy("Bone Horror", EntityClasses.BossMonster, 50, 12, 10, 2, [cast_black_miasma], gold=120)]
    elif location == "Underwater Cave":
        return [
            Mage("Nymph", EntityClasses.Mage, 20, 8, 7, 0, mage_spells=[Spell("Charm Kiss", SpellType.Offensive, 4, 4, "Spell lowers opponent's armor.", charm_kiss)]),
            Mage("Nymph", EntityClasses.Mage, 20, 8, 7, 0, mage_spells=[Spell("Charm Kiss", SpellType.Offensive, 4, 4, "Spell lowers opponent's armor.", charm_kiss)])
        ]
    else:
        return []


def enemy_attack(enemy_party, player_party):
    print("\nThe enemy party begins their attack!\n")

    for enemy in enemy_party:
        print(f"{enemy.name} is moving!\n")
        target = random.choice(player_party)

        if isinstance(enemy, Mage):
            available_spells = number_key_dict(enemy.mage_spells)
            chosen_spell = random.choice(tuple(available_spells))

            chosen_spell = available_spells[chosen_spell]

            if chosen_spell.cost > enemy.mp:
                print(f"{enemy.name} has no mana for {chosen_spell.name}!\n")
                enemy.attack(target)
            else:
                if chosen_spell.stype == SpellType.Offensive:
                    enemy.cast_spell(chosen_spell, target)
                    if target.is_dead():
                        print(f"Player party has lost {target.name}!\n")
                        player_party.remove(target)

                elif chosen_spell.stype == SpellType.Summoning:
                    enemy.cast_spell(chosen_spell, enemy_party)

        elif isinstance(enemy, BossEnemy):
            chosen_action = random.randint(1, 2)
            if chosen_action == 1 and enemy.mp >= 4:
                enemy.use_special(target)
            else:
                enemy.attack(target)
        else:
            enemy.attack(target)

        if target.is_dead():
            print(f"The player party lost {target.name}!\n")
            player_party.remove(target)


def party_member_use_magic(member, chosen_spell, enemy_party, player_party):
    if chosen_spell.stype == SpellType.Offensive:
        enemy_dict = number_key_dict(enemy_party)
        targets = "\n".join(f"\t{i}) {enemy.name}" for i, enemy in enemy_dict.items())
        print(targets)

        target_enemy = input(f"\nChoose target for {member.name}: ")
        if target_enemy in enemy_dict:
            target = enemy_dict[target_enemy]
            member.cast_spell(chosen_spell, target)
            if target.is_dead():
                print(f"Enemy party has lost {target.name}!\n")
                enemy_party.remove(target)
        else:
            print("Invalid target!\n")

    elif chosen_spell.stype == SpellType.Summoning:
        print(f"{member.name} casts a Summoning spell!\n")
        member.cast_spell(chosen_spell, player_party)

    elif chosen_spell.stype == SpellType.Defensive:
        ally_dict = number_key_dict(player_party)
        friendly_targets = "\n".join(f"\t{i}) {member.name}" for i, member in ally_dict.items())
        print(friendly_targets)
        target_ally = input(f"\nChoose target for {member.name}: ")

        if target_ally in ally_dict:
            the_target = ally_dict[target_ally]
            print(f"{member.name} casts a Defensive spell!\n")
            member.cast_spell(chosen_spell, the_target)
        else:
            print("Invalid target!\n")


def party_member_attack(member, enemy_party):
    enemy_dict = number_key_dict(enemy_party)
    targets = "\n".join(f"\t{i}) {enemy.name}" for i, enemy in enemy_dict.items())
    print(targets)

    enemy_choice = input(f"Choose target for {member.name}:\n")

    if enemy_choice in enemy_dict:
        target = enemy_dict[enemy_choice]
        member.attack(target)

        if target.is_dead():
            print(f"Enemy party has lost {target.name}!\n")
            enemy_party.remove(target)
    else:
        print("Invalid target!")


def battle_at(location, player_party):
    enemies = add_enemies(location)
    gold_gained = sum(random.randint(en_gold // 2, en_gold) for enemy in enemies if (en_gold := enemy.gold) > 0)

    print(f"Enemies at {location}:")
    enemy_str = "\n".join(f"\t{enemy.name}" for enemy in enemies)
    print(enemy_str, "\n")

    while True:
        if not player_party:
            print("\nYou lost the battle!\n")
            return 0

        for member in player_party:
            commands_prompt = "\t(A)ttack enemy\n" \
                              "\t(E)scape combat\n" \
                              "\tBattle (I)nfo\n" \

            if isinstance(member, Mage):
                commands_prompt += "\t(C)ast a spell\n"

            print(f"Enter your command for {member.name}: \n")
            command = input(commands_prompt)

            if command in ("a", "A"):
                if enemies:
                    party_member_attack(member, enemies)

            elif command in ("e", "E"):
                print(f"\nYour party escaped from combat!\n")
                return 0

            elif command in ("i", "I"):
                print("\nPlayer party:\n")
                for pm in player_party:
                    print(pm)
                print("\nEnemy party:\n")
                for en in enemies:
                    print(en)

            elif command in ("c", "C"):
                if enemies:
                    available_spells = number_key_dict(member.mage_spells)
                    spells_str = "\n".join(f"{i}) Name: {s.name}\tCost: {s.cost}\tPower: {s.power}\nDescription:\n{s.desc}\n"
                                           for i, s in available_spells.items())
                    spells_str += f"\nMana available: {member.mp}\n"
                    print(spells_str)

                    chosen_spell = input("Choose spell to cast: ")
                    chosen_spell = available_spells[chosen_spell]

                    party_member_use_magic(member, chosen_spell, enemies, player_party)

            if not enemies:
                party_summoned = (crit for crit in player_party if isinstance(crit, SummonedCreature))
                for crit in party_summoned:
                    crit.unsummon(player_party)
                print(f"\nYou have won the battle!\nGold earned: {gold_gained}.")
                return gold_gained

        if enemies:
            enemy_attack(enemies, player_party)
