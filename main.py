rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#to print images in the output 

def printImage(inp, choosenBy):
  print(choosenBy)
  if inp == 0:
    print(rock)
  elif inp == 2:
    print(scissors)
  elif inp == 1:
    print(paper)
  


user_choice=int(input("what do you choose, 0 for rock,1 for paper,2 for scissors\n"))
import random
import choose
computer_choice=random.randint(0,2)
if computer_choice==0:
  print("rock")
elif computer_choice==1:
  print("paper")
else:
  print("scissors")
printImage(user_choice, "User choice")
printImage(computer_choice, "Computer choice")

#here , only one case is like 2>0 is when you lose , otherwise always greater wins ex 1>0 : wins , 2>1 : wins

if user_choice<computer_choice:
  print("you loose!")
elif user_choice==computer_choice:
  print("it is a draw match!")
else:
  print("you win!")


