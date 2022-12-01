#Rock, Paper, Scissors (Intermediate) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

#This is Example Code for the Rock, Paper, Scissors project (Intermediate Version)

import random

#Best of 3 to win, create variables to keep track of wins
playerWins = 0
computerWins = 0

#Introduce the game
print('Rock, Paper, Scissors...Best of 3 to win!')
print()

#While loop for Best of 3
while playerWins < 2 and computerWins < 2:
    #Ask player to choose Rock, Paper, or Scissors (default is Rock)   
    rpsPlayer = int(input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))

    #Print blank line for formatting
    print()
    
    #Print out player choice
    if rpsPlayer == 2:
        print('Player selected Paper')
    
    elif rpsPlayer == 3:
        print('Player selected Scissors')
    
    else:
        rpsPlayer = 1
        print('Player selected Rock')

    #Computer picks Rock, Paper, or Scissors
    rpsComputer = random.randint(1, 3)

    #Output computer's choice
    if rpsComputer == 1:
        print('The computer selected Rock')
    elif rpsComputer == 2:
        print('The computer selected Paper')
    else:
        print('The computer selected Scissors')

    #Check for winner and output results
    if rpsPlayer == rpsComputer:
        print('It is a draw')
        print()
    
    elif rpsPlayer == 1 and rpsComputer == 3:
        print('Player wins this round!')
        print()
        playerWins += 1
    
    elif rpsPlayer == 2 and rpsComputer == 1:
        print('Player wins this round!')
        print()
        playerWins += 1
    
    elif rpsPlayer == 3 and rpsComputer == 2:
        print('Player wins this round!')
        print()
        playerWins += 1
    
    else:
        print('Computer wins this round!')
        print()
        computerWins += 1
        
    continue

#Determine overall winner and output result
if playerWins == 2:
    print('Player wins the match!')
else:
    print('Computer wins the match!')