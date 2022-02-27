from helper_funcs import number_key_dict


def travel_to(prev_location, locations):
    """
    Transport the party to a location from the list of available locations.

    :param prev_location: The previous location of the party.
    :type prev_location: str
    :param locations: The list of available locations.
    :type locations: list[str]
    :return: Either the previous location or the new location, depending on player choice.
    :rtype: str
    """
    if prev_location == "Derelict Shrine":
        locations = locations + ["Mausoleum"]

    available_locations = number_key_dict(locations)
    loc_string = "\n".join(f"\t{i}) {loc}" for i, loc in available_locations.items())
    print(loc_string)

    choice = input("\nChoose location:\n")
    if choice in available_locations:
        return available_locations[choice]
    else:
        print("You can't go there!\n")
        return prev_location
