#!/usr/bin/env python
# coding=utf-8
from turtle import *
from datetime import datetime
#draw first circle

angleList=[i*6 for i in range(60)]
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

def drawDial():
    for index,angle in enumerate(angleList):
        penup()
        home()
        seth(angle)
        fd(200)
        pendown()
        if index % 5 == 0 :
            dot(10,"red")
        else:
            dot(5,"black")       

def moving(distance, angle = 0):
    penup()
    right(angle)
    forward(distance)
    left(angle)
    pendown()

def layout(length,vast):
    fd(length*1.15)
    rt(90)
    fd(vast/2.0)
    lt(120)
    fd(vast)
    lt(120)
    fd(vast)
    lt(120)
    fd(vast/2.0)

def timer_hands(name, length, vast):
    reset()
    moving(-length*0.15)
    begin_poly()
    layout(length,vast)
    end_poly()
    clock_labellings = get_poly()
    register_shape(name, clock_labellings)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        moving(radius)
        if i % 5 == 0:
            fd(25)
            moving(-radius-25)
        else:
            dot(3)
            moving(-radius)
        rt(6)


def setting():
    global second_hand, minute_hand, hour_hand
    timer_hands("second_hand", 125, 25)
    timer_hands("minute_hand", 130,25)
    timer_hands("hour_hand", 90, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray40", "black")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("red", "orange")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("red", "orange")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()

def tick():
    t = datetime.today()
    secondTimer= t.second + t.microsecond * 0.000001
    minute = t.minute + secondTimer / 60.0
    onTheHour = t.hour + minute / 60.0
    try:
        tracer(False)
        second_hand.setheading(6*secondTimer)
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*onTheHour)
        tracer(True)
        ontimer(tick,100)
    except Terminator:
        pass

def main():
    tracer(False)
    #drawDial()
    setting()
    tracer(True)
    tick()

if __name__ == "__main__":
    mode('logo')
    msg = main()
    print(msg)
    mainloop()
