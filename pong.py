#@author Tucker Ferguson
#1/14/2020
#This is an implementation of the classic 'pong' using the turtle module

#turtle is a drawing board feature
import turtle

#Main Loop for Pong


#initializing screen
mySn = turtle.Screen()
mySn.title("PyPong Vanilla @TuckerFerg")
mySn.bgcolor("black")
mySn.setup(width=800, height=600)
mySn.tracer(0) 

#Score
score_p1 = 0
score_p2 = 0

#Paddle One
paddle_p1 = turtle.Turtle()
paddle_p1.speed(0)
paddle_p1.shape("square")
paddle_p1.color("white")
paddle_p1.shapesize(stretch_wid=5,stretch_len=1)
paddle_p1.penup()
paddle_p1.goto(-350,0)

#Paddle Two
paddle_p2 = turtle.Turtle()
paddle_p2.speed(0)
paddle_p2.shape("square")
paddle_p2.color("white")
paddle_p2.shapesize(stretch_wid=5,stretch_len=1)
paddle_p2.penup()
paddle_p2.goto(350,0)

#Pong Ball
pong_Ball = turtle.Turtle()
pong_Ball.speed(0)
pong_Ball.shape("square")
pong_Ball.color("white")
pong_Ball.penup()
pong_Ball.goto(0, 0)
pong_Ball.dx = .1
pong_Ball.dy = -.1

#Score keeper
scoreKeeper = turtle.Turtle()
scoreKeeper.speed(0)
scoreKeeper.color("white")
scoreKeeper.penup()
scoreKeeper.hideturtle()
scoreKeeper.goto(0,260)
scoreKeeper.write("Player One:[0]   Player Two:[0]",align="center",font=("Courier",24,"normal"))

#Instructions
instruction = turtle.Turtle()
instruction.speed(0)
instruction.color("green")
instruction.penup()
instruction.hideturtle()
instruction.goto(0,-280)
instruction.write("          P1: up = 'w', down = 's'\n          P2: up = 'o', down = 'k'",align="left",font=("Courier",12,"normal"))


#Up function for player 1
def paddle_p1_up():
    y = paddle_p1.ycor()
    y += 20
    paddle_p1.sety(y)

#down function for player 1
def paddle_p1_down():
    y = paddle_p1.ycor()
    y -= 20
    paddle_p1.sety(y)

#Up function for player 1
def paddle_p2_up():
    y = paddle_p2.ycor()
    y += 20
    paddle_p2.sety(y)

#down function for player 1
def paddle_p2_down():
    y = paddle_p2.ycor()
    y -= 20
    paddle_p2.sety(y)

#Keyboarding Listening
#player
mySn.listen()
mySn.onkeypress(paddle_p1_up, "w")
mySn.onkeypress(paddle_p1_down, "s")
mySn.onkeypress(paddle_p2_up, "o")
mySn.onkeypress(paddle_p2_down, "k")

# Main Loop 
while True :
    mySn.update()

    #Make ball dynamic
    pong_Ball.setx(pong_Ball.xcor() + pong_Ball.dx)
    pong_Ball.sety(pong_Ball.ycor() + pong_Ball.dy)

    #Enforce border checking
    #If ball hits top or bottom border its vector direction reversed
    if(pong_Ball.ycor() > 290):
        pong_Ball.sety(290)
        pong_Ball.dy *= -1
    if(pong_Ball.ycor() < -290):
        pong_Ball.sety(-290)
        pong_Ball.dy *= -1

    #When one player scores on another the ball is reset
    if(pong_Ball.xcor() > 390):
        pong_Ball.goto(0,0)
        pong_Ball.dx *= -1
        score_p1 += 1
        scoreKeeper.clear()
        scoreKeeper.write("Player One:[{0}]  Player Two:[{1}]".format(score_p1,score_p2),align="center",font=("Courier",24,"normal"))
    if(pong_Ball.xcor() < -390):
        pong_Ball.goto(0,0)
        pong_Ball.dx *= -1    
        score_p2 += 1
        scoreKeeper.clear()
        scoreKeeper.write("Player One:[{0}]  Player Two:[{1}]".format(score_p1,score_p2),align="center",font=("Courier",24,"normal"))
    #Paddle / Ball collisions
    if (pong_Ball.xcor() > 340 and pong_Ball.xcor() < 350)and(pong_Ball.ycor() < paddle_p2.ycor() + 40 and pong_Ball.ycor() > paddle_p2.ycor() - 40):
        pong_Ball.setx(340)
        pong_Ball.dx *= -1

    if (pong_Ball.xcor() < -340 and pong_Ball.xcor() > -350) and (pong_Ball.ycor() < paddle_p1.ycor() + 40 and pong_Ball.ycor() > paddle_p1.ycor() - 40):
        pong_Ball.setx(-340)
        pong_Ball.dx *= -1