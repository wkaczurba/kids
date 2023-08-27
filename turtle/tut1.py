import random
# Turtle - from https://pythonandturtle.com/turtle
t = turtle.Turtle('turtle')

t.width(5)
t.color('red')

l=t.left
r=t.right
f=t.forward
t.speed(10)

for i in range(0,500):
    (a,l,c) = (random.randint(15, 360), 
            random.randint(50, 150),
            random.choice(['red','green','blue','yellow','pink','black','cyan']))
    t.goto(0,0)
    t.color(c)
    t.left(a)
    t.forward(l)

t.penup()

t.goto(-80, 150)
t.color('green')

turtle.done()

