import turtle
import math

qw=turtle.Turtle()
qw.speed(10000)


def turtpos(x,y):
  qw.penup()
  qw.setpos(x,y)
  qw.pendown()

def turtsquare(length):
	for i in range(4):
		qw.forward(length)
		qw.left(90)

def turtpattern1(length):
	turtpos(0,0)
	for i in range(19):
		turtsquare(length)
		qw.left(20)

def turtpattern2(radius):
	turtpos(0,0)
	for i in range(19):
		qw.circle(radius)
		qw.left(30)



qw.getscreen().bgcolor("grey")#background colour is set





qw.color("#a10000","#a10000")
turtpos(0,-300)                                   #outline
qw.begin_fill()
qw.circle(300)
qw.end_fill()

qw.color("#ffe87c","#ffe87c")#thesquarestuff
qw.begin_fill()
turtpattern1(200)
qw.end_fill()

qw.color("#ffff00","#ff6600")#the circle thing
qw.begin_fill()
turtpattern2(90)
qw.end_fill()

qw.color("#a52a2a","#966f33")#the weird star spam thing
turtpos(0,0)
qw.begin_fill()
for j in range(20):
	for i in range(10):
		qw.forward(150)
		qw.left(216)
	qw.left(20)
qw.end_fill()

turtpos(0,-90)#circle inside the star spam
qw.left(90)
qw.color("#665d1e","#a05544")
qw.begin_fill()
qw.circle(90)
qw.end_fill()

turtpos(0,0)#the innermost pattern
qw.color("#ff6700","#ff7f50")
qw.begin_fill()
for j in range(15):
	for i in range(6):
		qw.forward(30)
		qw.left(300)
	qw.left(50)
qw.end_fill()






turtle.done()