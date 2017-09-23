
# that calculates and outputs the dot product of two integer matrices.
#  The two matrices should be stored in files in a format that you define. 
#  The program should take as input parameters the locations of the two files 
#  that represent the two matrices. Please document and provide examples of the 
#  matrix file format as well as the source code for the program.



# read a txt file as an input
import numpy as np
l = []
# Read the txt file
readfile = open("testcase.txt")
f = readfile.readlines()
for x in f:
	integer = x.split(",")
	for y in integer:
		y.split(" ")
		temp = []
		for z in y:
			# if avoid write empty and nextline to list
			if z != ' ' and z !='\n':
				temp.append(int(z))
		l.append(temp)

# Get two matrix if len / 2
a = l[:len(l)/2]
b = l[len(l)/2:]
aMatrix = np.matrix(a)
bMatrix = np.matrix(b)
print aMatrix * bMatrix
readfile.close()
