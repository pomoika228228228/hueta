# import turtle
from turtle import *
from time import sleep

чрпх = Turtle()


for i in range(6):
    чрпх.forward(50)
    чрпх.left(60)
print(чрпх.pos())


чрпх.penup()
чрпх.goto(30,200)
чрпх.pendown()

for i in range(4):
    чрпх.forward(50)
    чрпх.left(90)
print(чрпх.pos())


чрпх.penup()
чрпх.goto(30,260)
чрпх.pendown()

for i in range(4):
    чрпх.forward(50)
    чрпх.left(90)
print(чрпх.pos())

чрпх.penup()
чрпх.goto(90,260)
чрпх.pendown()

for i in range(4):
    чрпх.forward(50)
    чрпх.left(90)
print(чрпх.pos())

чрпх.penup()
чрпх.goto(90,200)
чрпх.pendown()

for i in range(4):
    чрпх.forward(50)
    чрпх.left(90)
print(чрпх.pos())





exitonclick()