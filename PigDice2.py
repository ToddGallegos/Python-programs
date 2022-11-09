# Created On: 4/14/21
# Author: Todd G
# This program is a simulated dice game called PigDice, where players take turns rolling dice and adding to their score until someone reaches 100 points. Player 1 is the user and Player 2 is the CPU, who plays extremely cautiously.
# Updated 4/15/21 to give CPU better logic for winning. Now the CPU will hold if the dice roll is 6 or if the turn-total is greater than 10. This logic enabled the CPU to beat me.

import random

def PigDice():
  #initializing player score variables
  p1score = 0 
  p2score = 0

  #introduction
  print("Welcome to PigDice! Here are the rules:\n\nEach turn, a player repeatedly rolls a die until\neither a 1 is rolled or the player decides to hold.\nIf the player rolls a 1, they score nothing and it becomes\nthe next player's turn. If the player rolls any other\nnumber, it is added to their turn total and the player's turn continues.\nIf a player chooses to hold, their turn total is added to their score,\nand it becomes the next player's turn.\nThe first player to score 100 or more points wins.")
  input("\npress ENTER to begin")

  #overall game loop will continue while both players' scores are under 100
  while (p1score <=99) and (p2score <=99):
    #PLAYER ONE CODE
    p1dice = random.randint(1, 6) #initial dice roll, random number 1-6
    p1TurnTotal = 0 #initializing turn total
    print("\nYou've rolled a", p1dice,)

    
    if (p1dice !=1): #if the die roll is anything but a 1, add the dice roll to a turn total and ask whether to roll again
      p1TurnTotal = p1TurnTotal+p1dice
      p1choice = input("\nDo you want to hold or roll again?\n1 = hold\n2 = roll again\nEnter choice:")

      while (str(p1choice) == str(2)): #while they keep rolling, the turn total updates with each roll that isn't a 1
        p1dice2 = random.randint(1, 6) #new roll

        if (p1dice2 != 1):
          print("\nYou've rolled a", p1dice2,)
          p1TurnTotal=p1TurnTotal+p1dice2
          print("\nTurn Total:", p1TurnTotal)
          p1choice = input("\nDo you want to hold or roll again?\n1 = hold\n2 = roll again\nEnter choice:")
        else: #if the die comes up 1, the turn total becomes zero and the player choice switches to hold
          print("\nAWWW YOU ROLLED A 1 AND LOST YOUR", p1TurnTotal, "POINTS FROM THIS TURN.")
          p1TurnTotal=0
          p1choice = 1
      
      if (str(p1choice) ==str(1)): #if the player holds, then the turn total is added to the player's score 
        p1score = p1score+p1TurnTotal
        print("\nPLAYER 1 SCORE =", p1score)
        input("\npress ENTER to continue")
      elif (str(p1choice) != str(1)) and (str(p1choice) != str(2)):
        print("INVALID CHOICE. PENALTY TURN-SKIP.")
      
    elif (p1dice ==1): #if the original roll comes up 1 then it's a quick skip to player 2 with no updates to variables
        print("\nBummer. That's the end of your turn!")
        input("\npress ENTER to continue")

    #PLAYER TWO CODE
    #Similar to player 1 code except player 2 holds if dice is 6 or turn total is more than 10.
    p2dice = random.randint(1, 6) #initial dice roll, random number 1-6
    p2TurnTotal = 0 #initializing turn total
    print("\nPlayer 2 rolled a", p2dice)
    

    if (p2dice !=1): #if the die roll is anything but a 1, add the dice roll to a turn total and ask whether to roll again
      p2TurnTotal = p2TurnTotal+p2dice
      print("Turn Total:", p2TurnTotal)
      if (p2dice < 6): #if CPU rolls less than 6, it will roll again
        p2choice = 2
      else:
        p2choice = 1
        print("Player 2 holds")

      while (str(p2choice) == str(2)): #while they keep rolling, the turn total updates with each roll that isn't a 1
        p2dice2 = random.randint(1, 6) #new roll

        if (p2dice2 != 1):
          print("Player 2 rolled a", p2dice2,)
          p2TurnTotal=p2TurnTotal+p2dice2
          print("Turn Total:", p2TurnTotal)
          if (p2dice < 6) and (p2TurnTotal < 10): #CPU will only roll again if dice is less than 6 and turn total less than 10.
            p2choice = 2
          else:
            p2choice = 1
            print("Player 2 holds")
        else: #if the die comes up 1, the turn total becomes zero and the player choice switches to hold
          print("AWWW PLAYER 2 ROLLED A 1 AND LOST THEIR", p2TurnTotal, "POINTS FROM THIS TURN.")
          p2TurnTotal=0
          p2choice = 1
      
      if (str(p2choice) ==str(1)): #if the player holds, then the turn total is added to the player's score 
        p2score = p2score+p2TurnTotal
        print("PLAYER 2 SCORE =", p2score)
        input("\npress ENTER to continue")
      elif (str(p2choice) != str(1)) and (str(p2choice) != str(2)):
        print("INVALID CHOICE. PENALTY TURN-SKIP.")
      
    elif (p2dice ==1): #if the original roll comes up 1 then it's a quick skip to player 2 with no updates to variables
        print("\nBummer. That's the end of their turn!")
        input("\npress ENTER to continue")

  #Remaining game logic to figure out a winner and end the game
  if (p1score>99) and (p2score<100):
    print("\n**************")
    print("Player 1 Wins!")
    print("**************")
  elif (p2score>99) and (p1score<100):
    print("\n**************")
    print("Player 2 Wins!")
    print("**************")
  else:
    print("\nTIE! GAME OVER!")

PigDice()


