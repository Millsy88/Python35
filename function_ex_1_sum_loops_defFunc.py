def min_max(x):     #defining function
    size = len(x)
    print (size)    #prints lenght of the list
    print (x)       #prints received list
    min1 = x[0]     #minimum value assumed
    max1 = x[0]     #maximum value assumed

    for num in range(0,size):   #for all list elements
        if min1 > x[num]:       
            min1 = x[num]
        if max1 < x[num]:
            max1 = x[num]

    return (min1, max1)         #returning list
                                #function definition ends

# define another func, 
def sum_all(x):
    #min1 = x[0]     we can assign min and max using this index method
    #max1 = x[0]     which requires the for loop below
    #size = len(x)
    min1 = min(x)    # or we can just use these built in functions....
    max1 = max(x)
    
# need to use range(0, size) to provide a number of times to iterate through
# the list, so we start at 0 and go on until we reach our len, in this case size

#    for i in range(0, size): 
#        if min1 > x[i]:       if min1 is greater than x[i] then min1 = x[i]
#            min1 = x[i]       because it is smaller than the current min1
#        if max1 < x[i]:       Vice versa for max1. Complex, but workable
#            max1 = x[i]       if you can't use the built in functions.
    sum1 = min1 + max1  # provides our sum
    return (sum1)       # returns it, so when we call print, we print the sum
        
    
listnum = [12, 45, 22, 2, 0, 3, -5]    #main program - list
(minimum, maximum) = min_max(listnum)   #calling min_max function
print ("Smallest number is: " + str(minimum))   #printing outputs
print ("Largest number is: " + str(maximum))
print ("The sum of ", minimum, "&", maximum, "is", str(sum_all(listnum)))

