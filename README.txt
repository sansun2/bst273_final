1.	List your name and email address.

NAME: Sanjana Sundaresan
EMAIL: ssundaresan@hsph.harvard.edu

2.	Summarize your experience working on the final project. For example, you might approximate how many hours you spent on it and how those hours were distributed. If you found some aspects considerably harder than others, list those here. If there are known problems with your final project script, list those here.

ANSWER:

3.	In a few sentences, describe what your final project script does.

ANSWER: The script allows the user to specify 2 columns from a tsv file to plot as a scatter plot. The default option will plot the first 2 columns, and save the file as "default_scatter.png". The axes are labeled with the respective column headings. There are several flags that can be used to customize the plot.

The flags are:
-x: specifies the x values to be plotted
-y: specified the y values to be plotted
-strat : a column by which the plot can be stratified, identified by different colors. If not specified, the plot will contain a single series.
-title: a title for the plot. Default- no title.
-xlabel: customized label for the x-axis. Default- header of the x-axis column.
-ylabel: customized label for the y-axis. Default- header of the y-axis column.
-out: path to the output file. Default: file gets saved as default_scatter.png in the current working directory.

4.	List any modules (outside of the Python standard library) that are required to execute your final project script. You may answer “N/A” if no such modules are required.

ANSWER: The additional modules required are argparse, matplotlib, and seaborn.

5.	Describe your sample INPUT FILE(S). If you are completing a custom final project that does not require an input file, explain that clearly here.

ANSWER: The input file has tab separated columns. The first line contains column headers. The file has the extension ".tsv".

6.	Provide the command used to produce your sample OUTPUT FILE with flags and arguments specified (e.g. “$ python script_name.py arguments”).

ANSWER: Here is an example command to create a stratified plot using the iris.tsv. The OUTPUT file flag is "-out" and the file will be saved as scatter_iris.png in the current working directory. If this is not specified, the file will be saved as default_scatter.

$python scatter.py iris.tsv -x 1 -y 2 -strat 5 -out scatter_iris.png

7.	Describe your sample OUTPUT FILE(S). If you are completing a custom final project that does not produce an output file, capture the STDOUT of the command specified above and include it here (e.g. “$ command > sample_stdout.txt”).

ANSWER: The output file is a scatter plot.

8.	What was your favorite part of learning to program in BST 273 (i.e. something we should definitely NOT change in future incarnations of the course)?

ANSWER: This is one of the best courses I have taken at HSPH. Eric and Kevin, thank you both very much creating a highly comprehensive course. My favorite parts were the live coding sessions during class.

9.	What was your LEAST favorite part of learning to program in BST 273 (i.e. something we should look into changing for future incarnations of the course)?

ANSWER: I didn't have any!
