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
    screen.blit(background_04,(0,0))
    screen.blit(face4,(350,150))
    pygame.display.update()
    pygame.time.delay(2000)
    waitForPlayerToPressKey()
    break