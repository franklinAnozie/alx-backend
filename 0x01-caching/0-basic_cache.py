#!/usr/bin/python3
""" basic_cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache Class """
    def __init__(self):
        """ init fxn """
        super().__init__()

    def put(self, key, item):
        """ sets a cache """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """ gets a cache """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
