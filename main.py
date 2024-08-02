# Project 1
#  Rock, Paper, Scissor Game

import random

print('''
R for Rock (0)
P for Paper (-1)
S for Scissor (1)
      ''')

# Connecting input from the user to options
youDict = {"s":1,"S":1,"p":-1,"P":-1,"r":0,"R":0}
reverseDict = {1:"Scissor",-1:"Paper",0:"Rock"}

# Verify the information provided by the user
while True:
    youstr = input("Enter your choice (R, P, S): ")
    if youstr in youDict:
        you = youDict[youstr]
        break
    else:
        print("Invalid choice, please enter R, P, or S.")
        
# Computer choice 
computer = random.choice([-1,0,1])

# Present options of user and computer
print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

# Check Winner!
if(computer==you):
    print("Its Draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you==0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")