#! /Python35/python

import cgi
import cgitb      #use for error traces
cgitb.enable()     #use for error traces

print ('Content-type:text/html \n')

text = """ <!DOCTYPE HTML>
<html>
	<head>
		
	<title>Quiz</title>			
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
	
	<div ALIGN="center" font: 30pt courier; font-variant: small-caps;">
	
	<Form action="search1.py" method="get">
            <H2>ICT2 Registration Query Interface</H2>
            <p>Enter word you want to check: <input type="text" name="word"></p>
            <input type=submit value="Search">
	</Form>

	</div>
	
	<div id="footer"> <!--Footer with copyright and a link to the T&C's-->
					&#169; DPRK Fan Page  <li><a href="/Users/Sonata34/Desktop/My files/UWE\Web systems/Part B/Pages/Terms & conditions.html">Terms & conditions</a></li>
				</div>
			</div>
		</body>
	</html>
"""

print(text)
