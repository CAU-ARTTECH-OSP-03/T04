import pygame 
import random
import sys
from pygame import display 
import turtle
import math
from time import sleep
import time
import sys
from pygame import display
from pygame.font import Font 

pygame.init() # 초기화


def sTage01_game() :
    
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기
    pygame.display.set_caption("바이러스 피하기")
    clock = pygame.time.Clock() # FPS(초 당 프레임 수)

# 전역변수 선언

    result_font = pygame.font.Font('DungGeunMo.ttf', 80)
    setting_font = pygame.font.Font('DungGeunMo.ttf', 40) # 결과, 기능 폰트

    score = 0 # 스코어
    heart = 3 # 생명

    background = pygame.image.load('background.png')
    background = pygame.transform.scale(background, (1280, 720)) # 배경 이미지 받고 크기 변환

    item_image = pygame.image.load('item.png')
    item_image = pygame.transform.scale(item_image, (100, 100)) # 아이템 이미지 받고 크기 변환
    items = []

# 아이템 rect 정보 받고 위치, 속도 설정

    for i in range(4):
        item = item_image.get_rect()
        item.left = random.randint(0, screen_width - item.width)
        item.top = -100
        ds = random.randint(6, 12)
        items.append({'item': item, 'ds': ds})

    
    virus1_image = pygame.image.load('virus1.png')
    virus1_image = pygame.transform.scale(virus1_image, (60, 60)) # 바이러스 이미지 받고 크기 변환
    viruses1 = []

    virus2_image = pygame.image.load('virus4.png')
    virus2_image = pygame.transform.scale(virus2_image, (60, 60)) # 바이러스 이미지 받고 크기 변환
    viruses2 = []


# 바이러스1 rect 정보 받고 위치, 속도 설정

    for i in range(4):
        virus1 = virus1_image.get_rect()
        virus1.left = random.randint(0, screen_width - virus1.width)
        virus1.top = - 100
        ds = random.randint(6, 12)
        viruses1.append({'virus1': virus1, 'ds': ds})

# 바이러스2 rect 정보 받고 위치, 속도 설정

    for i in range(4):
        virus2 = virus2_image.get_rect()
        virus2.left = random.randint(0, screen_width - virus2.width)
        virus2.top = - 100
        ds = random.randint(6, 12)
        viruses2.append({'virus2': virus2, 'ds': ds})

    character_image = pygame.image.load('person.png')
    character_image = pygame.transform.scale(character_image, (80, 80)) # 캐릭터 이미지 받고 크기 변환

# 캐릭터 rect 정보 받고 위치 설정
    character = character_image.get_rect()
    character.left = (screen_width / 2) - (character.width / 2)
    character.top = screen_height - character.height
    character_dx = 0 


# 바이러스, 아이템 계속 추가

    def add_item(item):
        item = item_image.get_rect()
        item.left = random.randint(0, screen_width - item.width)
        item.top = -100
        ds = random.randint(6, 12)
        items.append({'item': item, 'ds': ds})

    def add_virus1(virus1):
        virus1 = virus1_image.get_rect()
        virus1.left = random.randint(0, screen_width - virus1.width)
        virus1.top = - 100
        ds = random.randint(6, 12)
        viruses1.append({'virus1': virus1, 'ds': ds}) 

    def add_virus2(virus2):
        virus2 = virus2_image.get_rect()
        virus2.left = random.randint(0, screen_width - virus2.width)
        virus2.top = - 100
        ds = random.randint(6, 12)
        viruses2.append({'virus2': virus2, 'ds': ds}) # 게임 진행 중 바이러스, 아이템 제거되는 오류 수정    
                                                  # rect 정보(위치, 속도) 업데이트 후 추가
   
#음악은 나중에 아무거나 다운받아서
# pygame.mixer.init()
# pygame.mixer.music.load('music.mid') #배경 음악
# pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
# game_over_sound = pygame.mixer.Sound('game_over.wav')

# 게임 실행 루프

    running = True
    while running:
        clock.tick(30) #30 FPS
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False # 창 닫으면 게임 종료
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_dx -= 5 # 왼쪽 방향키 누르면 왼쪽으로 이동
                elif event.key == pygame.K_RIGHT:
                    character_dx += 5 # 오른쪽 방향키 누르면 오른쪽으로 이동
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_dx = 0 # 방향키 안 누르면 멈춤

        for item in items:
            item['item'].top += item['ds'] # 아이템이 떨어질 때
            if item['item'].top > screen_height: # 바닥 밑으로 떨어지면
                items.remove(item) 
                item = item_image.get_rect()
                item.left = random.randint(0, screen_width - item.width)
                item.top = - 100 # 다시 생성하고 위치 재설정
                ds = random.randint(6, 12)
                items.append({'item': item, 'ds': ds})
            
        for virus1 in viruses1:
            virus1['virus1'].top += virus1['ds'] # 바이러스 떨어질 때
            if virus1['virus1'].top > screen_height: # 바닥 밑으로 떨어지면
                viruses1.remove(virus1)
                virus1 = virus1_image.get_rect()
                virus1.left = random.randint(0, screen_width - virus1.width)
                virus1.top = - 100 #다시 생성하고 위치 재설정
                ds = random.randint(6,12)
                viruses1.append({'virus1': virus1, 'ds': ds})

        for virus2 in viruses2:
            virus2['virus2'].top += virus2['ds'] # 바이러스 떨어질 때
            if virus2['virus2'].top > screen_height: # 바닥 밑으로 떨어지면
                viruses2.remove(virus2)
                virus2 = virus2_image.get_rect()
                virus2.left = random.randint(0, screen_width - virus2.width)
                virus2.top = - 100 #다시 생성하고 위치 재설정
                ds = random.randint(6,12)
                viruses2.append({'virus2': virus2, 'ds': ds})

        character.left += character_dx # 캐릭터 위치 정의

# 경계값 설정(캐릭터가 화면 밖으로 못 나가도록)

        if character.left < 0:
            character.left = 0
        elif character.left > screen_width - character.width:
            character.left = screen_width - character.width

# 배경, 캐릭터 화면에 나타내기        

        screen.blit(background, (0, 0)) # 배경 화면에 그리기
        screen.blit(character_image, character) # 캐릭터 화면에 그리기
    

# 아이템/바이러스와 충돌 시

# 아이템
        for item in items:
            if item['item'].colliderect(character): # 충돌 확인
                items.remove(item)
                add_item(item)
                score += 1 # 스코어 올라감
            screen.blit(item_image, item['item']) # 아이템 화면에 그리기
                
                # pygame.mixer.music.stop()
                # score_sound.play()
# 바이러스1              
        for virus1 in viruses1:
            if virus1['virus1'].colliderect(character):
                viruses1.remove(virus1)
                add_virus1(virus1)
                score -= 1
                heart -= 1 # 스코어, 생명 깎임
            screen.blit(virus1_image, virus1['virus1']) # 바이러스 화면에 그리기

        for virus2 in viruses2:
            if virus2['virus2'].colliderect(character):
                viruses2.remove(virus2)
                add_virus2(virus2)
                score -= 1
                heart -= 1 # 스코어, 생명 깎임
            screen.blit(virus2_image, virus2['virus2']) # 바이러스 화면에 그리기
            
        if score > 1:
            screen.blit(game_clear_image, game_clear)
            running = False # 2초 대기 후 종료
        
        elif score < 0 or heart == 0:
            screen.blit(game_over_image, game_over)
            running = False # 2초 대기 후 종료
         
    
# 알림 메세지(스코어, 생명, 결과)

        score_image = setting_font.render("SCORE  "+str(score), True, (255, 255, 0)) # 노란색
        screen.blit(score_image, (10, 10)) # 스코어 메세지 화면에 그리기

        heart_image = setting_font.render("HEART  "+str(heart), True, (255, 0, 0)) # 빨강색
        screen.blit(heart_image, (10,40)) # 생명 개수 메세지 화면에 그리기

        game_clear_image = result_font.render("GAME CLEAR!", True, (0, 255, 0)) # 초록색
        game_clear = game_clear_image.get_rect(center = (int(screen_width / 2), int(screen_height / 2))) # 메세지 위치 설정
    
        game_over_image = result_font.render("GAME OVER!", True, (255, 0, 0)) # 빨강색
        game_over = game_over_image.get_rect(center = (int(screen_width / 2), int(screen_height / 2))) # 메세지 위치 설정

        pygame.display.update() # 화면 업데이트

    pygame.time.delay(2000) # 2초 대기
    return False
    

#######################################################################################################
pygame.init() # 초기화
clock = pygame.time.Clock() # FPS(초 당 프레임 수)
font = pygame.font.Font('DungGeunMo.ttf',50)  #폰트 설정
stage = -1
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기

stage_01_back = pygame.image.load('stage_first_back.png')
stage_01_back = pygame.transform.scale(stage_01_back, (1280, 720)) # 배경 이미지 받고 크기 변환
stage_02_back = pygame.image.load('stage_02_back.png')
stage_02_back = pygame.transform.scale(stage_02_back, (1280, 720)) # 배경 이미지 받고 크기 변환

stage_01_button_image = pygame.image.load("stage_01_image.png")
stage_01_button_image = pygame.transform.scale(stage_01_button_image, (220,220))

stage_02_button_image = pygame.image.load("stage_02_image.png")
stage_02_button_image = pygame.transform.scale(stage_02_button_image, (220,220))

stage_03_button_image = pygame.image.load("stage_03_image.png")
stage_03_button_image = pygame.transform.scale(stage_03_button_image, (220,220))

stage_04_button_image = pygame.image.load("stage_04_image.png")
stage_04_button_image = pygame.transform.scale(stage_04_button_image, (220,220))

button_01 = stage_01_button_image.get_rect()
button_02 = stage_02_button_image.get_rect()
button_03 = stage_03_button_image.get_rect()
button_04 = stage_04_button_image.get_rect()

start_button = pygame.image.load('start_button.png')
start_button = pygame.transform.scale(start_button, (320, 100))
startbutton = start_button.get_rect()

def terminate():
    pygame.quit()
    exit()
def waitForPlayerToPressKey():
    while True:
        screen.blit(stage_01_back, (0,0))
        text = font.render("PRESS ANY KEY TO CONTINUE",True,(255,255,255))  #텍스트가 표시된 Surface 를 만듬
        screen.blit(text,(330,600))    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return
        
        
def background_01():
    screen.blit(stage_01_back, (0,0))
    screen.blit(start_button, (480, 500))

def background_02_04():
    screen.blit(stage_02_back, (0, 0))
    screen.blit(stage_01_button_image, (56, 220))
    screen.blit(stage_02_button_image, (312, 220))
    screen.blit(stage_03_button_image, (618, 220))
    screen.blit(stage_04_button_image, (924, 220))
    text1 = font.render("GAME 01",True,(255, 255 ,255))  #텍스트가 표시된 Surface 를 만듬
    screen.blit(text1,(56,480))
    text2 = font.render("GAME 02",True,(255, 255 ,255))  #텍스트가 표시된 Surface 를 만듬
    screen.blit(text2,(332,480))
    text3 = font.render("GAME 03",True,(255, 255 ,255))  #텍스트가 표시된 Surface 를 만듬
    screen.blit(text3,(638,480))
    text4 = font.render("GAME 04",True,(255, 255 ,255))  #텍스트가 표시된 Surface 를 만듬
    screen.blit(text4,(944,480))
#######################################################################################################

# 기본 화면 구성
def stage_04():

    wn = turtle.Screen()
    wn.setup(1280, 720)
    wn.tracer(0)
    wn.bgpic("background_2.png")


    # block.gif 사용해 미로 만들기
    class Maze(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            v = self.getscreen()
            v.register_shape("block.gif")
            self.shape("block.gif")
            self.penup()
            self.speed(3)


    # character.gif 사용해 방역복 캐릭터 그리기
    class Character(turtle.Turtle):
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


    pen = Maze()
    player = Character()

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

#######################################################################################################

def stage_02():

    pygame.init() # 초기화
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기
    pygame.display.set_caption("바이러스 잡기")
    clock = pygame.time.Clock()  # FPS(초 당 프레임 수)


    # 전역변수 선언

    result_font = pygame.font.Font('DungGeunMo.ttf', 80)
    setting_font = pygame.font.Font('DungGeunMo.ttf', 40) # 결과, 기능 폰트

    score = 0 # 스코어
    time_left = 60 # 시간
    time_start = int(time.time()) # 현재 시각 구하기

    background = pygame.image.load('게임 화면_3.png')
    background = pygame.transform.scale(background, (1280, 720)) # 배경 이미지 받고 크기 변환

    virus_image = pygame.image.load('virus1.png')

    virus_image = pygame.transform.scale(virus_image, (100, 100))

    viruses = []

    for i in range(2):
        virus = virus_image.get_rect()
        virus.left = random.randint(0, screen_width - virus.width)
        virus.top = random.randint(0, screen_height - virus.height)
        appear_time = random.randint(0, 3)
        remain_time = random.randint(1, 3)
        virus_appear = int(time.time()) + appear_time
        virus_gone = int(time.time()) + appear_time + remain_time
        viruses.append((virus, virus_appear, virus_gone))

    def add_virus(virus):
        virus = virus_image.get_rect()
        virus.left = random.randint(0, screen_width - virus.width)
        virus.top = random.randint(0, screen_height - virus.height)
        appear_time = random.randint(0, 3)
        remain_time = random.randint(1, 3)
        virus_appear = int(time.time()) + appear_time
        virus_gone = int(time.time()) + appear_time + remain_time
        viruses.append((virus, virus_appear, virus_gone))


    # 게임 실행 루프

    running = True
    
    while running:
        screen.blit(background, (0, 0)) # 배경화면 그리기
        clock.tick(30)

        event = pygame.event.poll() 
        if event.type == pygame.QUIT:
            running = False # 창 닫으면 게임 종료
        
        elif event.type == pygame.MOUSEBUTTONDOWN and running:
            print(event.pos[0], event.pos[1])
            for virus, virus_appear, virus_gone in viruses:
                if virus.collidepoint(event.pos): # 마우스로 바이러스 클릭 시
                    print(virus)
                    viruses.remove((virus, virus_appear, virus_gone))
                    add_virus(virus)
                    score += 1 # 스코어 올라감, 바이러스 없어졌다가 다시 생성

        if running:       
            current_time = int(time.time())
            time_left = 10 - (current_time - time_start)

            if time_left <= 0:
                if score < 120:
                    screen.blit(game_over_image, game_over)
                else:
                    screen.blit(game_clear_image, game_clear)
                running = False
            
                for virus, virus_appear, virus_gone in viruses:
                    current_time = int(time.time())
                    if appear_time > current_time:
                        viruses.remove((virus, virus_appear, virus_gone))

            for virus, virus_appear, virus_gone in viruses:
                current_time = int(time.time())
                if current_time > virus_gone:
                    viruses.remove((virus, virus_appear, virus_gone))
                    add_virus(virus)
   

        #화면 그리기

        for virus, virus_appear, virus_gone in viruses:
            current_time = int(time.time())
            if  current_time >= appear_time:  
                screen.blit(virus_image, virus)

        # 알림 메세지(스코어, 시간, 결과)

        score_image = setting_font.render("SCORE  "+str(score), True, (255, 255, 0)) # 노란색
        screen.blit(score_image, (10, 10)) # 스코어 메세지 화면에 그리기
        time_left_image = setting_font.render("TIME   "+str(time_left), True, (255, 0, 0)) # 빨강색
        screen.blit(time_left_image, time_left_image.get_rect(right = screen_width - 10, top=10))

        game_clear_image = result_font.render("GAME CLEAR!", True, (0, 255, 0)) # 초록색
        game_clear = game_clear_image.get_rect(center = (int(screen_width / 2), int(screen_height / 2))) # 메세지 위치 설정
    
        game_over_image = result_font.render("GAME OVER!", True, (255, 0, 0)) # 빨강색
        game_over = game_over_image.get_rect(center = (int(screen_width / 2), int(screen_height / 2))) # 메세지 위치 설정

        pygame.display.update() # 화면 업데이트
   
    pygame.time.delay(2000) # 2초 대기

    

#######################################################################################################

def stage_03():

    pygame.init() # 초기화

    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기
    pygame.display.set_caption("STAGE_04")
    clock = pygame.time.Clock() # FPS(초 당 프레임 수)

    background_04 = pygame.image.load('background_04.png')
    background_04 = pygame.transform.scale(background_04, (1280, 720)) # 배경 이미지 받고 크기 변환
    face1 = pygame.image.load('face1.png')
    face1 = pygame.transform.scale(face1, (600 ,500))
    face2 = pygame.image.load('face2.png')
    face2 = pygame.transform.scale(face2, (600 ,500))
    face3 = pygame.image.load('face3.png')
    face3 = pygame.transform.scale(face3, (600 ,500))
    face4 = pygame.image.load('face4.png')
    face4 = pygame.transform.scale(face4, (600 ,500))

    correct = pygame.image.load('correct.png')
    correct = pygame.transform.scale(correct, (400, 300))
    tryagain = pygame.image.load('tryagain.png')
    tryagain = pygame.transform.scale(tryagain, (400, 300))

    font = pygame.font.Font('DungGeunMo.ttf',50)  #폰트 설정
    ending_font = pygame.font.Font('DungGeunMo.ttf', 80)

    Q1 = pygame.image.load('Q1.png')
    Q1 = pygame.transform.scale(Q1, (768, 432))
    Q2 = pygame.image.load('Q2.png')
    Q2 = pygame.transform.scale(Q2, (768, 432))
    Q3 = pygame.image.load('Q3.png')
    Q3 = pygame.transform.scale(Q3, (768, 432))
    Q4 = pygame.image.load('Q4.png')
    Q4 = pygame.transform.scale(Q4, (768, 432))

    A1 = pygame.image.load('A1.png')
    A1 = pygame.transform.scale(A1, (768, 432))
    A2 = pygame.image.load('A2.png')
    A2 = pygame.transform.scale(A2, (768, 432))
    A3 = pygame.image.load('A3.png')
    A3 = pygame.transform.scale(A3, (768, 432))
    A4 = pygame.image.load('A4.png')
    A4 = pygame.transform.scale(A4, (768, 432))

    
    def terminate():
        pygame.quit()
        exit()
    def waitForPlayerToPressKey():
        while True:
            text = font.render("PRESS ANY KEY TO CONTINUE",True,(255,255,255))  #텍스트가 표시된 Surface 를 만듬
            screen.blit(text,(330,350))    
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
                    return
    def waitQuestion():
        while True:
            text = font.render("PRESS ANY KEY TO CONTINUE",True,(255,255,255))  #텍스트가 표시된 Surface 를 만듬
            screen.blit(text,(330,400))    
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
                    return screen.blit(background_04,(0,0))

    def waitClick():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
                    return screen.blit(background_04,(0,0))
            

    def question_01():
        playing = True
        while playing:
            screen.blit(Q1, (256, 144))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    playing = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    pygame.mouse.get_rel()
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] > 410 and mouse_pos[0] < 530 and mouse_pos[1] > 370 and mouse_pos[1] < 510 : #답 적을 부분 위치 수정
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(correct, (455, 200))
                                pygame.display.update()
                                waitQuestion()
                            
                                return False
                    else:
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(tryagain,(450, 200))
                                pygame.display.update() 
                                waitQuestion()
                                return question_01()
    def question_02():
        playing = True
        while playing:
            screen.blit(Q2, (256, 144))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    playing = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    pygame.mouse.get_rel()
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] > 742 and mouse_pos[0] < 860 and mouse_pos[1] > 368 and mouse_pos[1] < 508 : #답 적을 부분 위치 수정
                         if pygame.mouse.get_pressed():
                             while True:
                                screen.blit(correct, (455, 200))
                                pygame.display.update()
                                waitQuestion()
                                return False
                    else:
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(tryagain,(450, 200))
                                pygame.display.update() 
                                waitQuestion()
                                return question_02()
    def question_03():
        playing = True
        while playing:
            screen.blit(Q3, (256, 144))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    playing = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    pygame.mouse.get_rel()
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] > 328 and mouse_pos[0] < 499 and mouse_pos[1] > 413 and mouse_pos[1] < 440 : #답 적을 부분 위치 수정
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(correct, (455, 200))
                                pygame.display.update()
                                waitQuestion()
                                return False
                    else:
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(tryagain,(450, 200))
                                pygame.display.update() 
                                waitQuestion()
                                return question_03()                            
    def question_04():
        playing = True
        while playing:
            screen.blit(Q4, (256, 144))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    playing = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    pygame.mouse.get_rel()
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] > 742 and mouse_pos[0] < 860 and mouse_pos[1] > 368 and mouse_pos[1] < 508 : #답 적을 부분 위치 수정
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(correct, (455, 200))
                                pygame.display.update()
                                waitQuestion()
                                return False
                    else:
                        if pygame.mouse.get_pressed():
                            while True:
                                screen.blit(tryagain,(450, 200))
                                pygame.display.update() 
                                waitQuestion()
                                return question_04()

    screen.blit(background_04,(0,0))
    waitForPlayerToPressKey()
    pygame.display.update()
    question_01()
    pygame.display.update()

    while True:
        screen.blit(A1, (256, 144))
        pygame.display.update()
        waitClick()
        screen.blit(background_04,(0,0))
        screen.blit(face1,(350,150))
        pygame.display.update()
        pygame.time.delay(2000)
        waitForPlayerToPressKey()
        break

    waitForPlayerToPressKey()
    pygame.display.update()
    question_02()
    pygame.display.update()

    while True:
        screen.blit(A2, (256, 144))
        pygame.display.update()
        waitClick()
        screen.blit(background_04,(0,0))
        screen.blit(face2,(350,150))
        pygame.display.update()
        pygame.time.delay(2000)
        waitForPlayerToPressKey()
        break

    waitForPlayerToPressKey()
    pygame.display.update()
    question_03()
    pygame.display.update()

    while True:
        screen.blit(A3, (256, 144))
        pygame.display.update()
        waitClick()
        screen.blit(background_04,(0,0))
        screen.blit(face3,(350,150))
        pygame.display.update()
        pygame.time.delay(2000)
        waitForPlayerToPressKey()
        break

    waitForPlayerToPressKey()
    pygame.display.update()
    question_04()
    pygame.display.update()

    while True:
        screen.blit(A4, (256, 144))
        pygame.display.update()
        waitClick()
        screen.blit(background_04,(0,0))
        screen.blit(face4,(350,150))
        pygame.display.update()
        pygame.time.delay(2000)
        waitForPlayerToPressKey()
        break



def return_false():
    return False
#######################################################################################################
######실행
Ql1 = pygame.image.load('Ql1.png')
Ql1 = pygame.transform.scale(Ql1, (768, 432))
Ql2 = pygame.image.load('Ql2.png')
Ql2 = pygame.transform.scale(Ql2, (768, 432))
Ql3 = pygame.image.load('Ql3.png')
Ql3 = pygame.transform.scale(Ql3, (768, 432))

Al1 = pygame.image.load('Al1.png')
Al1 = pygame.transform.scale(Al1, (768, 432))
Al2 = pygame.image.load('Al2.png')
Al2 = pygame.transform.scale(Al2, (768, 432))
Al3 = pygame.image.load('Al3.png')
Al3 = pygame.transform.scale(Al3, (768, 432))

background_04 = pygame.image.load('background_04.png')
background_04 = pygame.transform.scale(background_04, (1280, 720))
correct = pygame.image.load('correct.png')
correct = pygame.transform.scale(correct, (400, 300))
tryagain = pygame.image.load('tryagain.png')
tryagain = pygame.transform.scale(tryagain, (400, 300))

def waitClick():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
                    return screen.blit(background_04,(0,0))

def waitQuestion():
        while True:
            text = font.render("PRESS ANY KEY TO CONTINUE",True,(255,255,255))  #텍스트가 표시된 Surface 를 만듬
            screen.blit(text,(330,400))    
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
                    return screen.blit(background_04,(0,0))

def Question_end_01() :
    playing = True
        
    while playing:
        screen.blit(Ql1, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 742 and mouse_pos[0] < 860 and mouse_pos[1] > 368 and mouse_pos[1] < 508 : #답 적을 부분 위치 수정
                    if pygame.mouse.get_pressed():
                        while True:
                            screen.blit(correct, (455, 200))
                            pygame.display.update()
                            waitQuestion()
                            
                            return False
                else:
                    if pygame.mouse.get_pressed():
                        while True:
                            screen.blit(tryagain,(450, 200))
                            pygame.display.update() 
                            waitQuestion()
                            return Question_end_01()

    
def Question_end_02() :
    playing = True
    while playing:
        screen.blit(Ql2, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 742 and mouse_pos[0] < 860 and mouse_pos[1] > 368 and mouse_pos[1] < 508 : #답 적을 부분 위치 수정
                    if pygame.mouse.get_pressed():
                        while True:
                            screen.blit(correct, (455, 200))
                            pygame.display.update()
                            waitQuestion()
                            
                            return False
                else:
                    if pygame.mouse.get_pressed():
                        while True:
                            screen.blit(tryagain,(450, 200))
                            pygame.display.update() 
                            waitQuestion()
                            return Question_end_01()


def Question_end_03() :
    playing = True
    while playing:
        screen.blit(Ql3, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 742 and mouse_pos[0] < 860 and mouse_pos[1] > 368 and mouse_pos[1] < 508 : #답 적을 부분 위치 수정
                    if pygame.mouse.get_pressed():
                        while True:
                            screen.blit(correct, (455, 200))
                            pygame.display.update()
                            waitQuestion()
                            
                            return False
                else:
                    if pygame.mouse.get_pressed():
                        while True:
                            screen.blit(tryagain,(450, 200))
                            pygame.display.update() 
                            waitQuestion()
                            return Question_end_01()


waitForPlayerToPressKey()
playing = True
while playing :
    background_02_04()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            playing = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            pygame.mouse.get_rel()
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] > 56 and mouse_pos[0] < 306 and mouse_pos[1] > 220 and mouse_pos[1] < 470 :
                if pygame.mouse.get_pressed():
                    sTage01_game() 
                    return_false()
                    Question_end_01()
                    while True:
                        screen.blit(Al1, (256, 144))
                        pygame.display.update()
                        waitClick()
                        screen.blit(background_04,(0,0))
                        pygame.display.update()
                        break
            elif mouse_pos[0] > 312 and mouse_pos[0] < 532 and mouse_pos[1] > 220 and mouse_pos[1] < 470 :
                    if pygame.mouse.get_pressed():
                        stage_02()
                        return_false()
                        Question_end_02()
                        while True:
                            screen.blit(Al2, (256, 144))
                            pygame.display.update()
                            waitClick()
                            screen.blit(background_04,(0,0))
                            pygame.display.update()
                            break
            elif mouse_pos[0] > 618 and mouse_pos[0] < 838 and mouse_pos[1] > 220 and mouse_pos[1] < 470 :
                if pygame.mouse.get_pressed():
                    stage_03()
                    return_false()
                    Question_end_03()
                    while True:
                        screen.blit(Al3, (256, 144))
                        pygame.display.update()
                        waitClick()
                        screen.blit(background_04,(0,0))
                        pygame.display.update()
                        
                        pygame.quit
            elif mouse_pos[0] > 924 and mouse_pos[0] < 1144 and mouse_pos[1] > 220 and mouse_pos[1] < 470 :
                if pygame.mouse.get_pressed():
                    stage_04()
                    return_false()
            
