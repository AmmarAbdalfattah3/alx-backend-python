#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up the elements of a list containing both integers and floats.

    Parameters:
    - mxd_lst: A list of integers and floats.

    Returns:
    - The sum of the elements in the list as a float.
    """
    return float(sum(mxd_lst))
