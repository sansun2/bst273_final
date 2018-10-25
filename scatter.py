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
	help="1-based index of the x-column",
)

parser.add_argument(
	"-y", "--ycol",
	type=int,
	default=1,
	help="1-based index of the y-column",
)

parser.add_argument(
	"-strat", "--strat",
	type=int,
	default=None,
	help="1-based index of the stratification column",
)
parser.add_argument(
	"-title", "--title",
	type=str,
	default=None,
	help="Title of the plot",
)
parser.add_argument(
	"-xlabel", "--xlabel",
	type=str,
	default=None,
	help="Label for the x-axis",
)
parser.add_argument(
	"-ylabel", "-ylabel",
	type=str,
	default=None,
	help="Label for the y-axis",
)
parser.add_argument(
	"-out", "--output_file",
	default = None,
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

#Iterate through the dataframe and store values for the 2 specific columns in individual lists.
for line in fh:
	if "#" not in line: #Ignore the header line
		row = line.strip().split("\t") #first split the file into individual rows
		x1.append(float(row[args.xcol -1])) #append x1 with values for the x-axis column
		y1.append(float(row[args.ycol -1])) #append y1 with values for the y-axis column
		if args.strat: #if a stratification column is mentioned
			z1.append(row[args.strat -1]) #append z1 with values for stratification

#Conditional for plotting the graph
if args.strat == None: #If the stratification column is not mentioned
	ax = sns.scatterplot(x = x1, y= y1)
else:
	ax = sns.scatterplot(x = x1, y= y1, hue = z1, palette="muted") #Color of the plot assigned 
	plt.legend(loc='upper left', prop={'size':6},bbox_to_anchor=(1,1))
	plt.tight_layout(pad=3)

#Default labels for the axes
if args.xlabel:
	plt.xlabel(args.xlabel)
else:
	plt.xlabel(headers[args.xcol - 1])

if args.ylabel:
	plt.ylabel(args.ylabel)
else:
	plt.ylabel(headers[args.ycol - 1])

#title
if args.title:
	plt.title(args.title)
else:
	plt.title("Plot")

if args.output_file:
	plt.savefig(args.output_file, bbox_inches="tight")
else:
	plt.savefig('default_scatter', format = "png", bbox_inches='tight')
plt.subplots_adjust(bottom=0.2)
plt.show()
