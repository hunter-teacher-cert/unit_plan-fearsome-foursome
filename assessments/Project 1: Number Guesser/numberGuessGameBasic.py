#Number Guesser (Basic Version) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

#This is Example Code for the Basic Version of Number Guesser Project

import random

#Variable to track number of guesses
counter = 0

#Computer picks Secret Number
num = random.randint(1, 10)

#Uncomment to show Secret Number while testing
print("Number = ",num)

#Variable for exit condition (True when player wins)
win = False

#While loop to continue game until player guesses the Secret Number
while win == False:
    
#Ask player to input a guess    
    guess = int(input('Enter Number: '))

#Update Guess Counter
    counter += 1
#Check whether player guessed the Secret Number
    if guess == num:
        win = True
    else:
        print('Try again!')
        continue

print('You win! The Secret Number is', num)
print('Number of guesses =', counter)