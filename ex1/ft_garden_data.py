
class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        name = self.name.capitalize()
        return f"{name}: {self.height}cm, {self.age} days old"


def ft_garden_data() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(f"{rose.show()}\n{sunflower.show()}\n{cactus.show()}")


if __name__ == "__main__":
    ft_garden_data()
