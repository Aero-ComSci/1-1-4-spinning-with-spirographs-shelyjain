import turtle
import random

screen = turtle.Screen()
screen.setup(800, 800)
p = turtle.Turtle()
p.speed(0)

length = 90
width = 90

for each in range(16):
    p.color("white")
    p.width(1)
    p.goto(-length / 2, length / 2)  

    p.color(random.choice(["red", "pink", "yellow", "blue", "sky blue", "cyan", "black", "gray"]))
    p.width(50)
    for _ in range(4):  # Draw one square
        p.forward(length)
        p.right(90)
        
    length += 50  # Increase the size for the next square

screen.mainloop()
