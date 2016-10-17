import random
import re

integerOne = 0
integerTwo = 0
integerThree = 0
temporaryInteger = 0
continueOrStop = "Continue"


while continueOrStop == "Continue":
    print("Please enter three positive integers, e.g. 456, 10 and 124. \n")
    integerOne = int(input())
    integerTwo = int(input())
    integerThree = int(input())

# Below is how we make sure our ints are in order

    if integerOne > integerTwo: # if 1 greater than 2
        temporaryInteger = integerOne # temp = 1 (largest number)
        integerOne = integerTwo # 1 becomes 2
        integerTwo = temporaryInteger # 2 becomes temp (largest number)

    if integerTwo > integerThree: #if 2 is greater than 3
        temporaryInteger = integerTwo # temp = 2 (largest number)
        integerTwo = integerThree # 2 becomes 3
        integerThree = temporaryInteger # 3 = temp (largest number)

    if integerTwo < integerOne: #if 2 is less than 1
        temporaryInteger = integerTwo # temp = 2 (largest number)
        integerTwo = integerOne # 2 becomes 1
        integerOne = temporaryInteger # 2 = temp (largest number)    
        

    print("The correct ordering of the entered pair of integers is : " , integerOne , " " , integerTwo , "", integerThree, "\n")
    print("\n")
    continueOrStop = "Not known"

    print("If you do not wish to enter another pair of positive integers, input 'Stop'." , 
          "If you do want to enter three more positive integers, input 'Continue'. \n")

    while ((continueOrStop is not "Continue") or (continueOrStop is "Stop")):
        reply = input()
        stop = "Stop" # assigns value to stop
        cntinue = "Continue" # assigns value to cntinue (can't use continue as it's a keyword)
# using re.match, we can check if our vars match the user input in a
#case insensitivie fashion / method.
        if re.match(reply, stop, re.IGNORECASE): 
            continueOrStop = "Stop"
            break;
        elif re.match(reply, cntinue, re.IGNORECASE):
            continueOrStop = "Continue"
        else:
            print("Please enter either 'Continue' or 'Stop'. Nothing else \n")
