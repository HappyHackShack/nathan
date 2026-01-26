#!/bin/env python3

import turtle

a_z = {
    'a': 'l90,f20,r90,f10,r90,f10,l90,f-10,f10,r90,f10,l90,c0,f10,c1',
    'b': 'l90,f20,r90,f10,r90,f10,l90,f-10,f10,r90,f10,l90,f-10,f10,c0,f10,c1',
    'c': 'c0,f10,l90,f20,l90,c1,f10,l90,f20,l90,f10,c0,f10,c1',
    'd': 'f5,l45,f7,l45,f10,l45,f7,l45,f5,l90,f20,l90,f6,c0,f14,c1',
    'e': 'l90,f20,r90,f10,f-10,r90,f10,l90,f10,f-10,r90,f10,l90,f10,c0,f10,c1',
    'f': 'l90,f20,r90,f10,f-10,r90,f10,l90,f10,f-10,r90,f10,l90,c0,f20,c1',
    'g': 'c0,f5,l90,f7,r90,c1,f5,r90,f7,r90,f10,r90,f20,r90,f10,r90,f4,c0,f9,c1,f7,l90,c0,f10,c1',
    'h': 'l90,f20,f-10,r90,f10,l90,f10,f-20,r90,c0,f10,c1',
    'i': 'f10,f-5,l90,f20,r90,f-5,f10,c0,r90,f20,l90,f10,c1',
    'j': 'r90,f-5,f5,l90,f5,l90,f20,r90,f-5,f10,c0,r90,f20,l90,f10,c1',
    'k': 'l90,f20,f-10,r45,f14,f-14,r90,f14,l45,c0,f10,c1',
    'l': 'l90,f20,f-20,r90,f10,c0,f10,c1',
    'm': 'l90,f20,r90,f5,r90,f20,f-20,l90,f5,r90,f20,l90,c0,f10,c1',
    'n': 'l90,f20,r90,f5,r45,f7,r45,f15,l90,c0,f10,c1',
    'o': 'f10,l90,f20,l90,f10,l90,f20,l90,f10,c0,f10,c1',
    'p': 'l90,f20,r90,f10,r90,f10,r90,f10,l135,c0,f14,l45,f10,c1',
    'q': 'f8,l90,f20,l90,f8,l90,f20,l135,c0,f7,r90,c1,f7,l45,f1,c0,f9,c1',
    'r': 'l90,f20,r90,f10,r90,f10,r90,f10,l135,f14,l45,c0,f10,c1',
    's': 'c0,f10,l90,f15,c1,f5,l90,f10,l90,f10,l90,f10,r90,f10,r90,f10,r90,f5,f-5,r90,f10,c0,f10,c1',
    't': 'c0,f5,l90,c1,f20,r90,f-5,f10,r90,c0,f20,l90,f10,c1',
    'u': 'l90,f20,f-20,r90,f10,l90,f20,f-20,r90,c0,f10,c1',
    'v': 'c0,l90,f20,c1,f-15,r135,f7,l90,f7,l45,f15,f-16,c0,f-4,r90,f10,c1',
    'w': 'l90,f20,f-20,r90,f5,l90,f10,f-10,r90,f5,l90,f20,f-20,r90,c0,f10,c1',
    'x': 'l63.4,f22.3,l116.6,c0,f10,c1,l116.6,f22.3,l63.4,c0,f10,c1',
    'y': 'l63.4,f11.15,l53.2,f11.15,f-11.15,r53.2,f11.15,r153.4,c0,f20,l90,f10,c1',
    'z': 'c0,l90,f20,r90,c1,f10,r116.6,f22.3,l116.6,f10,c0,f10,c1',
    ' ': 'c0,f10,c1',
    '1': 'c0,f10,l90,c1,f20,f-20,r90,c0,f10,c1',
    '2': 'c0,l90,f20,r90,c1,f10,r90,f10,r90,f10,l90,f10,l90,f10,c0,f10,c1',
    '3': 'c0,l90,f20,r90,c1,f10,r90,f10,r90,f10,f-10,l90,f10,l90,f-10,f10,c0,f10,c1',
    '4': 'c0,l90,f10,c1,f10,f-10,r90,f10,l90,f10,f-20,r90,c0,f10,c1',
    '5': 'f10,l90,f10,l90,f10,r90,f10,r90,f10,r90,c0,f10,c1,f10,l90,c0,f10,c1',
    '6': 'f10,l90,f10,l90,f10,r90,f-10,f20,r90,f10,r90,c0,f10,c1,f10,l90,c0,f10,c1',
    '7': 'c0,l90,f20,r90,c1,f10,r90,f20,l90,c0,f10,c1',
    '8': 'f10,l90,f10,l90,f10,r90,f10,r90,f10,r90,f10,r90,f10,l90,f10,l90,f10,c0,f10,c1',
    '9': 'f10,l90,f20,l90,f10,l90,f10,l90,f10,r90,f10,l90,c0,f10,c1',
    '0': 'f10,l90,f20,l90,f10,l90,f20,l90,f10,c0,f10,c1',
    '+': 'c0,f5,l90,c1,f10,l135,c0,f7,l135,c1,f10,r90,c0,f5,l90,f10,c1',
    '-': 'c0,l90,f5,r90,c1,f10,r90,c0,f5,l90,f10,c1',
    '*': 'l45,f14,l135,c0,f10,l135,c1,f14,l45,c0,f10,c1',
    '/': 'l63.4,f22.3,r153.4,c0,f20,l90,f10,c1',
    '=': 'c0,l90,f5,r90,c1,f10,f-10,l90,c0,f5,r90,c1,f10,r90,c0,f10,l90,f10,c1',
    '.': 'f2,c0,f18,c1',
    ',': 'l45,f7,r90,c0,f7,l45,f10,c1',
    "'": 'c0,f5,l90,f13,c1,f7,r90,c0,f5,r90,f20,l90,f10,c1',
    '[': 'c0,f5,l90,f20,l90,c1,f5,l90,f20,l90,f5,c0,f15,c1',
    ']': 'c0,f5,l90,f20,r90,c1,f5,r90,f20,l90,f-5,f5,c0,f10,c1',
    '^': 'c0,l90,f15,r45,c1,f7,r90,f7,r45,c0,f15,l90,f10,c1',
    '#': 'f10,l90,f20,l90,f10,l90,f20,l153.4,f22.3,l116.6,f10,l116.6,f22.3,l63.4,c0,f10,c1',
}

line = 0

def initialise():
    view = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    view.bgcolor("black")
    t.color("#ff60ff")
    C1=['black','#ff60ff']
    return view, t, C1

def exec_command(Cmd):
    verb = Cmd[0]
    value = float(Cmd[1:])
    if verb == "f":
        t.fd(value)
    elif verb == "r":
        t.rt(value)
    elif verb == "l":
        t.lt(value)
    elif verb == "c":
        t.color(C1[int(value)])
    else:
        t.fd(10)

def execute_command_string(cmd_string):
    for c in cmd_string.split(','):
        exec_command(c)

def Print(phrase):
    global line
    for letter in phrase:
        if letter in a_z:
            commands = a_z[letter]
            execute_command_string(commands)
            if letter == ' ':
                line += 10
            else:
                line += 20
        else:
            execute_command_string(a_z['#'])
            line +=20

def ask():
    global line
    say = input("say something: ")
    if 'exit' in say or 'stop' in say or 'quit' in say:
        return
    else:
        Print(say)
        execute_command_string('c0,r90,f30,l90')
        execute_command_string('f'+str(-line))
        execute_command_string('c1')
        line = 0
        ask()
    

print('running program...')
print('say exit, stop or quit to exit program')
view,t,C1 = initialise()
execute_command_string('c0,f-400,c1')
ask()