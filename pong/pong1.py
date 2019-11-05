#Part 1: Getting started
import turtle
import winsound

wn = turtle.Screen() #make a window
wn.title("Pong by Hunter")
wn.bgcolor("black")
wn.setup(width=800, height=600) #width / height of window
wn.tracer(0)

#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle() #small t for module, capital T for Class name
paddle_a.speed(0) #speed of animation, not speed paddle moves on screen
paddle_a.shape("square") #circle, square, triangle, few others
paddle_a.color("white") #paddle color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #penup so line is not drawn
paddle_a.goto(-350, 0) #start in middle of screen

#Paddle B
paddle_b = turtle.Turtle() #small t for module, capital T for Class name
paddle_b.speed(0) #speed of animation, not speed paddle moves on screen
paddle_b.shape("square") #circle, square, triangle, few others
paddle_b.color("white") #paddle color
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #penup so line is not drawn
paddle_b.goto(350, 0) #start in middle of screen

#Ball
ball = turtle.Turtle() #small t for module, capital T for Class name
ball.speed(0) #speed of animation, not speed paddle moves on screen
ball.shape("square") #circle, square, triangle, few others
ball.color("white") # ball color
ball.penup() #penup so line is not drawn
ball.goto(0, 0) #start in middle of screen
ball.dx = 0.2 #dx = delta/change X coord (Speed of Ball)
ball.dy = 0.2 #dy = delta/change Y coord (Speed of Ball)

# Pen
pen = turtle.Turtle() #draw new turtle
pen.speed(0) #normal animation speed
pen.color("white") #color
pen.penup() #penup so line is not drawn
pen.hideturtle() #hide turtle
pen.goto(0, 260) #position, x=0, y=260
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_a_up():
    y = paddle_a.ycor() #get current y-coord of paddle_a
    y += 20
    paddle_a.sety(y) #set y-coord to y variable

def paddle_a_down():
    y = paddle_a.ycor() #get current y-coord of paddle_a
    y -= 20
    paddle_a.sety(y) #set y-coord to y variable

def paddle_b_up():
    y = paddle_b.ycor() #get current y-coord of paddle_b
    y += 20
    paddle_b.sety(y) #set y-coord to y variable

def paddle_b_down():
    y = paddle_b.ycor() #get current y-coord of paddle_b
    y -= 20
    paddle_b.sety(y) #set y-coord to y variable

#Keyboard binding
wn.listen() #listen for keypress
wn.onkeypress(paddle_a_up, "w") #press W to execute paddle_a_up function
wn.onkeypress(paddle_a_down, "s") #press S to execute paddle_a_down function
wn.onkeypress(paddle_b_up, "Up") #press Up Arrow to execute paddle_b_up function
wn.onkeypress(paddle_b_down, "Down") #press Down Arrow to execute paddle_b_down function


# Main game loop
while True:
    wn.update() #every time the game runs, it updates the screen

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #set ball x-coord to x-coord + delta-x
    ball.sety(ball.ycor() + ball.dy) #set ball y-coord to y-coord + delta-y

    #Border checking
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)