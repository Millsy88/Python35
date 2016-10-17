import re

fh = open('test2_animals.txt')

search = input("What do you want to search for? ")

p = re.compile(search, re.IGNORECASE) # caseinsensitve useing re.

counter = 1 # used to provide our line numbers
found = 0 # used to avoid printing a load of 'not found' lines.

for line in fh:
        # returns if the criteria is anywhere in the line
        if p.search(line):
                print(search, "found on line ", counter)
                found += 1
                counter += 1 # increases line number with each iteration
        if not found:
                counter += 1 # because we don't add an iteration for found
                             # if it isn't in the doc we can go to the below if

if found == 0: # which will print the below.
        print (search, "not found")

fh.close()






