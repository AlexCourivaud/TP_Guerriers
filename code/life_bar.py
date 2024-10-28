import os
os.system("")

class LifeBar: 
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m", "default": "\033[0m", "green": "\033[92m"}

    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.life_max
        self.current_value = entity.life
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.life

    def draw(self) -> None:
        remainings_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remainings_bars
        print(f"{self.entity.name}'s life : {self.entity.life}/{self.entity.life_max}")
        print(f"{self.barrier}" 
              f"{self.color if self.is_colored else ''}"
              f"{remainings_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}"
              )


    