import turtle

colors = ["red", "purple", "blue", "green", "violet", "orange", "yellow"]
sb = turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    sb.pencolor(colors[i % 7])  
    sb.width(i / 100 + 1)       
    sb.forward(i)             
    sb.left(60)                 

turtle.done()
