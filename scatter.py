"""
=================================
BST 273 Final Project, 100 points
=================================

NAME: Sanjana Sundaresan
EMAIL:

"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn

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
	"-o", "--output_file",
	help="path to the output data file (scatter plot)",
)
"""
Need to add in another argument for the path to the output file.
"""
args = parser.parse_args( )

fh = open(args.input_file)
df = pd.read_csv(args.input_file, delimiter = '\t')
headers = np.array(df.columns)  # get headers

a = args.xcol -1
b = args.ycol -1
cc = args.strat -1

row = []
x = []
y = []
z = []

df.groupby(headers[args.strat-1])
for line in fh:
    if "#" not in line: #removes the header row
        row = line.strip().split("\t") #first split into individual rows
        x.append(float(row[args.xcol -1]))
        y.append(float(row[args.ycol -1]))
        z.append(row[args.strat -1])


plt.scatter(x,y, label = z)
plt.xlabel(headers[a])
plt.ylabel(headers[b])
plt.show()
