from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable

if TYPE_CHECKING:
    from entity import EntityClasses


def get_class_as_str(entity_class: EntityClasses) -> str:
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


def number_key_dict(iterable: Iterable) -> dict[str, Any]:
    return {str(n): item for n, item in enumerate(iterable, start=1)}
