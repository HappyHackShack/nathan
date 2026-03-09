#!/bin/env python
import tkinter as tk

W = 1024
H = 768
x_min, x_max = -2,1
y_min, y_max = -1.5,1.5
res = 50

# Create TK, and a canvas to hold the image
window = tk.Tk()
canvas = tk.Canvas(window, width=W, height=H, bg="black")
canvas.pack()

# Create an empty image object, and add it to the canvas
img = tk.PhotoImage(width=W, height=H)
canvas.create_image((0, 0), image=img, anchor=tk.NW)

# Draw a single white pixel at x=100, y=100
img.put("#ffffff", (10, 10))

# Draw a green line of pixels
for i in range(100):
    img.put("#00ff00", (140 + i, 150))

def picture():
    c = 0
    col = "ff0000"
    for py in range(H):
        for px in range(W):
            c = convert(px,py)
            col = mandelbrot(c)
            img.put(col,(px,py))
        if py%4 == 0:
            window.update()
    print(x_min, x_max-x_min, y_min, y_max-y_min)

def convert(px, py):
	x2 = px/W * (x_max-x_min) + x_min
	y2 = py/H * (y_max-y_min) + y_min
	return complex(x2, y2)

def mandelbrot(c):
    z = 0
    for i in range(res):
        z = z*z+c
        if abs(z) > 2:
            g = format(int(i*5.1), "#04x")[2:]
            return f"#{g}{g}{g}"
    return "#000000"

def julia(p):
    c = complex(0.7,0.5)
    z = p
    for i in range(res):
        z = z*z+c
        if abs(z) > 2:
            g = format(int(i*5.1), "#04x")[2:]
            return f"#{g}{g}{g}"
    return "#000000"

#def colour(c):


def zoomin(event):
    global x_min,x_max,y_min,y_max,res
    res += 1
    x_min += (x_max-x_min)/10
    x_max -= (x_max-x_min)/10
    y_min += (y_max-y_min)/10
    y_max -= (y_max-y_min)/10
    picture()

def zoomout(event):
    global x_min,x_max,y_min,y_max,res
    res -= 1
    x_min -= (x_max-x_min)/9
    x_max += (x_max-x_min)/9
    y_min -= (y_max-y_min)/9
    y_max += (y_max-y_min)/9
    picture()

def down(event):
    global x_min,x_max,y_min,y_max
    y_min += (y_max-y_min)/10
    y_max += (y_max-y_min)/10
    picture()

def up(event):
    global x_min,x_max,y_min,y_max
    y_min -= (y_max-y_min)/10
    y_max -= (y_max-y_min)/10
    picture()

def left(event):
    global x_min,x_max,y_min,y_max
    x_min -= (x_max-x_min)/10
    x_max -= (x_max-x_min)/10
    picture()

def right(event):
    global x_min,x_max,y_min,y_max
    x_min += (x_max-x_min)/10
    x_max += (x_max-x_min)/10
    picture()

def bind():
    window.bind( "w", up )
    window.bind( "s", down )
    window.bind( "d", right )
    window.bind( "a", left )
    window.bind( "e", zoomin )
    window.bind( "q", zoomout )

bind()
picture()

window.mainloop()