#! /usr/bin/python 

fh = open("shop.txt")
item = input("Check for what?: ")
  
print("*******************")
print("**** Checking  ****")
print("** User defined ***")
print("***** item ********")
print("***** exists ******")
print("******** ? ********")

print ('user defined word is: ', item)
data = fh.readlines() # used to read through the file

for line in data: # used to iterate through the data.
	if item.casefold() in line.rstrip(): #case insensitive search using
		print ("line found: ", line) #casefold.()
else:
	print('All file is parsed')		

fh.close() # always good practice to close a file when you're done
