from helper_funcs import number_key_dict
from collections import namedtuple

Item = namedtuple("Item", ["name", "price", "description"], defaults=["None", 0.0, "Unknown"])

def shop_for_items(inventory, shop_items, cur_loc, party_gold):
    items_for_sale = number_key_dict(shop_items)
    item_str = "\n".join(f"{i}) {item.name}" for i, item in items_for_sale.items())
    print(item_str)
    print(f"\nWelcome to the Shop at {cur_loc}!\n")

    while True:
        player_choice = input("Please choose what you need! (Type 'done' when finished)\n")
        if player_choice in items_for_sale and party_gold > items_for_sale[player_choice].price:
            chosen = items_for_sale[player_choice]
            print(f"The party buys {chosen.name} for {chosen.price} gold pieces!\n")
            inventory.append(chosen)

        elif player_choice in items_for_sale and items_for_sale[player_choice].price > party_gold:
            print("The party does not have enough gold to buy this item!\n")
        elif player_choice not in items_for_sale and player_choice != "done":
            print("That item is not available for sale!\n")
        elif player_choice == "done":
            print("Leaving the shop...")
            break

