import random
#n = 30 # can be used to set the upper limit on our range of our possible numbers
#instead we use randint to create a random function and set our parameters all
#in one line. We also add 1 to our generated number, cause why not.
to_be_guessed = int(random.randint(1, 30)) + 1
guess = 0

while guess != to_be_guessed:
    guess = int(input("New number: "))

    if guess > 0:       # program will exit if 0 or -1 is entered
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you couldn't find the number!") 
        break;
else:
    print("Congratulation. You found it!")
