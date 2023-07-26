#!/usr/bin/python3
"""Cache using the lifo architecture"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
	"""Inherit from basecache to impliment a lifo put algo"""
	def __init__(self):
		""" Initialize class instance."""
		super().__init__()
		self.keys = []

	def put(self, key, item):
		"""Put key and item into cache dict using lifo
		Args:
			key: dict key
			item: dict data
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
		"""Get data using key.
		Args:
			key = data key
		Return = Data from cache_data dict or None of key doesnt exist."""
		if key is not None and key in self.cache_data:
			return self.cache_data[key]
		return None
