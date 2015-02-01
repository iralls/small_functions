#!/usr/bin/env python

import random

def get_field_by_percentage(l):
	"""
	return entry from list containing 'keys' with associated percentage proportions
	@params:
		l - list of entries with a percentage (out of 100 please)
		ex: [['a', 30], ['b', 20], ['c', 40], ['d', 10]]
	'a' will be returned 30% of the time, 'b' 20%, 'c' 40%, 'd' 10%
	"""
	s = sum([i[1] for i in l])
	num = random.randrange(s)
	for i in l:
		num -= i[1]
		if num <= 0:
			return i[0]
