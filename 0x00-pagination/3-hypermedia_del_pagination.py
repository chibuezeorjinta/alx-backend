#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        by creating a new counter that keeps expanding the
        next index will be found consistently
        Args:
                index: int = given start index
                page_size: int = size of data packet
        Return: Dict = Data packet
        """
        dataset = self.indexed_dataset()
        assert index >= 0 and index < len(dataset) - 1
        page_data = []
        next_index = index
        last_index = page_size + index
        i = index
        while i < last_index:
            row = dataset.get(i)
            if not row:
                last_index += 1
            else:
                page_data.append(row)
            next_index += 1
            i += 1
        data = page_data
        return {
            "page_size": page_size,
            "data": data,
            "next_index": next_index,
            "index": index
        }
