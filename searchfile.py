#! /Python35/python

import cgi, re
#import cgitb      #use for error traces
#cgitb.enable() 	  #use for error traces

def search_func (srchdoc, srchStr):
	for line in srchdoc:
		line = line.rstrip()
		if re.search(str(srchStr.lower()), line.lower()) != None:
			print ('<br>Line Found: ', line)

#Program logic starts here
print ('Content-type: text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Web Client Server File Search Example </title>')
print ('</head>')
print ('<body>')
print ("<H1>Search Text Example </H1>")


# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
searchString = form.getvalue('search')   # get search variable 
print("<br><H2 style='color:red;'> Search String: ", searchString)
fh = open("animals.txt")
fhdatalist = fh.readlines()

fh.close()
print('</body>')
print('/html>')
