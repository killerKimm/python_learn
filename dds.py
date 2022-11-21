import os
# CLEAR THE CONSOL
os.system("cls")

# DEFAULT FIELD


class Field:

    I = [["X", ".", "."],
         ["X", ".", "."],
         ["X", ".", "."]]

    status = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
   

    available_moves = {"q": [0, 0], "w": [0, 1], "e": [0, 2],
                       "a": [1, 0], "s": [1, 1], "d": [1, 2],
                       "z": [2, 0], "x": [2, 1], "c": [2, 2]}

    def __init__(self):
        self.fields = Field.I

    # THE DICT OF AVEILABLE MOVES (Q,W,E,
    #                             A,S,D,
    #                             Z,X,C)
    
    # DRAW THE FIELD

    @staticmethod
    def draw_field(i):
        for row in i:
            for x in row:
                print(f" {x}", end=" ")
            print()

    def update_field(self, val: str, player: str):
        fields = self.fields
        if val in self.available_moves:
            key = self.available_moves[val] # [0, 0]
            y = key[0] # 0

            x = key[1]

            assert(fields[y][x] == ".")

            fields[y][x] = player
            self.fields = fields
            self.draw_field(fields)

            #i[key[0][0]][key[1][0]] = "X"


class Player:
    def __init__(self, role: str, name: str):
        self.role = role
        self.name = name

    def new_move(self):
        return input(f"{self.name} ({self.role}) move: ")
        #field.update_field(val, self.role)

        # This is the player

# Game controller
class Game:
    def __init__(self, player1: Player, player2: Player):
        self.field = Field()
        self.player1 = player1
        self.player2 = player2

    def start(self):
        Field.draw_field(Field.I)
        while True:
          
          player1_move = self.get_move(self.player1)
          self.field.update_field(player1_move, self.player1.role)
          self.field.draw_field(self.field.fields)
          self.result_game()
            
          player2_move = self.get_move(self.player2)
          self.field.update_field(player2_move, self.player2.role)
          self.field.draw_field(self.field.fields)
          self.result_game()

    def result_game(self):
        field = self.field
        pass

    def get_move(self, player: Player):
        field = self.field
        move = player.new_move()

        if move in field.available_moves:
            key = field.available_moves[move]
            y = key[0]
            x = key[1]

            if field.fields[y][x] == ".":
                return move
            else:
                print("INVALID MOVE")
                return self.get_move(player)
        else:
            print("INVALID MOVE")
            return self.get_move(player)



player = Player("🫰", "Ramil")
player2 = Player("👌", "Huanio")

io = Game(player, player2)
io.start()

# field = Field()
# player = Player("X")
# player2 = Player("O")

# while True:
#     player.new_move(field)
    
#     player2.new_move(field)

#     # This is the game


