#Tutorial by  TokyoEdTech

import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Arena")
wn.bgcolor("black")
wn.tracer(0)



pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Sprite():
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.heading += self.da

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0

    def rotate_left(self):
        self.da = 5

    def rotate_right(self):
        self.da = -5

    def stop_rotation(self):
        self.da = 0


# Create player sprite
player = Player(0, 0, "triangle", "white")

enemy = Sprite(0, 100, "square", "red")
enemy.dx = -0.3
enemy.dy = -0.3

powerup = Sprite(0, -100, "circle", "blue")
powerup.dy = 0.5
powerup.dy = 0.1

# Sprites list  
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)

# Key bindings
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")

wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")

# Main loop
while True:
    # Clear screen
    pen.clear()

    # Game logic
    # Update sprites
    for sprite in sprites:
        sprite.update()
    
    # Render sprites 
    for sprite in sprites:
        sprite.render(pen)


    # Update screen 
    wn.update()
