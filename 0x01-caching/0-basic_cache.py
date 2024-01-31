#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        assign to the dictionary cache_data the item value for the key key.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in cache_data linked to key
        """
        if key:
            return self.cache_data.get(key, None)
