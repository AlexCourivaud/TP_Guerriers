from avatarClass import Avatar 
import random

class Merchant(Avatar):
    def __init__(self, name, life=1000, power=1500, magic=9999, gold=100, potion=10) -> None:
        super().__init__(name=name, life=life, power=power, magic=magic, gold=gold, potion=potion)

    def salute(self):
        print("I'm the Merchant, I have some potions and if you're rich enough, some gears!")


    

#         if random.randint(1, 7) == 1:
#             price_potion = 4
#             print(f"{} dealt a critical hit!")
#             print(f"With his dexterity and his luck, the thief stole 1 gold from his oponent!")
#             self.gold += 1
#         else:
#             damage = self.power
#         return damage

# # def potion_price(self, rand):

