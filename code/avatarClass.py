from abc import ABC, abstractmethod
from life_bar import LifeBar

@abstractmethod
class Avatar(ABC):
    def __init__(self, name, life, power, magic, gold, potion) -> None:
        self.name = name
        self.life = life
        self.life_max = life
        self.power = power
        self.magic = magic
        self.gold = gold
        self.potion = potion
        self.life_bar = LifeBar(self, color="green")

        
    def attack(self, opponent) -> None:
        damage = self.job_attack()
        opponent.life -= damage
        opponent.life = max(opponent.life, 0)
        opponent.life_bar.update()
        print(f"{self.name} dealt {damage} damage to {opponent.name}")

    def job_attack(self):
        return self.power
    
    def drink_potion(self):
        if self.potion > 0:
            print(f"{self.name} drink a potion!")
            self.potion -= 1
            self.life += 30
            print(f"{self.name}'s get +30 live points to {self.life} lp!")
        else: 
            print("You do not have potion!")

    def display_player_info(self):
        print(f"Here the informations of your Avatar : {self.name} ! \n")
        print(f"{self.life} life points, {self.power} of power, {self.magic} magic points, {self.gold} gold coins")


    def shopping(self):
        # rand = random.randint(1,8)
        # potion_price(rand)
        while self.gold > 2:
            print(f"You have {self.gold} golds left")
            print("1 - potion / 3 golds")
            print("2 - Legendary trinket! / 25 golds")
            print("3 - To leave the shop.")
            user_input = input("enter your choice : \n")
            if user_input == "1":
                if self.gold > 2:
                    print("you bought a potion ! ")
                    self.potion += 1
                    self.gold -= 3
                else:
                    print("You don't have enough gold")
            elif user_input == "2":
                if self.gold >= 25:
                    print("you bought a the LEGENDARY TRINKET !!!! Have fun with it! ")
                    self.power += 40
                    self.gold -= 25
            elif user_input == "3":
                return
            else: 
                print("wrong input!!")
