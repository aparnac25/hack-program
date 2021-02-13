#!/usr/bin/env python

"""
A function to tell you what ice cream to eat 
"""

import random


def howareyou(arg):
	"""
	returns what ice cream you should eat

	Parameters 
	----------
	arg (str): 
		"good" or "bad"
	"""
	# Lists of ice cream flavors
	goodlist = ["fudge ice cream", "cookie dough ice cream", "mint chip ice cream"]
	badlist = ["rocky road ice cream", "strawberry ice cream", "vanilla ice cream"]

	# return what ice cream you should eat if you had a good day
	if arg == "good":
		print(f"You should eat {random.choice(badlist)}")

	# return what ice cream you should eat if you had a bad day
	elif arg == "bad":
		print(f"You should eat {random.choice(goodlist)}")
	

if __name__ == "__main__":
	howareyou("good")
	howareyou("bad")
