class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> str:
        name = self.name.capitalize()
        height = round(self.height, 2)
        return f"{name}: {height}cm, {self.age_days} days old"

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25.0, 30)
    init_height = rose.height
    print("=== Garden Plant Growth ===")
    print(rose.show())
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        print(rose.show())
    final_height = rose.height
    week_growth = final_height - init_height
    print(f"Growth this week: {round(week_growth, 2)}cm")


if __name__ == "__main__":
    ft_plant_growth()
