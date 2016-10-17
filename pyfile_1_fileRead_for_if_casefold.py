#! /usr/bin/python 

# You must create an input file
inFile = "shop.txt"   #shop.txt is already in the folder
fh = open(inFile)  # opening a file in read mode

search = input("What letter to search for? ")

# loop over input file
for line in fh:
# checks for specified letter set by the user using search (set above).
        if search.casefold() in line:
#        if "d" in line: - searches only for specified letter.
                print ("** ", line.rstrip('\n'))
	
  



