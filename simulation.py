#!/bin/env python3

from tkinter import Tk, Canvas
from math import sin, cos, radians, sqrt, atan2, pi

W = 1000
H = 750
c0 = "#ffff00"
c1 = "#00ffff"

selection = [-1,-1,-1]
objects = []
elasticity = 0.8
gravity = 1

class point:
    def __init__(self, x:float, y:float, vx:float, vy:float):
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy = vy
        self.angle = 90
        self.W = 10
        self.r = 50
        self.topV = 20

def draw():
    canvas.delete("all")
    for ob in objects:
        #print(type(ob).__name__)
        if type(ob).__name__ == "point":
            canvas.create_oval(ob.x-ob.r,H-ob.y+ob.r,ob.x+ob.r,H-ob.y-ob.r,fill=c1)
    canvas.update()

def select(event):
    global selection
    selection[0:2] = [event.x,H-event.y]

def move(event):
    global selection
    selection[0] = event.x
    selection[1] = H-event.y
    for ob in objects:
        #if sqrt((event.x-ob.x)**2+(event.y-ob.y)**2) <= ob.r:
        if sqrt((selection[0]-ob.x)**2+(selection[1]-ob.y)**2) <= ob.r:
            selection = [selection[0],selection[1],ob]
            ob.x = event.x
            ob.y = H-event.y
            draw()
            return

def deselect(event):
    global selection
    ob = selection[2]
    ob.Vx = 0
    ob.Vy = 0
    selection[2] = -1

def update():
    window.after(50,update)
    physics()
    draw()

def physics():
    global tick
    tick = (tick+1)%20
    for ob in objects:
        if ob is selection[2]:
            continue
        if ob.r-1<ob.y<ob.r+2 and -1<ob.Vy<0:
            ob.y = ob.r
            ob.Vy = 0
        else:
            ob.Vy -= gravity
        
        if ob.y + ob.Vy < ob.r:
            ob.y = ob.r-(ob.y+ob.Vy-ob.r)
            ob.Vy = -ob.Vy*elasticity
        else:
            ob.y += ob.Vy
        
        if ob.x + ob.Vx < ob.r:
            ob.x = ob.r
            ob.Vx = -ob.Vx
        elif ob.x + ob.Vx > W-ob.r:
            ob.x = (W-ob.r)
            ob.Vx = -ob.Vx
        else:
            ob.x += ob.Vx
        Vd = sqrt(ob.Vx**2+ob.Vy**2)
        if Vd >= ob.topV:
            ob.Vx = ob.Vx*ob.topV/Vd
            ob.Vy = ob.Vy*ob.topV/Vd

    for o1 in range(len(objects)):
        for o2 in range(len(objects)):
            if o1 != o2:
                ob1 = objects[o1]
                ob2 = objects[o2]
                d = sqrt((ob2.x-ob1.x)**2+(ob2.y-ob1.y)**2)-(ob1.r+ob2.r)
                if d <= 0:
                    a1 = atan2(ob2.y-ob1.y,ob2.x-ob1.x)
                    if a1<0:
                        a1 += 2*pi
                    a2 = atan2(ob1.y-ob2.y,ob1.x-ob2.x)
                    if a2<0:
                        a2 += 2*pi
                    ob1.Vx += d*cos(a1)
                    ob1.Vy += d*sin(a1)
                    ob2.Vx += d*cos(a2)
                    ob2.Vy += d*sin(a2)

def initialize():
    window = Tk()
    canvas = Canvas(window, width=W, height=H, bg=c0)
    canvas.pack()
    return canvas, window, 0

def quit(event):
    window.quit()

def bind():
    window.bind()

    window.bind("q", quit)

    canvas.bind("<Button-1>", select)
    canvas.bind("<B1-Motion>", move)
    canvas.bind("<ButtonRelease-1>", deselect)

canvas, window, tick = initialize()
bind()

for i in range(100,W,200):
    objects.append(point(i,300,10,0))
    #objects.append(point(300,400))
    draw()

# objects.append(point(100,50,10,0))
# objects.append(point(400,50,0,0))

update()

window.mainloop()
