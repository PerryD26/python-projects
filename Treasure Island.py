print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

cross_roads = input("During your daily run, you decided to take a new path in the woods. While running down this new path, you encounter a crossroads. Which path do you take? Left or Right?\n")

if cross_roads == "Left":
  lake_crossing = input("After following this path for a mile, you come to a lake's shoreline. As you look across the lake, you see an island! There are two ways to get to the island. You can either swim to the island or take a boat. Which option do you select? Swim or Boat?\n")
  if lake_crossing == "Boat":
    proceed_wait = input("You have successfully made it safely across the lake and to the island! After making it to the island, you see a mysterious and abandoned house! You can either call and wait for your friends to arrive or do you enter the house by yourself? Which option do you select? Proceed or Wait?\n")
    if proceed_wait == "Wait":
      door = input("After waiting for 30 minutes, your two friends arrived. Then, you and your two friends entered the mysterious house and were attacked by a monster! However, as a group, you were able to defeat the monster! After defeating the monster your group proceed to the upstair level of the house. Once upstairs, you notice there are three different doors, each with a different color: Red, Yellow, and Blue. Which door do you open? Red, Yellow or Blue?\n")
      if door == "Red":
        print("You opened the Red door and encountered a trap!\nGame over!")
        exit()
      elif door == "Yellow":
        chest = input("You opened the Yellow door and found a large chest! In order to open the chest, you have to answer the following riddle!\nWhat force and strength cannot get through, I with my unique teeth can do. What am I? [hint: the answer is one word with three letters.]\n")
        if chest == "Key" or "key":
          print("You solved the riddle and opened the chest to find gold! You found the treasure! You win!!")
        else:
          print("You entered the wrong answer and the chest is now locked forever!!\nGame over!")
          exit()
      else:
        print("You opened the Blue door and encounter a trap!\nGame over!")
        exit()
    else:
      print("You enter the mysterious house by yourself and you were attacked by a monster!! Since you had no backup help, the monster defeated you!\nGame over!")
      exit()
  else:
    print("As you were swimming across the lake, you were attacked by an alligator!\nGame over!")
    exit()
else:
  print("After following this path for a mile, you get back to the city and do not get to the treasure island!\nGame over!")
  exit()
