# This is the one that took me the longest I think. The issue was caused by the
# \n at the end of my write lines, which was required to make them readable
# and to let the function re-read them on the next iteration.
# However this would cause errors when it came to reading because a blank line
# has no int value for it read on the next iteration. This was solved with
# seek and truncate (eventually).

import random
import os # required for os.SEEK_END

fh = open('numbers.txt')

num_list = [] #create a global list var
for num in fh:
	#print('Number is ', num) #will print with newline   
	print('Number is ', num.rstrip())    
	num_list.append(int(num)) # append num as int to global list var

fh.close()


fh = open('numbers.txt', "r+") # open in read & write mode
size = len(num_list) # required to work out the number of iterations needed

# the below for loop replaces the numbers in file with new, random numbers

# this needed to be done seperately as I need the len of the num_list
# to work out how many times to loop through. From 0 to the number of
# items in the list, which is the same as the number of items
# in the file as thats were we got them from.
for i in (range(0, size)): 
        new_int = random.randint(1, 30) # range for randint
        new_int = str(new_int) # sets int to str so we can write it
        line = fh.write(new_int + '\n') # write our number with a \n
fh.close()

# VERY IMPORTANT b IS REQUIRED IN MODE FOR SEEK TO FUNCTION
with open('numbers.txt', 'rb+') as fh: 
    fh.seek(-1, os.SEEK_END) # we use the -1 to go to the last place in the file
    # we use truncate to remove any trailing garbage / whitespace, this removes
    # the \n which was previously causing issues. Because we didn't specify a size
    # it will default to the last postion / byte in the file which we specified
    # using seek.
    fh.truncate() 
    
print ('\nList is: ', num_list)
num_list.sort() # sorts list
print ('Sorted list is: ', num_list)

large_num = max(num_list)
small_num = min(num_list)
total_num = sum(num_list)
# formats average so it is a float with only 2 decimal places
av_num = float("{0:.2f}".format(total_num / len(num_list))) 

print ('Largest number from list: ', large_num)
print ('Smallest number from list: ', small_num)
print ('Sum of list: ', total_num)
print ('Average of list: ', av_num, "\n")


# reopen file and re-iterate through to compare the new numbers with the old
# this could have been done by appending the numbers to a new list as
# we wrote them to the file, but this way we can check the actual contents of
# the file itself, which was what was giving me the most trouble as I coded
# and we can use the previously created num_list as we have already printed
# out all the values from it.

num_list = []
fh = open('numbers.txt')
for num in fh:
	#print('Number is ', num) #will print with newline   
	print('New number is ', num.rstrip())    
	num_list.append(int(num))
fh.close()

print ('\nNew list is: ', num_list)
num_list.sort()
print ('Sorted new list is: ', num_list)

large_num = max(num_list)
small_num = min(num_list)
total_num = sum(num_list)
av_num = float("{0:.2f}".format(total_num / len(num_list)))

print ('Largest number from new list: ', large_num)
print ('Smallest number from new list: ', small_num)
print ('Sum of new list: ', total_num)
print ('Average of new list: ', av_num)




