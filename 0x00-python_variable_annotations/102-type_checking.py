#!/usr/bin/env python3
"""
This module uses mypy to validate the following
piece of code and apply any necessary changes.
"""

from typing import List

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on a list by repeating each element `factor` times.

    Args:
        lst (List[int]): The list to zoom in on.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        List[int]: A new list where each element is repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Example usage
array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Correcting the factor to be an integer
zoom_3x = zoom_array(array, 3)
