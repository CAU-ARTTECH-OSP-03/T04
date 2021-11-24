import pygame 
import random

pygame.init() # 초기화
clock = pygame.time.Clock() # FPS(초 당 프레임 수)


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
        screen.blit(start_button, (480, 500))
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


def background_02():
    screen.blit(stage_02_back, (0, 0))
    screen.blit(stage_01_button_image, (56, 220))
    screen.blit(stage_02_button_image, (312, 220))
    screen.blit(stage_03_button_image, (618, 220))
    screen.blit(stage_04_button_image, (924, 220))

background_01
pygame.display.update()
waitForPlayerToPressKey()
while True:
    background_02()
    pygame.display.update()
    

