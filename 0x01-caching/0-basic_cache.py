#!/usr/bin/env python3
"""implement a basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
	"""
	class for a basicc cache system without limit.
	inherites from the basecaching class
	"""
	def __init__(self):
		"""Constructor method"""
		super().__init__()
	
	def put(self, key, item):
		"""
		Put items in cache dictionary.
		Args:
			key = dict key
			item = dict data
		Return: void = if input error"""
		if key is None:
			return
		if item is None:
			return
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
