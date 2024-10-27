from avatarClass import Avatar
from warrior_Class import Warrior
from thief_Class import Thief
from wizard_Class import Wizard
from shop_Class import Merchant
import pytest

### VAR ### 

marlouin = Thief(name="Marlouin el fifrelin")
gertrude = Thief(name="Gertrude the ninja")
marley = Warrior(name="Marley le guerrier")
roger = Warrior(name="Roger le boucher")
sharad = Wizard(name="Sharad The Wizard")
michel = Wizard(name="Michel the great magician")
fouille = Merchant(name="M. Fouille, Foire Fouille")

list_opponent = [marlouin,
                 gertrude,
                 marley,
                 roger,
                 sharad,
                 michel
]

list_opponent_name = [marlouin.name,
                 gertrude.name,
                 marley.name,
                 roger.name,
                 sharad.name,
                 michel.name
]

### Avatar Selection ###
def avatarSelection():
    print("Welcome to the battle of the warrior of the adventure of the magic ans the secret of the magic")
    print("You have to choose a class, there is only 3 available :")
    print("1 - Warrior - Strong for melee battle! ")
    print("2 - Thief - Can steal gold and make some critics on each attack!")
    print("3 - Magician - Strong magic user ! Can blast enemies!")

    user_class_choice = input("Select a class, '1' for Warrior, '2' for Thief, '3' for Wizard \n") 
    global avatarClass
    if user_class_choice == "1":
        avatarClass = Warrior
    elif user_class_choice == "2":
        avatarClass = Thief
    elif user_class_choice == "3":
        avatarClass = Wizard
    else:
        print("Wrong input - stay focus ! ")
        return avatarSelection()
    global player_name
    player_name = input("Please select a name for your Avatar \n")

### MAIN ###
avatarSelection()
player_Avatar = avatarClass(name=player_name)
print(player_Avatar.display_player_info())

while len(list_opponent) > 0 :

    print(f"you have {player_Avatar.gold} gold(s), would you like to go to shop ?")
    shop_selection = input("type 1 for the shop, 2 for fighting!")
    if shop_selection == "1":
        fouille.salute()
        player_Avatar.shopping()
    print("you can see the bright fighter waiting for a deadly battle!")
    print(list_opponent_name)


    opponent_selection = int(input(f"choose an opponent {len(list_opponent_name)} remaining(s)! type a number between 1 and {len(list_opponent_name)} \n"))
    opponent_selection -= 1
    if 0 <= opponent_selection <= len(list_opponent_name):
        enemy = list_opponent[(opponent_selection)]
    else:
        print("you type a wrong number.")

    print(f"The battle between {player_Avatar.name} and {enemy.name} is about to start")

    player_Avatar.salute()
    enemy.salute()
    print("FIGHT!")

    while player_Avatar.life > 0 and enemy.life > 0:
        print(f"Type 1 to attack or 2 to drink a potion (You have {player_Avatar.potion} potion(s) left)")
        user_choice = input("What do you want to do ? type 1 or 2 \n")
        if user_choice == "1":
            player_Avatar.attack(enemy)
            enemy.attack(player_Avatar)
            print()
            player_Avatar.life_bar.draw()
            print()
            enemy.life_bar.draw()
        elif user_choice == "2":
            player_Avatar.drink_potion()
        else:
            print("Wrong input")
        input("press enter to continue")
            
        if enemy.life == 0 and player_Avatar.life == 0:
            print(f"{player_Avatar.name} and {enemy.name} are both dead... you lose")
            print("TRY AGAIN!")
        if player_Avatar.life == 0 and enemy.life > 0:
            print(f"{player_Avatar.name} is dead, you lose...")
            print("TRY AGAIN!")
            
        if enemy.life == 0 and player_Avatar.life > 0:
            print(f"{enemy.name} is dead, you Won !")
            player_Avatar.gold += enemy.gold
            print(f"You get {enemy.gold} gold coins from you enemy, you now have {player_Avatar.gold} golds!")
            list_opponent.remove(list_opponent[opponent_selection])
            list_opponent_name.remove(list_opponent_name[opponent_selection])

print("you finished the game ! BRAVO")


