Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if selection == "0":
  print(Rock)
elif selection == "1":
  print(Paper)
else:
  print(Scissors)

computer_selection = [Rock, Paper, Scissors]

computer_selection_rndm = random.choice(computer_selection)

print(f"Computer chose:\n{computer_selection_rndm}")

if selection == "0":
  if computer_selection_rndm == Rock:
    print("You tie")
  elif computer_selection_rndm == Paper:
    print("You lose")
  else:
    print("You win")
elif selection == "1":
  if computer_selection_rndm == Rock:
    print("You win")
  elif computer_selection_rndm == Paper:
    print("You tie")
  else:
    print("You lose")
else:
  if computer_selection_rndm == Rock:
    print("You lose")
  elif computer_selection_rndm == Paper:
    print("You win")
  else:
    print("You tie")
