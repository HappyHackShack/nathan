#!/bin/env python3
import turtle

t = []

for i in range(18):
    t.append(0)

for i in range(18):
    t[i] = turtle.Turtle()
    for ii in range(i):
        t[ii].right(20)

for i in range(18):
    t[i].speed(0)

def f(d):
    for i in range(18):
        t[i].fd(d)

def l(d):
    for i in range(18):
        t[i].lt(d)

def r(d):
    for i in range(18):
        t[i].rt(d)

f(50)
r(105)
for i in range(18):
    f(25)
    r(20)

turtle.Screen().exitonclick()