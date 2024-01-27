#!/usr/bin/env python3
""" 0. Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function that takes two integer arguments page and page_size.
    return a tuple of size two containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
