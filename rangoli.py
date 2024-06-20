from colorsys import hsv_to_rgb
import turtle
t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
colors = ("orange","dark green","red","purple","sky blue","pink")

for i in range (1,400):
    t.begin_fill()
    if 1<=i<=150:
        t.fillcolor(colors[3])

        t.pencolor(colors[0])
        t.forward(i)
        t.right(91)
    elif 151<=i<=300:
        t.fillcolor(colors[4])
        t.pencolor(colors[1])
        t.forward(i)
        t.right(73)
        
    else:
        t.fillcolor(colors[5])
        t.pencolor(colors[0]) 
        t.forward(i)
        t.right(61)
    t.end_fill()        

        


    

    
turtle.done()    


                   