fh = open('temperature.txt')

f = [] # global variable for list f
day = 1 # global variable for our day counter used later

for i in fh:
        # was used to print temp in fahren seperatly from cel
	#print('Day ', day, 'Tempreture in Fahrenheit ', i.rstrip())
	#day +=1
	f.append(int(i)) # iterates through file, appends contents to list f
                         # as an int

fh.close()

c = [] # global variable for list c
for i in f:
        # converts and formats from fahren to cel with only 2 decimal places
       j = float ("{0:.2f}".format((i - 32) / 1.8))
       c.append(float(j)) # appends to list c as a float


#create our temp in cel file in write mode
fh1 = open('temperature_Celsius.txt', 'w') 
# print("\n") was used to seperate out temp in fahren and cel when printed seperatley

for i in c:
        # writes from list c to the file we created above
        # using string formatters (because why not)
        fh1.write('Tempreture in Celsius %s\n' % i)
        # was used to print temp in cel seperatly from fahren
        #print ('Day ', day, "Tempreture in Celsius ", i)
        #day +=1
fh1.close()

# Vanity. The below takes our first two arguments and iterates them through
# our second two, using the zip() func. The arguments are in order of assignment
# so our first, first argument will iterate through our first, second argument.
#Therefore we need to make sure they're alligned correctly for our print.
for (i, j) in zip(f, c):
        print ('Day ', day, "Tempreture in Fahrenheit ", i, "|", "Tempreture in Celsius ", j)
        day +=1 # uses our global variable day to count through and add
                # a day counter to our print statement.

highest = []    # gloabl list highest
lowest = []     # gloabl list highest


day = 1       # global variable day, reset so we can loop through below.

# the below loops through our c list, if i is equal to the max temp in c
# we append it to the max list. If equal to the min temp, we append it to
# the min list. These way we can multiple max / min values.
for i in c:
        if i == max(c):
               highest.append(int(day))
               day += 1 # iterates through so we can assign a day value
        elif i == min(c):
                lowest.append(int(day))
                day += 1 # needs to loop through no matter the value
        else:
                day +=1 # otherwise our day count will be off.

# finds average temp, makes it a float, formats it so it's only 2 decimal places
av = float("{0:.2f}".format(sum(c) / len(c)))

# generic print statements, with variable values.
print ('\nThe highest temperature was: ', max(c))
# below uses index range to print through the list highest without brackets
print('The days with the highest tempreture were: Days', str(highest)[1:-1])
print ('\nThe lowest temperature was: ', min(c) )
# as above, print from first value, to last, with no brackets (vainity)
print('The days with the lowest tempreture were: Days', str(lowest)[1:-1])
print ('\nThe average temperature was: ', av)



