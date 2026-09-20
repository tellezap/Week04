import math
import random
import turtle

# ---------- FUNCTIONS ----------

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)


def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)


def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


# ---------- SETUP ----------

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()
t.pencolor("white")  # so the lines show up on the dark blue background

# Create a window to draw in
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)

# Clear the screen
t.clear()

# ---------- DRAW CALLS ----------

# Part 1: basic shapes
draw_square(t, 100)
draw_circle(t, 50)
draw_polygon(t, 6, 50)  # Hexagon

# Close the turtle graphics window when clicked (keep this LAST)
turtle.exitonclick()