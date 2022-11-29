# in file create the variables with coordinates witch contain winning positions, and function witch check this combination in field
I = ["q", "w", "e", "a", "q", "d", "z", "x", "q"]
# print(I[1:6:2])
ee = [["q", "w", "e"],
      ["a", "q", "d"],
      ["z", "x", "q"]]

r1 = I[0:3]
r2 = I[3:6]
r3 = I[6:9]

c1 = I[0:7:3]
c2 = I[1:8:3]
c3 = I[2:9:3]

d1 = I[0:9:4]
d2 = I[2:8:2]

if len(set(d1)) or len(set(d2)) or len(set(r1)) or len(set(r2)) or len(set(r3)) or len(set(c1)) or len(set(c2)) or len(set(c3)) == 1:
    print("huy")
else:
    print("NO")
