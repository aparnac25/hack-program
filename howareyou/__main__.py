#!/usr/bin/env python

"""
Command line argparser for darwin day
"""

import argparse
from howareyou.howareyou import howareyou

def parse_command_line():
	"parses arguemnts for the howareyou function"

	# init parser and add arguements
	parser = argparse.ArgumentParser()

	# parser for good
	parser.add_argument(
		"--good",
		help="returns what ice cream you should eat if you have a good day",
		action="store_true"
		)

	parser.add_argument(
		"--bad",
		help="returns what ice cream you should eat if you have a bad day",
		action="store_true"
		)

	# returns user arguements
	args = parser.parse_args()
	return args


def run_program():
	"runs the comman line program"
	# get command lines arguements
	args = parse_command_line()

	# pass arguement to call howareyou function
	if args.good:
			howareyou("good")
	elif args.bad:
			howareyou("bad")

if __name__ == "__main__":
	howareyou("good")
	howareyou("bad")
