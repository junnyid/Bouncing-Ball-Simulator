# Import library
import math
from tkinter import *

# Width, height of the screen
WIDTH, HEIGHT = 800, 500

class Ball:

    # The init method or constructor
    def __init__(self, canvas, speed, radius, color, initX, initY):

        # Create a circle 
        self.shape = canvas.create_oval(initX, initY, initX + 2 * radius, initY + 2 * radius, fill=color)
        self.radius = radius
        self.canvas = canvas
        self.xspeed = speed
        self.yspeed = speed

    def move_ball(self):

        # this moves the ball to x, y coordinates
        self.canvas.move(self.shape, self.xspeed, self.yspeed)

        # Get the position of the ball
        pos = self.canvas.coords(self.shape)
        
         # if ball get to edge then we need to change direction of movement
        if pos[0] <= 0 or pos[2] >= WIDTH:
            self.xspeed *= -1
        if pos[1] <= 0 or pos[3] >= HEIGHT:
            self.yspeed *= -1

def main():
    tk = Tk()
    tk.title('AllTech - Bouncing ball')
    tk.resizable(0, 0)
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()

    # init list ball 
    list_ball = []

    # Add ball to the list_ball
    list_ball.append(Ball(canvas, 3, 20, 'red', 100, 200))
    list_ball.append(Ball(canvas, 4, 18, 'orange', 200, 100))
    list_ball.append(Ball(canvas, 5, 30, 'blue', 600, 400))
    list_ball.append(Ball(canvas, 6, 15, 'yellow', 400, 200))
    list_ball.append(Ball(canvas, 4, 25, 'green', 500, 350))
    list_ball.append(Ball(canvas, 3, 25, 'indigo', 700, 150))
    list_ball.append(Ball(canvas, 3, 20, 'violet', 300, 200))

    while 1:
        tk.update()
        
        for ball in list_ball:
            ball.move_ball()

        for i in range(0, len(list_ball)):
            ball1 = list_ball[i]
            pos1 = ball1.canvas.coords(ball1.shape)
            centerX1 = pos1[0] + ball1.radius
            centerY1 = pos1[1] + ball1.radius
            for j in range(i + 1, len(list_ball)):
                ball2 = list_ball[j]
                pos2 = ball2.canvas.coords(ball2.shape)
                
                centerX2 = pos2[0] + ball2.radius
                centerY2 = pos2[1] + ball2.radius

                # check the distance between the balls. 
                # If the distance between the center of the two balls is less than the sum of the radius of the balls, then they are colliding.
                checkCollision = math.sqrt((centerX1-centerX2)**2 + (centerY1-centerY2)**2) <= ball1.radius + ball2.radius
                if checkCollision:
                    ball1.xspeed, ball2.xspeed = ball2.xspeed, ball1.xspeed
                    ball1.yspeed, ball2.yspeed = ball2.yspeed, ball1.yspeed
                
        tk.after(1)

main()
