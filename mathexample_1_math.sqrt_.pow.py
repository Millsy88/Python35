import math #because we are using import math we need to prefix each math func with math.


n = input("enter a number ")
n = int(n)+1
for a in range(1,n):
	n_sqr = a * a
	n_sqrt = math.sqrt(a)
	print ("number is ", a, " square is ", n_sqr, " square root is ", n_sqrt)
	#n_pow = a ** a #This will work as a power function but will return the complete ints
	#print ("number is ", a, " cube is ", n_pow)
	#The below will return the power in scientific notion and print it in one line.
	print ("number is ", a, " cube is", math.pow(a, a)) 
print ("end of program")

# here we are using multi-line printing using triple """
str = """
n = input("enter a number ")

n = int(n)+1
for a in range(1,n):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)
print ("end of program")

n = input("enter a number")

n = int(n)+1
for a in range(1,n):
	n_sqr = a * a
	n_sqrt = int(sqrt(a))
	print ("number is " + a + " squrare is " + n_sqr + " n_sqrt is " + n_sqrt)
print ("end of program")
"""
