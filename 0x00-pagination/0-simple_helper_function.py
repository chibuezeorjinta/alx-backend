#!/usr/bin/env python3
"""
Pagination helper function
"""
from typing import Tuple, Dict, List


def index_range(page: int, page_size: int,
                **kwargs: Dict[str, int]) -> Tuple[int, int]:
    """
    Get the range of data points to be returned.
    Args:
            page: int = particular page number, depends on the page_size param.
            page_size: int = size of each page datadump
            kwargs: dict = a key value pair still containing only
                page and page_size, but for alternative input method

    Return: tuple containing the start and end(exclusive)
        indexes of the datadump
    """
    out: List[int, int] = [0, 0]
    if (kwargs):
        if (len(kwargs) == 2):
            if (kwargs['page'] < 1):
                raise ValueError('page must be greater than 0')
            out[0] = (kwargs['page'] - 1) * kwargs['page_size']
            out[1] = kwargs['page'] * kwargs['page_size']
            return tuple(out)
        else:
            raise ValueError('Value pairs must be 2 in number')
    else:
        if (page < 1):
            raise ValueError('page must be greater than 0')
        out[0] = (page - 1) * page_size
        out[1] = page * page_size
        return tuple(out)
