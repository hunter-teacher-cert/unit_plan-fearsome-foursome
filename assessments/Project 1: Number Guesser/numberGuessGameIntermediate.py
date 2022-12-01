#Number Guesser (Intermediate Version) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

#This is Example Code for the Intermediate Version of Number Guesser Project

import random

#Variable to track number of guesses
counter = 0

#Ask player to input range    
max = int(input('Enter the highest number to guess from 1 - '))

#Print out selected range
print('You selected 1 -', max)

#Computer picks Secret Number
num = random.randint(1, max)

#Uncomment to show Secret Number while testing/comment out to hide during game play
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

#Output results
print('You win! The Secret Number is', num)
print('Number of guesses =', counter)