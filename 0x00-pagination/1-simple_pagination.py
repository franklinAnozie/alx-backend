#!/usr/bin/env python3
""" simple pagination """

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ fxn to get range """
    start_idx: int = (page - 1) * page_size
    end_idx: int = start_idx + page_size
    return (start_idx, end_idx)


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
        """ get page """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        idx: Tuple[int, int] = index_range(page, page_size)
        lst: List[int, int] = self.dataset()
        if idx[0] >= len(lst):
            return []
        return lst[idx[0]: idx[1]]
