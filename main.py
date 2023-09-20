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
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("Walking in a forest, you find an old abandoned castle.")
print('''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::o:::::::::::::::::::::
:::::::::::::::::::::::::::::::::+--:::::::::::::::::::
::::::::::::::::::::::::::::::::+--__<::::::::::::::::
::::::::::::::::::::::::::_:_:_:_|_::::::::::::::::::::
::::::::::::::::::::::::::]-I-I-I-[::::::::::::::::::::
::::::`      `::::::::::::\_,_,_,_/::::::::::::::::::::
::::/          \:::::::::::|     |:::::::::::::::::::::
:::::          ::::::::::::|  _  |:-_-_-_-:::::|II>::::
::::\          /:::-_-_-_-:| / \ |:\-.-.-/:::::I:::::::
::::::._    _.:::::\_,,_,/:| |_| |::|   |:::::/ \::::::
::::::::::::::::::::|   ]::|     |/\|   |::::/___\:::::
::::::::::::::::::::[ []|::|     ,... /\|:::::| |::::::
:::::::::::|II>:::::|   |__|    u|::| |||::::_| |::::::
:::::::::::I::::::::|[] ,--.  u  |::|   |::_- ,.:::::::
::::::::::/ \:::::::[   |::|u    |::|   |_-   |::::::::
:::::::::/___\::::|      |:|    _||||_   \    |::::::::
::::::::::| |:^:^:|      |/     - '' -          _\:::::
:::::::::::.,   ___          ,----' \       _/]/:::::::
::::::::::::|  /:::\        /``-.   \    __,:::::::::::
::::::::::`--. |::::) ___  _.---'|  (   /::::::::::::::
''')
print("You decide to walk inside. As you walk through the entrance, you have the option to go right, up a flight of stairs, or left, down a hallway.")
left_right = input("Which way do you go? Type left or right. \n").lower()

if left_right == "left":
  flee_fight = input("The hallway leads you to a room. After walking inside, you hear the click of the door as it closes. A large group of goons enter from the other side. Do you flee the attack or stay and fight? Type flee or fight. \n").lower()
  if flee_fight == "flee":
    door = input("You know when you are outmatched and leave as quickly as possible, losing those who would harm you in the maze of the castle. Running through the halls, you come to a dead end with three doors. Which one do you choose? Type red, green, or yellow. \n").lower()
    if door == "yellow":
      print("You find a treasure chest! Congratulations.")
    elif door == "green":
      print("A beast emerges and eats you. You die. Please try again.")
    elif door == "red":
      print("A fire emerges and consumes you. You die. Please try again.")
  else:
    print("The battle is too much for you. The opposition quickly overpowers you and you die. Please try again.")
else:
  print("You fall into a booby trap and die. Please try again.")