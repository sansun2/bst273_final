"""
=================================
BST 273 Final Project, 100 points
=================================

NAME:
EMAIL:

"""

import argparse
import numpy as np
import matplotlib as plt


parser = argparse.ArgumentParser( description=description )
parser.add_argument(
	"input_file",
	help="path to the input data file (TSV format)",
)
parser.add_argument(
	"-x", "--xcol",
	type=int,
	default=1,
	help="1-based index of the x-column to work on",
)

parser.add_argument(
	"-y", "--ycol",
	type=int,
	default=1,
	help="1-based index of the y-column to work on",
)
parser.add_argument(
	"-z", "--zcol",
	type=int,
	default=1,
	help="1-based index of the z-column to work on",
)

parser.add_argument(
	"-z", "--zcol",
	type=int,
	default=1,
	help="1-based index of the z-column to work on",
)

parser.add_argument(
	"-o", "--output_file",
	help="path to the output data file (scatter plot)",
)
"""
Need to add in another argument for the path to the output file.
"""
args = parser.parse_args( )

fh = open(args.input_file)

data= data.split("\t")

x =
