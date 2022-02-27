from typing import Iterable


def number_key_dict(iterable):
    """
    Make a dictionary where the keys are string numbers starting from 1.
    The values are whatever was in the passes iterable.
    :param iterable: The iterable of pretty much anything.
    :type iterable: Iterable
    :return: The dictionary of string keys and values.
    :rtype: dict[str, Any]
    """
    return {str(n): item for n, item in enumerate(iterable, start=1)}
