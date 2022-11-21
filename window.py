import os


class Field:

    def __init__(self):
        self.cells = Field.get_default_field()

    def add_cord(self, cord, val: str):
        if self.cells.get(cord) is None or val not in ["X", "O"]:
            raise Exception("wtf?")
        self.cells[cord] = val

    def clear(self):
        self.cells = Field.get_default_field()

    @staticmethod
    def get_default_field():
        return {"q": " ", "w": " ", "e": " ",
                "a": " ", "s": " ", "d": " ",
                "z": " ", "x": " ", "c": " "}


class IO:
    def __init__(self, field: Field):
        self.field = field

    def new_move(self, player):
        val = input(f"PLAYER {player} MOVE: ")
        cells = self.field.cells
        if cells.get(val) is None:
            self.clear_scr
            print("wrong input value")

    @staticmethod
    def clear_scr():
        os.system("cls")


class Logic():
    pass


field = Field()
field.add_cord("x", "X")
field2 = Field()
field2.add_cord("s", "O")
print(field.cells)
print()
print(field2.cells)
