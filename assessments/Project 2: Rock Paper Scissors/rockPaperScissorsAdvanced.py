#Rock, Paper, Scissors (Advanced) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

import random


#Create variables to keep track of wins
playerWins = 0
computerWins = 0

#Introduce the game and ask player how many rounds needed to win
neededWins = int(input('Rock, Paper, Scissors...Enter the number of rounds needed to win the match: '))
print()

#While loop for Best of 3
while playerWins < neededWins and computerWins < neededWins:
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
if playerWins == neededWins:
    print('Player wins the match with',playerWins,'victories!')
else:
    print('Computer wins the match with',computerWins,'victories!')