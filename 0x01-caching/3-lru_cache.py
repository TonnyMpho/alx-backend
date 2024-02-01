#!/usr/bin/env python3
""" LRU caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        assign to the dictionary cache_data the item value for the key key
        If the number of items in cache_data is higher that
        BaseCaching.MAX_ITEMS:
        discard the least recently used item (LRU algorithm)
        print DISCARD: with the key discarded and followed by a new line
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        else:
            return None
