#!/usr/bin/python3
"""Cache using the MRU architecture"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Like LRU, cre"""

    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Like LRC create a system that sends the most used
                key to the top of the stack.
                Args:
                        key = data key
                        item = data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Return item if key exists"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
