#! /usr/bin/python 

# You must create an input file
inFile = "shop.txt"   #shop.txt is already in the folder
fh = open(inFile)  # opening a file in read mode

# loop over input file

for line in fh:
	#print ("** ", line.rstrip('\n'))
	if 'e' in tuple(line):
		print(line.rstrip('\n') + ' has "e" in it')
	else:
		print('There is no "e" in ', line.rstrip('\n'))
	
		


  



