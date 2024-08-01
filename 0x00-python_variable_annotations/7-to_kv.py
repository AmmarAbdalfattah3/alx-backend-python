#!/usr/bin/env python3
"""
This script writes a type-annotated function to_kv that takes
a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element
is the square of the int/float v and should be annotated as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number, and returns a tuple where the first element
    is the string and the second element is the square of the number.

    Args:
        k (str): A string value.
        v (Union[int, float]): A number that can be an integer or a float.

    Returns:
        Tuple[str, float]: A tuple where:
            - The first element is the input string `k`.
            - The second element is the square of the input number `v`.

    Example:
        >>> to_kv("eggs", 3)
        ('eggs', 9.0)
        >>> to_kv("school", 0.02)
        ('school', 0.0004)
    """
    return (k, float(v * v))
