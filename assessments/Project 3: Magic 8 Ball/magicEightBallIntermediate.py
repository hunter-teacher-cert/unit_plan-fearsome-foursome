#Magic Eight Ball (Intermediate) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

#This is Example Code for the Magic 8 Ball project (Intermediate Version)

import random

#Variables for responses
yes1="Yes!"
yes2="Definitely!"
no1="No!"
no2="Definitely not!"
maybe1="Maybe"
maybe2="Could be"

#List of responses
answers=[yes1, yes2, no1, no2, maybe1, maybe2]

#Variable for exit condition ("y" to play again)
playAgain = "y"

#While loop to continue as long as the player wants to ask another question
while playAgain == "y":
    
#Ask player to input a question   
  question = str(input('Enter your question for the Magic 8 Ball: '))
  
#Computer picks Magic 8 Ball response
#responseNum = random.randint(1, 6)
  responseNum=random.randint(0, 5)
  answer=answers[responseNum]

#Uncomment to show Response Number while testing/comment out for game play
  print("Response Number = ",responseNum)
#Output response
  print(answer)

#Ask player to play again   
  playAgain = str(input('Enter y to ask another question: '))