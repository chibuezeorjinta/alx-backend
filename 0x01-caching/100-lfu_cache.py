#!/usr/bin/env python3
"""Cache using the LFU architecture"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Impliment caching using Lfu architecture"""

    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.keys = []
        self.freqCount = {}

    def put(self, key, item):
        """Append a new value pair and remove the least
        frequent key if max_items is reached.
                Args:
                        key = data key
                        item = data
        """
        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS and
                    key not in self.keys):
                discard = self.keys.pop(self.keys.index(self.leastfreq()))
                del self.cache_data[discard]
                del self.freqCount[discard]
                print('DISCARD: {:s}'.format(discard))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.freqCount[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.freqCount[key] += 1

    def get(self, key):
        """Return item of key if it exists."""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.freqCount[key] += 1
            return self.cache_data[key]
        return None

    def leastfreq(self):
        """A method to find the fequency of use of a key"""
        items = list(self.freqCount.items())
        freqs = [item[1] for item in items]
        least = min(freqs)
        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return key
