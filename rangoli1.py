import colorsys
import turtle
t = turtle.Turtle()
s = turtle.Screen()
turtle.setup(width=600,height=700)
t.speed(0)
t.hideturtle
t.pendown()
color = ("violet","indigo","blue","green","yellow","orange","red")  
s.bgcolor('black')
for i in range (280):
    if 1<=i<=40:
        t.color(color[0])
    if 41<=i<=80:
        t.color(color[1])
    if 81<=i<=120:
        t.color(color[2])
    if 121<=i<=160:
        t.color(color[3])
    if 161<=i<=200:
        t.color(color[4])
    if 201<=i<=240:
        t.color(color[5])  
    if 241<=i<=280:
        t.color(color[6])                      
    t.circle(i*0.5)
    t.left(60)
t.penup()
t.goto(600,200)
t.pendown()
for j in range(100):
    t.color(color[1])
    t.circle(72)
    t.left(10)
t.penup()
t.goto(600,-200)
t.pendown()
for j in range(100):
    t.color(color[1])
    t.circle(72)
    t.left(10)
t.penup()
t.goto(-600,-200)
t.pendown()
for j in range(100):
    t.color(color[1])
    t.circle(72)
    t.left(10)
t.penup()
t.goto(-600,200)
t.pendown()
for j in range(100):
    t.color(color[1])
    t.circle(72)
    t.left(10)
t.penup()
t.goto(400,0)
t.pendown()
for j in range(100):
    t.color(color[1])
    t.circle(72)
    t.left(10)
t.penup()
t.goto(-400,0)
t.pendown()
for j in range(100):
    t.color(color[1])
    t.circle(72)
    t.left(10)    

turtle.done()