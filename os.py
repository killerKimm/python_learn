fields = [[".", "1", "1"],
          ["1", ".", "1"],
          ["1", "1", "."]]
symbol = "."


def drow_check(self):
    i = []
    for row in fields:
        for dot in row:
            i.append(dot)

    if symbol in i:
        print("winner")
    else:
        print("losser")
