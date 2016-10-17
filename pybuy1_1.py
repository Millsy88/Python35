#! /usr/bin/python 


fh = open("shop.txt")
item = input("Check for what?: ")  # do not put quotes around user input
  
print("*******************")
print("**** Checking  ****")
print("** User defined ***")
print("***** item ********")
print("***** exists ******")
print("******** ? ********")

print ('user defined item is: ', item)
data = fh.read()
print ("All file data is:")
print (data)

# .lower() used to convert both item (user input) and data (item) to lowercase
# therefore they will match, regardless of how the user typed it in.
if item.lower() in data.lower(): 
    print ("Item exists in shop.txt")
else:
    print ("Item does not exists in shop.txt")


print ("\nConverting all a into b")
print (data.replace("a", "b"))

