#!/usr/bin/env python3
"""
This script augment the following code with the correct
duck-typed annotations:
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence containing elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence
    """
    if lst:
        return lst[0]
    else:
        return None
