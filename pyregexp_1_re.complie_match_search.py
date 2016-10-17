import re
# we use re.complie to assign values to variables, but we can make them
# more complex / add flags etc, so p now becomes case insensitive red.
p = re.compile('red', re.IGNORECASE)  # or re.compile('UF*')

q = re.compile('\d{2}[\\-/]\d{2}[\\-/]\d{4}') # search for date format dd/mm/yyyy






#print(p.match("this is my string"))
#print(p.match("this"))
#print(p.match(" "))
#print(p.match("thisismystring"))
#print(p.match('123'))

fh = open("test2_animals.txt")

counter = 1

for line in fh:

    # only returns if the criteria is at the start of the line    
    print("line ", counter, "using match", q.match(line))
    # returns if the criteria is anywhere in the line
    print("line ", counter, "using search", q.search(line))
    counter += 1

fh.close()
