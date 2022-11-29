import os
# CLEAR THE CONSOL


# DEFAULT FIELD


class Field:

    I = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

    status = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    available_moves = {"q": [0, 0], "w": [0, 1], "e": [0, 2],
                       "a": [1, 0], "s": [1, 1], "d": [1, 2],
                       "z": [2, 0], "x": [2, 1], "c": [2, 2]}

    def __init__(self):
        self.fields = Field.I

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
            key = self.available_moves[val]  # [0, 0]
            y = key[0]  # 0

            x = key[1]

            assert(fields[y][x] == ".")

            fields[y][x] = player
            self.fields = fields

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

    def __cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        Field.draw_field(Field.I)
        while True:

            player1_move = self.get_move(self.player1)
            self.field.update_field(player1_move, self.player1.role)
            self.__cls()
            self.field.draw_field(self.field.fields)
            result = self.result_game()
            self.check_result(result)

            player2_move = self.get_move(self.player2)
            self.field.update_field(player2_move, self.player2.role)
            self.__cls()
            self.field.draw_field(self.field.fields)
            result = self.result_game()
            self.check_result(result)

    def check_result(self, result):
        if result is False:
            return

        winner = self.player1.role if result == "X" else self.player2.role

        print(f"Winner is {winner}")
        exit()

    def result_game(self):
        fields = self.field.fields
        if fields[0][0] == fields[1][1] == fields[2][2] == self.player1.role\
                or fields[0][0] == fields[1][1] == fields[2][2] == self.player2.role:
            return fields[0][0]
        elif fields[0][2] == fields[1][1] == fields[2][0] == self.player1.role\
                or fields[0][2] == fields[1][1] == fields[2][0] == self.player2.role:
            return fields[0][2]

        if fields[0][0] == fields[1][1] == fields[2][2] == self.player1.role\
                or fields[0][0] == fields[1][1] == fields[2][2] == self.player2.role:
            return fields[0][0]
        elif fields[0][2] == fields[1][1] == fields[2][0] == self.player1.role\
                or fields[0][2] == fields[1][1] == fields[2][0] == self.player2.role:
            return fields[0][2]

        if fields[0][0] == fields[1][1] == fields[2][2] == self.player1.role\
                or fields[0][0] == fields[1][1] == fields[2][2] == self.player2.role:
            return fields[0][0]
        elif fields[0][2] == fields[1][1] == fields[2][0] == self.player1.role\
                or fields[0][2] == fields[1][1] == fields[2][0] == self.player2.role:
            return fields[0][2]

        elif fields[0][0] == fields[0][1] == fields[0][2] == self.player1.role\
                or fields[0][0] == fields[0][1] == fields[0][2] == self.player2.role:
            return fields[0][0]

        elif fields[1][0] == fields[1][1] == fields[1][2] == self.player1.role\
                or fields[1][0] == fields[1][1] == fields[1][2] == self.player2.role:

            return fields[1][0]

        elif fields[2][0] == fields[2][1] == fields[2][2] == self.player1.role\
                or fields[2][0] == fields[2][1] == fields[2][2] == self.player2.role:

            return fields[2][0]

        elif fields[0][0] == fields[1][0] == fields[2][0] == self.player1.role\
                or fields[0][0] == fields[1][0] == fields[2][0] == self.player2.role:
            return fields[0][0]

        elif fields[0][1] == fields[1][1] == fields[2][1] == self.player1.role\
                or fields[0][1] == fields[1][1] == fields[2][1] == self.player2.role:

            return fields[0][1]

        elif fields[0][2] == fields[1][2] == fields[2][2] == self.player1.role\
                or fields[0][2] == fields[1][2] == fields[2][2] == self.player2.role:
            return fields[0][2]

        else:
            return False

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


player = Player("X", "Ramil")
player2 = Player("O", "Huanio")

io = Game(player, player2)
io.start()
