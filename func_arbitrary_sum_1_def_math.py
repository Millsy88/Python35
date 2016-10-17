def arithmetic_sum(first, *more):
    return (first + sum(more))

print (arithmetic_sum(1,2))
print (arithmetic_sum(1,2,3))
print (arithmetic_sum(1,2,3,4))
print (arithmetic_sum(1,2,3,4,5))
print (arithmetic_sum(1,2,3,4,5,6))

# below is a function created to convert celsius to fahrenheit using the specified formula
def f_to_c (c): # define the function, we state that the function expects an argument (c) to work
    f = (c * 9/5 + 32) # we define what we want it to do with our given argument (convert it) and assign it to f
    return (f) # we then ask it to return f, our newly converted number. Therefore when we call this
			   # func in conjunction with print it will print out f
    
print (f_to_c(1))
print (f_to_c(2))
print (f_to_c(3))
print (f_to_c(4))
print (f_to_c(5))
