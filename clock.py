#!/usr/bin/env python
# coding=utf-8
import turtle
#draw first circle

turtle.title("clock")
def drawLine(pos,direction,dis):
    turtle.penup()
    turtle.goto(pos)
    turtle.seth(direction)
    turtle.pendown()
    turtle.fd(dis)

def drawCircle(pos,r):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.circle(r)

drawCircle((0,-200),200)
drawLine((-200,0),0,400)
drawLine((0,200),-90,400)
