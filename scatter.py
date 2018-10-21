"""
=================================
BST 273 Final Project, 100 points
=================================

NAME:
EMAIL:

"""

import argparse
import numpy
import matplotlib


parser = argparse.ArgumentParser( description=description )
parser.add_argument(
	"data_file",
	help="path to the input data file (TSV format)",
)
parser.add_argument(
	"--column",
	type=int,
	default=1,
	help="1-based index of the column to work on",
)
parser.add_argument(
	"--stats",
	choices=["mean", "median", "mode"],
	nargs="+",
	default=["mean"],
	help="choice(s) of statistics to compute [default: mean]",
)
args = parser.parse_args( )
