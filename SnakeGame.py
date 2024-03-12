import random
import time
import turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SEGMENTS = []
SCORE = 0

def create_snake():
    for p in SNAKE_POSITION:
        snake = turtle.Turtle()
        snake.penup()
        if p == (0, 0):
            snake.shape("arrow")
        else:
            snake.shape("square")
        snake.color("black")
        snake.goto(p)
        SEGMENTS.append(snake)

def snake_growth(new_x, new_y):
    snake = turtle.Turtle()
    snake.penup()
    snake.shape("square")
    snake.color("black")
    snake.goto(new_x - 20, new_y)
    SEGMENTS.append(snake)

def create_food():
    food = turtle.Turtle()
    food.penup()
    food.speed(10)
    food.shape("circle")
    food.color("red")
    food.goto(random.randint(-280, 280), random.randint(-280, 280))
    return food

def limit():
    if SEGMENTS[0].xcor() < -280:
        SEGMENTS[0].goto(280, SEGMENTS[0].ycor())
    elif SEGMENTS[0].xcor() > 280:
        SEGMENTS[0].goto(-280, SEGMENTS[0].ycor())
    elif SEGMENTS[0].ycor() < -280:
        SEGMENTS[0].goto(SEGMENTS[0].xcor(), 280)
    elif SEGMENTS[0].ycor() > 280:
        SEGMENTS[0].goto(SEGMENTS[0].xcor(), -280)

def score_board():
    turtle.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 260)
    turtle.write(f"Score = {SCORE}", align="center", font=("Arial", 20, "bold"))

def food_collision():
    if SEGMENTS[0].distance(food) < 20:
        food.clear()
        return True

def self_collision():
    for s in range(2, len(SEGMENTS)):
        if SEGMENTS[0].distance(SEGMENTS[s]) < 20:  
            return False
    return True

def up():
    if SEGMENTS[0].heading() != 270:
        SEGMENTS[0].setheading(90)

def down():
    if SEGMENTS[0].heading() != 90:
        SEGMENTS[0].setheading(270)

def left():
    if SEGMENTS[0].heading() != 0:
        SEGMENTS[0].setheading(180)

def right():
    if SEGMENTS[0].heading() != 180:
        SEGMENTS[0].setheading(0)

window = turtle.Screen()
window.setup(width = 600, height = 600)
window.bgcolor("yellow")
window.title("Snake game")
window.tracer(0)

create_snake()

food = create_food()

window.listen()
window.onkey(up, "Up")
window.onkey(down, "Down")
window.onkey(left, "Left")
window.onkey(right, "Right")

game = True
while game:
    window.update() 
    time.sleep(0.1)
    score_board()

    for s in range(len(SEGMENTS) - 1, 0, -1):
        new_x = SEGMENTS[s - 1].xcor()
        new_y = SEGMENTS[s - 1].ycor()
        limit()
        SEGMENTS[s].goto(new_x, new_y)

        if food_collision():
            SCORE += 1
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            snake_growth(new_x, new_y)
    
    SEGMENTS[0].forward(20)  
    
    game = self_collision()

window.exitonclick()
