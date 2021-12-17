import turtle
import math
from time import sleep

# 기본 화면 구성
wn = turtle.Screen()
wn.setup(1280, 720)
wn.tracer(0)
wn.bgpic("background_2.png")


# block.gif 사용해 미로 만들기
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("block.gif")
        self.shape("block.gif")
        self.penup()
        self.speed(3)


# character.gif 사용해 방역복 캐릭터 그리기
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("character.gif")
        self.shape("character.gif")
        self.penup()
        self.speed(0)
        self.gold = 0

    # 캐릭터 미로 안에서 움직임 (up, down, left, right)
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

    # 캐릭터, 아이템 충돌 시
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


# vaccine.gif 사용해 백신 아이템 그리기
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("vaccine.gif")
        self.shape("vaccine.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    # 백신 아이템 충돌 시 아이템 먹기
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# virus.gif 사용해 바이러스 그리기
class Virus(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("virus.gif")
        self.shape("virus.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    # 바이러스 충돌 시 감염
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# X, P, T, V를 사용해 미로와 아이템 나타냄
level = [""]


level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X        T          XXXXX",
    "X       XX  XXX        XX",
    "XX XXXXXXX  XXX   V    XX",
    "XX XXX  XX  XXXXXX    XXX",
    "XX    V       XXXX  XXXXX",
    "XXXXXX      V XXXXP XXXXX",
    "XX  T   XXXXXXXXXXXXXXXXX",
    "X V  VXXXXXXXXXXXXXXXXXXX",
    "X             V  XXXXXXXX",
    "XXXXXXXXXXXX       T    X",
    "XXXXXXXXXXXXXXX   VXXXXXX",
    "XXX  XXXXXXXXXX         X",
    "XXX      V              X",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX             TX",
    "XX T XXXXX      V       X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XXV   YXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX    V               X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

treasures = []
viruses = []

level.append(level_1)


# X, P, T, V를 사용해 미로와 아이템 그리기
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
            elif character == "V":
                viruses.append(Virus(screen_x, screen_y))


pen = Pen()
player = Player()

walls = []

setup_maze(level[1])

# 키보드 방향기
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# 백신 아이템 개수
Vaccine_left = 5
wn.tracer(0)

# 게임 구현 코드 (백신 => 아이템, 바이러스 => 게임 종료)
while True:
    for virus in viruses:
        if player.is_collision(virus):
            turtle.hideturtle()
            turtle.clear()
            virus.destroy()
            wn.update()
            turtle.up()
            turtle.hideturtle()
            turtle.color("white")
            turtle.goto(-500, -50)
            turtle.write("VIRUS INFECTED ", font=("궁서", 45, "italic"))
            sleep(3)
            quit()

    for treasure in treasures:
        if player.is_collision(treasure):
            turtle.hideturtle()
            player.gold += treasure.gold
            Vaccine_left = Vaccine_left - 1
            turtle.clear()
            treasure.destroy()
            if Vaccine_left == 0:
                turtle.clear()
                treasure.destroy()
                wn.update()
                turtle.up()
                turtle.hideturtle()
                turtle.color("white")
                turtle.goto(-500, -50)
                turtle.write("EARNED VACCINE ", font=("궁서", 45, "italic"))
                sleep(3)
                quit()
                # treasures.remove(Treasure)
            wn.update()

        wn.update()
