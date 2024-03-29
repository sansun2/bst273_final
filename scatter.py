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

description = """
A script to create a command line interface for plotting scatterplots in python.
"""

parser = argparse.ArgumentParser( description=description )
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
	default=2,
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
	help="Path to the output data file (scatter plot)",
)

args = parser.parse_args( )
fh = open(args.input_file)
h = fh.readline()
headers = h.strip().split("\t") #first split the file into individual rows
row = []
x1 = []
y1 = []
z1 = []

#Iterate through the dataframe and store values for the 2 specific columns in individual lists.
for line in fh:
	row = line.strip().split("\t") #first split the file into individual rows, separated by tabs.
	x1.append(float(row[args.xcol -1])) #append x1 with values for the x-axis column
	y1.append(float(row[args.ycol -1])) #append y1 with values for the y-axis column
	if args.strat: #If a stratification column is mentioned
		z1.append(row[args.strat -1]) #append z1 with values for stratification

#Conditional for plotting the graph
if args.strat == None: #If the stratification column is not mentioned
	sns.scatterplot(x = x1, y= y1)
else:
	sns.scatterplot(x = x1, y= y1, hue = z1, palette="muted") #Assigning the color of the plot with the categorical variable
	plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1)) #Placing the legend outside the plot
	plt.tight_layout(pad=3)

#X-axis label
if args.xlabel:
	plt.xlabel(args.xlabel)
else: #Default value for the x-axis label
	plt.xlabel(headers[args.xcol - 1])

#Y-axis label
if args.ylabel:
	plt.ylabel(args.ylabel)
else: #Default value for the y-axis label
	plt.ylabel(headers[args.ycol - 1])

#Title
if args.title:
	plt.title(args.title)
else: #Default plot title
	plt.title("Plot")

if args.output_file:
	plt.savefig(args.output_file, bbox_inches="tight")
else:
	plt.savefig('default_scatter', bbox_inches='tight')

plt.show()
