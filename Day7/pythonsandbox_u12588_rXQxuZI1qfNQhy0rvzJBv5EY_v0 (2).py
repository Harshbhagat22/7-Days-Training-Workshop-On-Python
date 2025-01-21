import turtle

# Rainbow colors in order
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
sb = turtle.Turtle()


sb.speed(10) 


for i in range(360):
    sb.pencolor(rainbow_colors[i % 7])  
    sb.width(i / 100 + 1)              
    sb.forward(i)                      
    sb.left(60)                          

turtle.done() 
