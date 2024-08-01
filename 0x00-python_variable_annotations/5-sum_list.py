#!/usr/bin/env python3
"""
This module writes a type-annotated function sum_list which takes
a list input_list of floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up the elements of a list of floats.

    Parameters:
    - input_list: A list of floats.

    Returns:
    - The sum of the floats in the list as a float.
    """
    return float(sum(input_list))
