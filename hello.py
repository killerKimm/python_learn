from turtle import *

speed(9999999)  # Painting speed control
bgcolor("#990000")
pensize(1)
penup()
goto(0, 50)
pendown()
circle(-120)
penup()
circle(-120, -60)
pendown()
pensize(5)
right(50)
circle(70, 55)
right(85)
circle(75, 58)
right(90)
circle(70, 55)
right(90)
circle(70, 58)

# body
penup()
pensize(10)
goto(80, 15)
pendown()
seth(92)
fd(135)
seth(125)
circle(30, 135)
seth(190)
fd(50)
seth(125)
circle(30, 135)
seth(275)
fd(90)
done()