#!/usr/bin/env python3
"""implement a cache following the fifo architecture"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
	"""Cache class according to FIFO"""
	def __init__(self):
		"""Constructor method"""
		super().__init__()
	
	def put(self, key, item):
		"""Put method for appending items"""
		if key is None:
			return
		if item is None:
			return
		if len(self.cache_data) == BaseCaching.MAX_ITEMS:
			keyList = list(self.cache_data.keys())
			self.cache_data.pop(keyList[0])
			print("DISCARD: {}".format(keyList[0]))
		self.cache_data[key] = item
	
	def get(self, key):
		"""
		retrieve an entry using its key
		Args:
			key: dict key
		Return = data related to key or none if not found"""
		if key is None:
			return None
		if key not in self.cache_data.keys():
			return None
		return self.cache_data[key]
