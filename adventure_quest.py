import sys

from entity import Entity, EntityClasses
from mage import Mage
from spell import Spell, SpellType
from combat_funcs import battle_at
from world_funcs import travel_to
from spell_funcs import cast_firebolt, cast_raise_dead, cast_healing


def main():
    print("Welcome to the Adventure Game!\nExplore the world and discover it's secrets!\n")
    print("You are controlling a small party of adventurers: "
          "Warrior named Aidan,\nRogue by the name of Morena and a Mage called Jasper!\n")

    battle_locations = ["Graveyard", "Abandoned Mine", "Derelict Shrine"]
    towns = ["Town Tristram"]
    current_location = "Town Tristram"

    warrior = Entity("Aidan", EntityClasses.Warrior, 35, 9, 3)
    rogue = Entity("Morena", EntityClasses.Rogue, 30, 8, 1)
    mage = Mage("Jasper", EntityClasses.Mage, 20, 10, 5, 0, mage_spells=[], gold=0)

    player_party = [warrior, rogue, mage]

    party_gold = 0

    firebolt_spell = Spell("Firebolt", SpellType.Offensive, 2, 9, "This spell burns the target creature and"
                                                                  " does fire damage. The damage is " \
                                                                  "deduced from spell's power.", cast_firebolt)
    raise_dead_spell = Spell("Raise Dead", SpellType.Summoning, 4, 8,
                             "Raises one Skeleton to fight for the caster's party until the end of combat.", cast_raise_dead)
    healing_spell = Spell("Healing", SpellType.Defensive, 3, 8,
                          "Heals the target for the amount equivalent to spell's power.\n", cast_healing)

    while True:
        if not player_party:
            print("Game Over!")
            input("Press Enter to quit.")
            break
        command_prompts = "Choose command:\n" \
                          "\t(Q)uit\n" \
                          "\t(T)ravel to:\n" \
                          "\t(E)xamine the area\n" \
                          "\tParty (I)nfo\n"

        if current_location in towns:
            command_prompts += "\t(R)est at Town Inn\n"

        command = input(command_prompts)

        if command in ("q", "Q"):
            print("See you later...")
            sys.exit(0)

        elif command in ("t", "T"):
            locations = towns + battle_locations
            prev_location = current_location
            current_location = travel_to(prev_location, locations)
            print(f"The party travels to {current_location}!\n")

        elif command in ("r", "R"):
            if current_location in towns:
                print(f"\nThe party rests at the Inn in {current_location}.\n")
                for pm in player_party:
                    pm.heal(300)
                    if isinstance(pm, Mage):
                        pm.rejuvenate(100)
            else:
                print("\nThe party can only rest while in Town!\n")

        elif command in ("e", "E"):
            print(f"\nThe party is currently at {current_location}.\n")

            if current_location == "Abandoned Mine" and mage in player_party:
                print(f"The party finds {firebolt_spell.name} spell!")
                mage.learn_spell(firebolt_spell)
            elif current_location == "Derelict Shrine" and mage in player_party:
                print(f"The party finds {raise_dead_spell.name} spell!")
                mage.learn_spell(raise_dead_spell)
            elif current_location == "Graveyard" and mage in player_party:
                print(f"The party finds {healing_spell.name} spell!\n")
                mage.learn_spell(healing_spell)

            if current_location in battle_locations + ["Mausoleum", "Underwater Cave"]:
                battle_prompt = input(f"Do you wish to battle monsters at {current_location}? (y/n)\n")
                if battle_prompt in ("y", "Y"):
                    party_gold += battle_at(current_location, player_party)
                else:
                    pass
            else:
                print("You can't battle monsters here!")

        elif command in ("i", "i"):
            for pm in player_party:
                print(pm)
            print(f"\nThe party has {party_gold} gold coins.\n")

        else:
            print("Invalid command!\n")


if __name__ == '__main__':
    main()
