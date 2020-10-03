# run in pythonIDE and see animations
import turtle

wn = turtle.Screen()

wn.bgcolor("black")

colors = ["red","purple","blue","green","violet","yellow",'grey','brown','pink']

draw = turtle.Turtle()

for x in range(360):
    draw.pencolor(colors[x%6])
    draw.width(x/100 + 1)
    draw.forward(x)
    draw.left(59)
turtle.done()
