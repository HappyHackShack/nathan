#!/bin/env python3

import turtle
import random

view = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
view.bgcolor("black")
t.color("red","yellow")

result = [0]

for i in range(400):
    result.append(0)

for i in range(80000):
    x = 0
    for ii in range(400):
        x += random.randint(0,1)
    result[x] += .05

for i in range(2):
    t.fd(400)
    t.lt(90)
    t.fd(200)
    t.lt(90)
    
for i in range(201):
    t.fd(2)
    t.lt(90)
    t.fd(result[i+110])
    t.fd(-result[i+110])
    t.rt(90)

t.fd(-399)
t.color("blue","yellow")

for i in range(201):
    t.fd(2)
    t.lt(90)
    t.fd(result[i+90])
    t.fd(-result[i+90])
    t.rt(90)

view.exitonclick()