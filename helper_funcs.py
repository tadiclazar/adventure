def get_class_as_str(entity_class):
    if entity_class == entity_class.BaseEntity:
        return "Base Entity"
    elif entity_class == entity_class.Warrior:
        return "Warrior"
    elif entity_class == entity_class.Rogue:
        return "Rogue"
    elif entity_class == entity_class.Mage:
        return "Mage"
    elif entity_class == entity_class.BossMonster:
        return "Boss"
    else:
        return "Unidentified"


def number_key_dict(iterable):
    return {str(n): item for n, item in enumerate(iterable, start=1)}
