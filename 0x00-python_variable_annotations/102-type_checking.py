#!/usr/bin/env python3
"""
This module uses mypy to validate the following
piece of code and apply any necessary changes.
"""


from typing import List, Union


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of a list by repeating each element

    Args:
        lst (List[int]): The list of integers to be zoomed.

    Returns:
        List[int]: A new list with each element repeated 'factor' times.

    Raises:
        ValueError: If factor is not an integer.
    """
    if not isinstance(factor, int):
        raise ValueError("Factor must be an integer.")

    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Correctly pass an integer as factor
zoom_3x = zoom_array(array, 3)
