import turtle
import math
from time import sleep

wn = turtle.Screen()
wn.setup(1280, 720)
wn.tracer(0)
wn.bgpic("background_2.png")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("block.gif")
        self.shape("block.gif")
        self.color("white")
        self.penup()
        self.speed(3)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("character.gif")
        self.shape("character.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("vaccine.gif")
        self.shape("vaccine.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


level = [""]


level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X                   XXXXX",
    "X       XX  XXX        XX",
    "XX XXXXXXX  XXX        XX",
    "XX XXX  XX  XXXXXX    XXX",
    "XX            XXXX  XXXXX",
    "XXXXXX        XXXXP XXXXX",
    "XX      XXXXXXXXXXXXXXXXX",
    "X     XXXXXXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX   T        X",
    "XXXXXXXXXXXXXXX    XXXXXX",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX             TX",
    "XX T XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    YXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

treasures = []

level.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -520 + (x * 24)
            screen_y = 230 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            elif character == "P":
                player.goto(screen_x, screen_y)
            elif character == "T":
                treasures.append(Treasure(screen_x, screen_y))


pen = Pen()
player = Player()

walls = []

setup_maze(level[1])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

Gold_left = 3
wn.tracer(0)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            turtle.hideturtle()
            player.gold += treasure.gold
            Gold_left = Gold_left - 1
            turtle.clear()
            treasure.destroy()
            if Gold_left == 0:
                turtle.up()
                turtle.hideturtle()
                turtle.color("white")
                turtle.goto(-500, -50)
                turtle.write("EARNED VACCINE ", font=("궁서", 45, "italic"))
                sleep(3)
                exit()

                # treasures.remove(Treasure)
            wn.update()

        wn.update()

