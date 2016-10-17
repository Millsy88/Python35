#! /usr/bin/env python

# 90% of the below code is for display purposes when run via a web server

#try to run this program in web browser .... make sure apache service is running.
print ('Content-type:text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h1>Hello Word! This is my first CGI program</h1>')
print ('</body>')
print ('</html>')

# file handling

file = open("newfile.txt", "w")
file.write("hello world in the new file\n")
file.write("and another line\n")
file.close()

# opens, reads file we wrote to above, prints it to screen

file = open("newfile.txt", "r")
for line in file:
    print (line,)
file.close()

