class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return self._height

    def set_height(self, height):
        if (height < 0):
            print("Invalid Height")
        else:
            self._height = height

    def get_age(self):
        return self._age

    def set_age(self, age):
        if (age < 0):
            print("Invalid age")
        else:
            self._age = self.age

    def show(self) -> str:
        name = self.name.capitalize()
        return f"Created: {name}: {self.set_height}cm, {self.set_age} days old"
