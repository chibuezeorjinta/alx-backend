#!/usr/bin/python3
"""Cache using the LRC architecture"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class to impliment a caching system using the LRC algo"""
    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """in LRC create a system that send the a key to the top of the queue whenever it is used.
        Args:
            key = data key
            item: data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Return item associated with key if it exists"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
