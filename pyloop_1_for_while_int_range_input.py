#! /usr/bin/python

for i in (0,3+1): # no in range, so we print to 0 and 4 before two Hello line
  print (i, "Hello\n")
 
for i in range(0,10): # using in range we print Bye 0 through to 10.
  print (i, "Bye\n")

total = 100
while total > 0: 
    # get number from user
    print(total, " left")
    innum = int(input("Enter number : "))   
    total = total - innum
else:
  # if we type a negative number we will increase our total 
  # as we are using - and 100 - -10 becomes 100 + 10.
    print ("total value became <= 0 i.e. ", total)

print ("Goodbye!")


