################################# Rock Paper Scissor Game #################################
##### Summary #####
"""This is a rock scissor paper Game in which a User can play against the computer.
input for user is taken and computer randomly generates a choice from rock, paper, and scissor.
code will run again and again until user wins.
case1:
#For Rock
rock vs Rock = Tie
rock vs Paper = Computer Wins
rock vs Scissor = User Wins

case2:
#For Paper
paper vs Rock = User Wins
paper vs Paper = Tie
paper vs Scissor = Computer Wins
 case3:
#For Scissor
scissor vs Rock = Computer Wins
scissor vs Paper = User Wins
scissor vs Scissor = Tie
"""
print("\n"  + "="*60) 
print("WELCOME TO ROCK PAPER SCISSOR GAME!".center(60))
print("="*60 + "\n")
import random
list1 = ["rock" , "paper", "scissor"]
user_win = False
while user_win == False:
  user_choice = input( "\033[1m" + "Choose Options : Rock, Paper, Scissor : " + "\033[0m").lower()
  print("\n" + "-"*60)   
  comp_choice = random.choice(list1)
  print("user choice is :",user_choice)
  print("computer choice is:",comp_choice ,"\n" + "-"*60)
  case1 = "rock"
  case2 = "paper"
  case3 = "scissor"
  if user_choice == case1 and comp_choice == case1:
       print("\033[1m" + "Both chosse same :: MatchTie".center(60) + "\033[0m"+"\n")
  elif user_choice == case1 and comp_choice == case2:
     print("\033[1m" + "Paper covers Rock, Computer Wins".center(60) + "\033[0m"+"\n")
  elif user_choice == case1 and comp_choice == case3:
      print("\033[1m" + "Rock crushes Scissor, User Wins".center(60) + "\033[0m"+"\n")
      user_win = True
  elif user_choice == case2 and comp_choice == case1:
      print("\033[1m" + "Paper covers Rock, User Wins".center(60) + "\033[0m"+"\n")
      user_win = True
  elif user_choice == case2 and comp_choice == case2:
      print("\033[1m" + "Both chosse same :: MatchTie".center(60) + "\033[0m"+"\n")
  elif user_choice == case2 and comp_choice == case3:
      print("\033[1m" + "Scissor cuts Paper, Computer Wins".center(60) + "\033[0m"+"\n")
  elif user_choice == case3 and comp_choice == case1:
      print("\033[1m" + "Rock crushes Scissor, Computer Wins".center(60) + "\033[0m"+"\n")
  elif user_choice == case3 and comp_choice == case2:
      print("\033[1m" + "Scissor cuts Paper, User Wins".center(60) + "\033[0m"+"\n")
      user_win = True
  elif user_choice == case3 and comp_choice == case3:
      print("\033[1m" + "Both chosse same :: MatchTie".center(60) + "\033[0m"+"\n   ")

print("\n"+"="*60)
print("Game Over, User Wins the Game!!!!!!!!!!!!")
print("="*60)