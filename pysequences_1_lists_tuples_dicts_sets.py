#! /usr/bin/python

import copy

mystring = "Python under Linux is great"
mylist = ['a', 'b', 3, 4]    # list
mytuple = ('a', 'b', 3, 4)    # tuple
mymarks = {"webProg":80, "OOSD":70, "POC":68, "NOS": 50}   # sequence / dictionary
marks = copy.copy(mymarks) # shallow copy of mymarks using copy import
modulecode = {"webProg":"UFC80", "OOSD":"UFC70", "POC":"UFC68", "NOS": "UFC50"}
staff = {"Zaheer":"3Q31", "Julia":"2P35", "Rong":"2P35", "Martin":"2P21"}
course = {"module": modulecode, "staff": staff} # dictionary of dictionaries
myset = set("this is a book")
myfrozenset = frozenset(("This", "can't", "be", "altered"))

#list operations - check lecture slides
print(mylist)
mylist.insert(2,'c') # adds c to index 2
mylist.append(5) # adds 5 to the end of the list
print(mylist)
mylist.reverse() # prints the list in reverse order
print (mylist)
missing = mylist.pop() #.pop() removes a random element.
if missing in mylist:
  print (missing, "is in ", mylist) # this shouldn't ever run
else:
  print (missing, "is not in", mylist) # this should always run

# so we can compare the original with our edited version
newlist = copy.copy(mylist) 
print (newlist)



#typle operations - check lecture slides
print(mytuple[0])
print(mytuple[1])
mytuple = list(mytuple)# converts the tuple to a list
mytuple.append(5)# now we can append, which we can't do to tuples
print (mytuple)

#string operations - check lecture slides
# prints every 4th element, starting with the element at index 3
#remembering that would be our first 4th element, 0, 1, 2, 3...
print (mystring[3::4]) 
print (len(mystring)) # prints the number of chars in / len of the string
mystring += "! " # adds "! " to the end of our string.
print (len(mystring)) # number of chars in / len of the string should be different
print (mystring * 3) # prints the string 3 times

#dictionary operations - check lecture slides
print(mymarks['webProg']) # prints the value assigned to this key
print(mymarks.keys()) # prints out the keys
print(mymarks.values()) # prints out the values
print(len(mymarks)) # prints out the number of pairs in mymarks
print(len(course)) # prints out the number of pairs in course
del mymarks["NOS"] # deletes the key pair value NOS
mymarks.pop("POC") # deletes the key pair value POC
mymarks.get("POC") # shouldn't return as we deleted this kay
print (mymarks) #prints pairs in mymarks
mymarks.popitem() # removes a random pair
print (mymarks) #prints remaining pair in mymarks

mymarks.update(marks) # adds key / value pairs to mymarks fro our copy
print (mymarks) #prints pairs in updated mymarks

# prints from the key Julia, in the staff dict, from the course dict
print (course["staff"]["Julia"])
# prints from the key webProg, in the module dict, from the course dict
print (course["module"]["webProg"])


mymarks["webProg"] = "100" # changes the value of webProg to 100

# loops through keys and prints key & value.
for key in mymarks.keys(): 
  print("Key: ", key, " Value: ", mymarks[key]) 

#set operations - check lecture slides
print(myset) # prints myset
myset.add("item") # adds item to set
print (myset) #re-prints myset
myset.pop() # removes a random item
print(myset) #re-prints myset

print(myfrozenset)
