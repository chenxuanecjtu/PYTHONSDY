import turtle as tt
import time
import math

tt.pensize(10)
tt.color('red','crimson')
##########################
tt.penup()
tt.home()
tt.goto(-240,240)
tt.pendown()
tt.forward(150)
tt.penup()
tt.goto(-30-240,-50+240)
tt.pendown()

tt.forward(210)

tt.penup()
tt.goto(75-240,240)
tt.pendown()

# tt.right(105)
# tt.forward(150)
tt.right(105)
for i in range(55):
	tt.right(0.25)
	tt.forward(2.5)
for i in range(20):
	tt.right(0.6)
	tt.forward(2.5)

tt.penup()
tt.goto(75-50*math.tan(15/180*math.pi)-240,-50+240)
tt.pendown()

tt.left(73)
tt.forward(150)

#############

tt.penup()
tt.home()
tt.goto(0,240)
tt.pendown()

tt.forward(150)

tt.penup()
tt.goto(-30,-50+240)
tt.pendown()

tt.forward(210)

tt.penup()
tt.goto(75,0+240)
tt.pendown()

# tt.right(105)
# tt.forward(150)
tt.right(105)
for i in range(55):
	tt.right(0.25)
	tt.forward(2.5)
for i in range(20):
	tt.right(0.6)
	tt.forward(2.5)

tt.penup()
tt.goto(75-50*math.tan(15/180*math.pi),-50+240)
tt.pendown()

tt.left(73)
tt.forward(150)


#############

tt.penup()
tt.home()
tt.goto(-240,0)
tt.pendown()

tt.forward(150)

tt.penup()
tt.goto(-30-230,-50)
tt.pendown()

tt.forward(190)

tt.penup()
tt.home()
tt.goto(40-240,0)
tt.pendown()

# tt.right(105)
# tt.forward(150)
tt.right(90)
tt.forward(80)
for i in range(30):
	tt.right(0.6)
	tt.forward(2.5)

tt.penup()
tt.home()
tt.goto(100-240,0)
tt.pendown()
tt.right(90)
tt.forward(190)

##########################


def curveMove():
    for i in range(200):
        tt.left(1)
        tt.forward(1)


def drawHeart():
    tt.speed(10) 
    tt.begin_fill()
    tt.left(40) 
    tt.forward(111.65)
    curveMove() 
    tt.left(240) 
    curveMove() 
    tt.forward(111.65) 
    tt.end_fill()
tt.penup()
tt.home()
tt.goto(90,-170)
tt.pendown()
drawHeart()
time.sleep (99)





