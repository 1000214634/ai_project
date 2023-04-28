import turtle
import random

# Set up the screen
WIDTH = 600
HEIGHT = 400
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)

# Set up the paddles
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
LEFT_PADDLE_X = -280
RIGHT_PADDLE_X = 260

left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=PADDLE_HEIGHT / 20, stretch_len=PADDLE_WIDTH / 20)
left_paddle.penup()
left_paddle.goto(LEFT_PADDLE_X, 0)

right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=PADDLE_HEIGHT / 20, stretch_len=PADDLE_WIDTH / 20)
right_paddle.penup()
right_paddle.goto(RIGHT_PADDLE_X, 0)

# Set up the ball
BALL_SIZE = 20
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(BALL_SIZE / 20)
ball.penup()
ball.goto(0, 0)

# Set up the ball speed and direction
BALL_SPEED = 5
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Set up the score display
FONT_SIZE = 20
FONT_STYLE = ("Arial", FONT_SIZE, "normal")
left_score = 0
right_score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, HEIGHT / 2 - FONT_SIZE - 10)
score_display.write("0 : 0", align="center", font=FONT_STYLE)


# Define the collision detection function
def collides_with_paddle(paddle, ball):
    if (
        ball.xcor() + BALL_SIZE / 2 >= paddle.xcor() - PADDLE_WIDTH / 2
        and ball.xcor() - BALL_SIZE / 2 <= paddle.xcor() + PADDLE_WIDTH / 2
        and ball.ycor() + BALL_SIZE / 2 >= paddle.ycor() - PADDLE_HEIGHT / 2
        and ball.ycor() - BALL_SIZE / 2 <= paddle.ycor() + PADDLE_HEIGHT / 2
    ):
        return True
    else:
        return False


# Define the computer player AI function
def computer_player(paddle, ball):
    if ball.ycor() > paddle.ycor():
        paddle.sety(paddle.ycor() + BALL_SPEED)
    elif ball.ycor() < paddle.ycor():
        paddle.sety(paddle.ycor() - BALL_SPEED)


# Set up the game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Check for collision with the top and bottom walls
    if (
        ball.ycor() + BALL_SIZE / 2 >= HEIGHT / 2
        or ball.ycor() - BALL_SIZE / 2 <= -HEIGHT / 2
    ):
        ball_dy *= -1

    # Check for collision with the left and right walls (score)
    if ball.xcor() + BALL_SIZE / 2 >= WIDTH / 2:
        left_score += 1
        score_display.clear()
        score_display.write(
            str(left_score) + " : " + str(right_score), align="center", font=FONT_STYLE
        )
        ball.goto(0, 0)
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED
    elif ball.xcor() - BALL_SIZE / 2 <= -WIDTH / 2:
        right_score += 1
        score_display.clear()
        score_display.write(
            str(left_score) + " : " + str(right_score), align="center", font=FONT_STYLE
        )
        ball.goto(0, 0)
        ball_dx = -BALL_SPEED
        ball_dy = -BALL_SPEED

    # Check for collision with the paddles
    if collides_with_paddle(left_paddle, ball):
        ball_dx *= -1
    if collides_with_paddle(right_paddle, ball):
        ball_dx *= -1

    # Move the computer players
    computer_player(left_paddle, ball)
    computer_player(right_paddle, ball)

    # Delay to control the frame rate of the game
    turtle.delay(10)
