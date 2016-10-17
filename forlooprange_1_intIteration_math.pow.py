import math

n = 100
sum = 0
for counter in range(1,n+1):
    sum = sum + counter
    sqr = counter * counter
    #power = counter ** counter
    #print ("The power of ", counter, "is ", power)
    # math.pow gives us the answer using scientific notion
    print ("The power of ", counter, "is", math.pow(counter, counter)) 
    print ("The square of ", counter, "is ", sqr)
print("Sum of 1 until %d: %d" % (n,sum))
print("Average is ", sum//n)
