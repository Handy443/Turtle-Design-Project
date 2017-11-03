#Manuel Quinones
#Turtle Design Project
import turtle
bob = turtle.Turtle()
from myFunctionfile import*
from random import*
turtle.colormode(255)
bob.speed(11)
bob.width(15)
bob.hideturtle()
c1 = (0,0,0)
c2 = (134,134,134)

jump(bob,-60,-130)
bob.begin_fill()
quadround(bob,120,30,c2)
jump(bob,-120,-150)
quadround(bob,240,12,c2)
bob.end_fill()
jump(bob,-350,-85)
quadround(bob,700,400,c1)
jump(bob,-225,-320)
bob.begin_fill()
quadround(bob,450,150,c1)
bob.end_fill()

#Backdrop (On Monitor)

for times in range(15):
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    c = (r,g,b)
    bob.color(c)
    sides = randint(3,12)
    distance = randint(10,60)


    x = randint(-245,245)
    y = randint(150,300)
    jump(bob,x,y)
    polygon(bob,sides,distance,c)

#Python Logo

#Yellow Python(Bottom)

jump(bob,0,100)
bob.width(2)
bob.begin_fill()
bob.color(213,173,66)
for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(10)
bob.left(90)
bob.forward(30)
bob.right(90)
bob.forward(5)
bob.right(90)
bob.forward(60)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(40)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(10)
bob.left(90)
bob.forward(15)

for times in range(9):
    bob.forward(5)
    bob.right(10)

bob.forward(45)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(35)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(20)
bob.end_fill()
#Blue Python(Top)

jump(bob,25,194)
bob.begin_fill()
bob.color(68,103,133)
for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(35)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(35)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(10)
bob.left(90)
bob.forward(30)
bob.right(90)
bob.forward(5)
bob.right(90)
bob.forward(20)

bob.forward(40)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(40)

for times in range(9):
    bob.forward(5)
    bob.left(10)

bob.forward(24)
bob.left(90)

bob.forward(15)

for times in range(9):
    bob.forward(5)
    bob.right(10)

bob.forward(45)
bob.end_fill()

#Python Eyes (Yellow)

jump(bob,10,112.5)
bob.color(255,255,255)
bob.begin_fill()
bob.circle(5)
bob.end_fill()

#Python Eyes (Blue)

jump(bob,-10,265)
bob.color(255,255,255)
bob.begin_fill()
bob.circle(5)
bob.end_fill()
