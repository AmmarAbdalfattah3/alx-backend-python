#!/usr/bin/env python3
"""
This module returns values, add type annotations to the function
"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary based on a key.

    Args:
        dct (Mapping[Hashable, T]): A dictionary-like mapping.
        key (Hashable): The key.
        default (Union[T, None], optional): The default value.

    Returns:
        Union[T, None]: The value associated with the key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
