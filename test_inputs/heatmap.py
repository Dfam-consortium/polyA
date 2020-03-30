import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
import sys

## input is support matrix
#python heatmap.py support.tsv out.pdf
#PrintMatrixHashCollapse(cols, SupportHashCollapse) at the end of AdjudicateRegions will print support matrix

#red is larger nums, dark blue is smaller nums 

infile = sys.argv[1]
outfile = sys.argv[2]

matrix = []

subfams = []
positions = []

count = 0
with open(infile,'rb') as source:
    for line in source:
    	count+=1
    	
    	if count == 1:
    		positions = line.split('\t')
    		positions = positions[1:-2]
    	else:
    		fields = line.split('\t')
    		subfams.append(fields[0])
    		fields = fields[1:-2]
    		
    		for i in range(len(fields)):
    			fields[i] = float(fields[i])
    		matrix.append(fields)


for j in range(len(positions)):
	max = 0
	for i in range(len(subfams)):
		if(matrix[i][j] > max):
			max = matrix[i][j]
				
	for i in range(len(subfams)):
		matrix[i][j] = matrix [i][j] / max
			
matrix = np.array(matrix)
		
fig, ax = plt.subplots(figsize = (200, 50))

im = ax.imshow(matrix, interpolation='nearest', aspect='auto')

ax.set_yticks(np.arange(len(subfams)))
ax.set_yticklabels(subfams)

plt.savefig(outfile)

