import turtle, paddle, ball, threading, time, scoreboard

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(width=800, height=600)

screen.tracer(0)

scoreboard = scoreboard.Scoreboard()

right_paddle = paddle.Paddle(350, 0)
left_paddle = paddle.Paddle(-350, 0)

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

ball = ball.Ball()

finished = False

while not finished:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360 or ball.xcor() < -360:
        scoreboard.clear()
        if ball.xcor() > 360:
            scoreboard.left_increment()
        if ball.xcor() < -360:
            scoreboard.right_increment()
        ball.respawn()
        screen.update()
        threading.Event().wait(1)

screen.exitonclick()