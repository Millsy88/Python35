#! /usr/bin/python 

line = input ("Enter some text: ")
#len() method returns number of characters in line (user input
print ("You gave " , len(line) , " characters")   
line = line.lower().upper() # makes line case insensitive
					# more string methods: https://docs.python.org/3.4/library/stdtypes.html#string-methods
print ("In lowercase: ", line)
if len(line) <5 : # if line is less than 5, print:
     print ("Less than 5 characters")
elif len(line) >=5: # if line is equal to or greater than 5...
     if len(line) <10: # and less than 10, print:
          print ("Between 5 and 10 characters")
     else: # else (greater than 10) print:
          print ("More than 10 characters")
  
  

