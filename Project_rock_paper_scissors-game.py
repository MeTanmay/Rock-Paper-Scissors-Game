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

#Write your code below this line 👇

choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))

print("Your choice /n")

if choice==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif choice==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else :
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

import random

comp_choice=random.randint(0,2)

print("Computer Choose :")

if comp_choice ==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')


elif comp_choice==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')


else :
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


#0=rock 1=paper 2=scisscors
if choice== comp_choice:
    print("Game Drawn")
if choice==0 and comp_choice==1:
    print("You lose. AI is taking over humans!!")
if choice==0 and comp_choice==2:
    print("YOu win. AI needs to work to attain human level!")
if choice==1 and comp_choice==0:
    print("You Win. AI needs to work to attain human level!")
if choice==1 and comp_choice==2:
    print("You lose. AI is taking over humans!!")
if choice==2 and comp_choice==0:
    print("You lose. AI is taking over humans!!")
if choice==2 and comp_choice ==1:
    print("You win.AI needs to work to attain human level!")






