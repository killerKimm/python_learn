import os
# CLEAR THE CONSOL
os.system("cls")

# DEFAULT FIELD


class Field:

    i = [["q", "w", "e"],
         ["a", "s", "d"],
         ["z", "x", "c"]]

    def __init__(self):
        self.fields = Field.draw_field(self.i)
    # THE DICT OF AVEILABLE MOVES (Q,W,E,
    #                             A,S,D,
    #                             Z,X,C)
    available_mowes = {"q": [[0], [0]], "w": [[0], [1]], "e": [[0], [2]],
                       "a": [[1], [0]], "s": [[1], [1]], "d": [[1], [2]],
                       "z": [[2], [0]], "x": [[2], [1]], "c": [[2], [2]]}
    # DRAW THE FIELD

    @staticmethod
    def draw_field(i):
        for row in i:
            for x in row:
                print(f" {x}", end=" ")
            print()

    def update_field(self, val):
        i = self.i
        if val in self.available_mowes:
            print()


class Player:
    def __init__(self, field: Field):
        self.field = field

    def new_mowe(self, player,):
        val = input(f"PLAYER {player} MOVE: ")
        field = self.field.fields
        moves = self.field.available_mowes

        # This is the player


field = Field()
field.update_field("w")
input()
dd
