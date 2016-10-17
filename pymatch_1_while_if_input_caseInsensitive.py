#! /usr/bin/python

while True:
  want = input("What do you want for Xmas: (small letters): ")

  if want in ('book', 'phone', 'notebook', 'chocolate'):
      print ("The ", want, " is yours")
      choice = input("do you want something else: 'Y' or 'N': ")
      # simple case insensitive selection without using re
      if choice.lower().upper() == 'Y': 
        continue; # if they select Y we return to the start of the loop.
      # simple case insensitive selection without using re
      if choice.lower().upper() == 'N':
        break;
  else:
      print ("I don't have ", want)
