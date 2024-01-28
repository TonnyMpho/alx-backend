#!/usr/bin/env python3
""" 1. Simple pagination """
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function that takes two integer arguments page and page_size.
    return a tuple of size two containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


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
        method that takes two integer arguments page with default value 1
        and page_size with default value 10
        if the input arguments are out of range for the dataset,
        return an empty list.
        """
        assert isinstance(page, int) and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset) or end <= 0:
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        method that takes two integer arguments page with default value 1
        and page_size with default value 10
        returns a dictionary containing key-value pairs
        """
        data = self.dataset()
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(data) / page_size)
        next_page = page + 1 if (page * page_size) < len(data) else None

        return {
                'page_size': len(page_data),
                'page': page,
                'data': page_data,
                'next_page': next_page,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages,
                }
