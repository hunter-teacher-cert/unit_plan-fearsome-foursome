#Rock, Paper, Scissors (Basic) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

#This is Example Code for the Rock, Paper, Scissors project (Basic Version)

import random

#Ask player to choose Rock, Paper, or Scissors (default is Rock)   
rpsPlayer = int(input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))

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
    print('It is a draw.')
    
elif rpsPlayer == 1 and rpsComputer == 3:
    print('Player wins!')
    
elif rpsPlayer == 2 and rpsComputer == 1:
    print('Player wins!')
    
elif rpsPlayer == 3 and rpsComputer == 2:
    print('Player wins!')
    
else:
    print('Computer wins!')
    