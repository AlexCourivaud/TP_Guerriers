class Weapon:
    def __init__(self, name, type, damage, value) -> None:
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value

sword = Weapon(name="Les Paix", type="coutal", damage=7, value= 10)
axe = Weapon(name="Hachoir", type="gros coutal", damage=8, value=12)