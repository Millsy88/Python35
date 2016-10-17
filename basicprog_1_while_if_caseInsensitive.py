#! /usr/bin/python

import re

while True:
        want = input("What do you want for Xmas: (small letters): ")

        if want in ('book', 'phone', 'notebook', 'chocolate'):
                print ("The ", want, " is yours")
                break;
                
        else:
                print ("I don't have ", want)
                choice = input("do you want something else: 'Y' or 'N':")
# we don't need to specify an action for Y, as the loop will default to
# re-looping because we haven't told it to do anything else.
                no = "N"
                # more case insesnitive matching using re.match
                if re.match(choice, no, re.IGNORECASE):
                        break; # if the present matches, we exit the code
