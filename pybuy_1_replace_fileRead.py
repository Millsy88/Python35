#! /usr/bin/python 

import re
# You must create an input file

fh = open("shop.txt")

for line in fh:
  #replace e with z
  line = line.rstrip('\n')
  line = line.replace('e','z') 
  print(line)
fh.close()

print("*******************")
print("*** Another Way ***")
print("*******************")
print("****** Using ******")
print("**** re Module ****")
print("*******************")

# converting chars using a loop to iterate through each line
fh = open("shop.txt")
for line in fh:
  line = re.sub('e','z',line)
  print(line.rstrip('\n'))  
fh.close()
  

print("*******************")
print("*** Another Way ***")
print("*******************")
print("****** Using ******")
print("**** read func ****")
print("*******************")

# using the .replace() function, replaces all instances of first argument with
# the second argument.
fh = open("shop.txt")
data = fh.read()	# no use of loop
data = data.replace('e','z')
print (data)

print ("\nConverting all a into b")
print (data.replace("a", "b")) 
fh.close()
