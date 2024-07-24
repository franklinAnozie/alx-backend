#!/usr/bin/env python3
""" simple helper fxn """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ fxn to get range """
    start_idx: int = (page - 1) * page_size
    end_idx: int = start_idx + page_size
    return (start_idx, end_idx)
