import pygame 
import random
import sys
from pygame import display
from pygame.font import Font 

pygame.init() # 초기화

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기
pygame.display.set_caption("STAGE_04")
clock = pygame.time.Clock() # FPS(초 당 프레임 수)

background_04 = pygame.image.load('background_04.png')
background_04 = pygame.transform.scale(background_04, (1280, 720)) # 배경 이미지 받고 크기 변환

tmask1 = pygame.image.load('tmask1.png')
tmask1 = pygame.transform.scale(tmask1, (850, 400))
tmask2 = pygame.image.load('tmask2.png')
tmask2 = pygame.transform.scale(tmask2, (550, 350))
tmask3 = pygame.image.load('tmask3.png')
tmask3 = pygame.transform.scale(tmask3, (500, 350))
tmask4 = pygame.image.load('tmask4.png')
tmask4 = pygame.transform.scale(tmask4, (590, 350))

H_face = pygame.image.load('happy_face.png')
H_face = pygame.transform.scale(H_face, (600 ,500))
S_face = pygame.image.load('sad_face.png')
S_face = pygame.transform.scale(S_face,(600, 500))

correct = pygame.image.load('correct.png')
correct = pygame.transform.scale(correct, (400, 300))
tryagain = pygame.image.load('tryagain.png')
tryagain = pygame.transform.scale(tryagain, (400, 300))

font = pygame.font.Font('DungGeunMo.ttf',50)  #폰트 설정
ending_font = pygame.font.Font('DungGeunMo.ttf', 80)

square = pygame.image.load('Question_01_square.png')
square = pygame.transform.scale(square, (768, 432))

count = 2

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
            

def question_01():
    playing = True
    while playing:
        screen.blit(square, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 56 and mouse_pos[0] < 306 and mouse_pos[1] > 220 and mouse_pos[1] < 470 : #답 적을 부분 위치 수정
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
        screen.blit(square, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 56 and mouse_pos[0] < 306 and mouse_pos[1] > 220 and mouse_pos[1] < 470 : #답 적을 부분 위치 수정
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
        screen.blit(square, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 56 and mouse_pos[0] < 306 and mouse_pos[1] > 220 and mouse_pos[1] < 470 : #답 적을 부분 위치 수정
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
        screen.blit(square, (256, 144))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                playing = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 56 and mouse_pos[0] < 306 and mouse_pos[1] > 220 and mouse_pos[1] < 470 : #답 적을 부분 위치 수정
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
    screen.blit(background_04,(0,0))
    screen.blit(S_face,(380,150))
    screen.blit(tmask4,(380,380))
    pygame.display.update()
    pygame.time.delay(2000)
    waitForPlayerToPressKey()
    break

waitForPlayerToPressKey()
pygame.display.update()
question_02()
pygame.display.update()

while True:
    screen.blit(background_04,(0,0))
    screen.blit(S_face,(380,150))
    screen.blit(tmask3,(400,350))
    pygame.display.update()
    pygame.time.delay(2000)
    waitForPlayerToPressKey()
    break

waitForPlayerToPressKey()
pygame.display.update()
question_03()
pygame.display.update()

while True:
    screen.blit(background_04,(0,0))
    screen.blit(H_face,(380,150))
    screen.blit(tmask2,(400,340))
    pygame.display.update()
    pygame.time.delay(2000)
    waitForPlayerToPressKey()
    break

waitForPlayerToPressKey()
pygame.display.update()
question_04()
pygame.display.update()

while True:
    screen.blit(background_04,(0,0))
    screen.blit(H_face,(380,150))
    screen.blit(tmask1,(270,300))
    pygame.display.update()
    pygame.time.delay(2000)
    waitForPlayerToPressKey()
    break