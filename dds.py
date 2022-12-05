import os
# CLEAR THE CONSOL


# DEFAULT FIELD

class Field:

    available_moves = {"q": [0, 0], "w": [0, 1], "e": [0, 2],
                       "a": [1, 0], "s": [1, 1], "d": [1, 2],
                       "z": [2, 0], "x": [2, 1], "c": [2, 2]}

    def __init__(self):
        self.fields = Field.standard_field()

    # DRAW THE FIELD
    @staticmethod
    def standard_field():
        return [[".", ".", "."],
                [".", ".", "."],
                [".", ".", "."]]

    def clear_field(self):
        self.fields = Field.standard_field()

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


class Player:

    def __init__(self, role: str, name: str, wins: int = 0, losses: int = 0):
        self.role = role
        self.name = name
        self.wins = wins
        self.losses = losses

    def new_move(self):
        return input(f"{self.name} ({self.role}) move: ")

    def in_case_wins(self):
        self.wins += 1
        return self.wins

    def in_case_losses(self):
        self.losses += 1
        return self.losses


class Game:

    def __init__(self, player1: Player, player2: Player, *args):
        self.menu = Menu()
        self.field = Field()
        self.player1 = player1
        self.player2 = player2

    def __cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        Field.draw_field(self.field.fields)
        while True:
            print("press 0 to exit")
            player1_move = self.get_move(self.player1)
            self.field.update_field(player1_move, self.player1.role)
            self.__cls()
            self.field.draw_field(self.field.fields)
            result = self.result_game()
            if self.check_result(result):
                return

            print("press 0 to exit")
            player2_move = self.get_move(self.player2)
            self.field.update_field(player2_move, self.player2.role)
            self.__cls()
            self.field.draw_field(self.field.fields)
            result = self.result_game()
            if self.check_result(result):
                return

    def check_result(self, result):
        is_game_end = self.is_game_end()
        if result is False and not is_game_end:
            return
        self.field.clear_field()
        if is_game_end and not result:
            print("Draw!")
            return True

        winner = self.player1.role if result == "X" else self.player2.role

        print(f"Winner is {winner}")
        return True

    def is_game_end(self):
        fields = self.field.fields
        symbol = "."
        for row in fields:
            for el in row:
                if el == symbol:
                    return False
        return True

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
        if move == "0":  # exit from game loop
            exit()
        elif move in field.available_moves:
            key = field.available_moves[move]
            y = key[0]
            x = key[1]

            if field.fields[y][x] == ".":
                return move
            else:
                print("INVALID MOVE",
                      "\npress 0 to exit ")
                return self.get_move(player)
        else:
            print("INVALID MOVE",
                  "\npress 0 to exit ")
            return self.get_move(player)


class Menu:
    print("Hello, bitches")

    def __init__(self, *args, **kwargs):

        self.field = Field()

    def main_menu(self):

        a = input(f"1--PLAY GAME"
                  "\n2--SHOWE SCORE (not working)"
                  "\n3--exit:(\n")
        if a == "1":
            player1 = Player("X", input("\nenter name for X: "))
            player2 = Player("O", input("\nenter name for O: "))

            io = Game(player1, player2)

            io.start()
            self.main_menu()
        elif a == "2":
            pass

        elif a == "3":
            exit()


#player = Player("X", "Ramil")
#player2 = Player("O", "Huanio")
io = Menu()
io.main_menu()
#io = Game(player, player2)
# io.start()
