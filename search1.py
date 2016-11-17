#! /Python35/python

import cgi, cgitb, re, sys
cgitb.enable() 

#Program logic starts here
print ('Content-type:text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Quiz Example </title>')
print ('</head>')
print ('<body>')
print ("<H1>DPRK </H1>")


# use cgi.FieldStorage() to form parameter values 
form = cgi.FieldStorage() 
keys = list(form.keys())    # get all keys to check if anything is received from the form

if len(keys) > 0:           # To check if there is any form parameter received 
    word = form.getvalue('word')    # To get name value 

content = []	
	
file = open("animals.txt", "r")
for line in file:
	for words in line.replace(',',' ').split():
		content.append(words)

if file == None:              # If error in opening file then call failpage() and exit
    print("<H2 style='color:red;'> Unable to open file on server ... ")
    sys.exit()
	
file.close()



if word.upper() in (str.upper() for str in content):  
	template = """
				<title>Thank you!</title>
				<body style="background:#DDFFDD;">
				<h1>Thank you!</h1>
				<p> {i} is Correct! </p>
				</body>
				"""
else:
	template = """
				<title>Thank you!</title>
				<body style="background:#DDFFDD;">
				<h1>Sorry!</h1>
				<p> {i} is incorrect! </p>
				</body>
				"""
            


print(template)  
print (content) 
print("<br/><br/>") 
