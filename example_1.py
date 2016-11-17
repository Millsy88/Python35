#! /Python35/python

import cgi, re
import cgitb      #use for error traces
cgitb.enable()     #use for error traces

print ('Content-type:text/html \n')

fh = open("content.txt")

filedata = fh.readlines()

fh.close()



#table=["<htm><body><table border=\"1\" width=\"100%\"><caption> Top 3 Olympic Medal Rankings </caption>"]		

#for i in range(0, len(country)):

	 #table.append("<tr><td align=\"center\">"+country[i]+"</td><td align=\"center\">"+gold[i]+"</td><td align=\"center\">"+silver[i]+"</td><td align=\"center\">"+bronze[i]+"</td></tr>")
	 
#table.append("</table></body></html>")   


text = """ <!DOCTYPE HTML>
<html>
	<head>
		
	<title>Index</title>			
	</head>
	<body>
		
	<h1 ALIGN="center" STYLE="background: #000000; font: 30pt courier"><font color="white">DPRK Fan Page </font></h1> <!--The name at the top of the page-->

	<div ALIGN="center"> <!-- Navigation bar-->
	
		<ul STYLE="background: #E74C3C; font: 110% courier; font-variant: small-caps;">
		  <li ALIGN="center" STYLE="display: inline"><a href="/Users/Sonata34/Desktop/My files/UWE\Web systems/Part B/Pages/home.html">Home</a></li><!--Linkes to the home page-->					  
		  <li ALIGN="center" STYLE="display: inline"><a href="/Users/Sonata34/Desktop/My files/UWE/Web systems/Part B/Pages/About me.html">About me</a></li><!--Linkes to the about me page-->
		  <li ALIGN="center" STYLE="display: inline"><a href="/Users/Sonata34/Desktop/My files/UWE\Web systems/Part B/Pages/Contact.html">Contact</a></li><!--Linkes to the contact page-->
		</ul> 
	</div>

	<div ALIGN="center" font: 30pt courier; font-variant: small-caps;"><!--Main area of the page-->
		<h2>Welcome</h2><!--Using the heading format to make the text stand out-->
		<p></p><!--Did have text here but decided it did not fit well-->
		<!--image links. Partial mapping must use / not \ -->
		<a href="News.html">
			<img src="Image Src/News.jpg" alt="News" title="All the latest from the DPRK" style="width:30%;height:30%; padding: 10px;">
		</a>
		<a href="example_2.py">
			<img src="Image Src/KJU_P.jpg" alt="Quiz" title="Do you know your dictators from your dog toupes?" style="width:30%;height:30%; padding: 10px;">
		</a>
		<br> <!-- can be used to break up images so they go inline etc -->
		<a href="Shop.html">
			<img src="Image Src/NK_FL_H.jpg" alt="Shop" title="Shop like your life depended on it!" style="width:30%;height:30%; padding: 10px;">
		</a>
"""

print(text)

print('<table border=1 width="75%"><caption> Top 3 Olympic Medal Rankings 2016 </caption>') 

for row in filedata:
    row = re.split(',', row.rstrip())  #split each item in the row by ',' - now row is a list
    print('<tr>')                      #create table row
    print('<td align="center">', row[0], '</td>')     #create table data - we know from file there are 4 cols 
    print('<td align="center">', row[1], '</td>')
    print('<td align="center">', row[2], '</td>')
    print('<td align="center">', row[3], '</td>')
    print('</tr>')

#print(table)
		
		

text = """		</div>
				
		<div id="footer"> <!--Footer with copyright and a link to the T&C's-->
					&#169; DPRK Fan Page  <li><a href="/Users/Sonata34/Desktop/My files/UWE\Web systems/Part B/Pages/Terms & conditions.html">Terms & conditions</a></li>
				</div>
			</div>
		</body>
	</html>
"""

print(text)
