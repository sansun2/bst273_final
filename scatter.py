"""
=================================
BST 273 Final Project, 100 points
=================================

NAME: Sanjana Sundaresan
EMAIL: ssundaresan@hsph.harvard.edu

"""

import argparse
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser( description="" )
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
	"-strat", "--strat",
	type=int,
	default=None,
	help="1-based index of the z-column to work on",
)

parser.add_argument(
	"-out", "--output_file",
	help="path to the output data file (scatter plot)",
)

args = parser.parse_args( )

fh = open(args.input_file)
df = pd.read_csv(args.input_file, sep = '\t')
headers = np.array(df.columns)  # get headers

row = []
x1 = []
y1 = []
z1 = []

for line in fh:
	if "#" not in line:
		row = line.strip().split("\t") #first split into individual rows
		x1.append(float(row[args.xcol -1]))
		y1.append(float(row[args.ycol -1]))
		if args.strat:
			z1.append(row[args.strat -1])

if args.strat == None:
	ax = sns.scatterplot(x = x1, y= y1)
else:
	ax = sns.scatterplot(x = x1, y= y1, hue = z1)

plt.xlabel(headers[args.xcol - 1])
plt.ylabel(headers[args.ycol - 1])

if args.output_file:
	plt.savefig(args.output_file)
else:
	plt.savefig('default_scatter.png')

plt.show()
