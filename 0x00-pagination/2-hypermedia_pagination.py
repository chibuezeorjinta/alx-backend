#!/usr/bin/env python3
"""
Pagination helper function
"""
import csv
import math
from typing import Tuple, Dict, List, Any


def index_range(page: int, page_size: int,
                **kwargs: Dict[str, int]) -> Tuple[int, int]:
    """
    Get the range of data points to be returned.
    Args:
            page: int = particular page number, depends on the page_size param.
            page_size: int = size of each page datadump
            **kwags: dict = a key value pair still containing only page and
                page_size, but for alternative input method

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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a datadump within a given range

        Args:
            page: int = particular page number, depends on the page_size param.
            page_size: int = size of each page datadump

        Return: List[List] = List of data within the required range
        """
        DataSet = self.dataset()
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page > 0
        DataRange = index_range(page, page_size)
        DataEnd: int = len(DataSet)
        if (DataEnd < DataRange[0] or DataEnd < DataRange[1]):
            return []
        return DataSet[DataRange[0]: DataRange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get datadump with some metadata.
        Args:
            page: int = particular page number, depends on the page_size param.
            page_size: int = size of each page datadump
        Return: Dict = key value pair.
        """
        OutList = self.get_page(page, page_size)
        next_page: int
        prev_page: int
        total_pages = math.ceil(len(self.__dataset) / page_size)
        if page == total_pages:
            next_page = None
        else:
            next_page = page + 1
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        outDict = {
            'page_size': len(OutList),
            'page': page,
            'data': OutList,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return outDict
