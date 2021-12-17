import pygame 
import random
import time

pygame.init() # 초기화
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기
pygame.display.set_caption("바이러스 잡기")
clock = pygame.time.Clock()  # FPS(초 당 프레임 수)


# 전역변수 선언

result_font = pygame.font.Font('C:/Users/ivywe/Downloads/neodgm.ttf', 80)
setting_font = pygame.font.Font('C:/Users/ivywe/Downloads/neodgm.ttf', 40) # 결과, 기능 폰트

score = 0 # 스코어
time_left = 60 # 시간
time_start = int(time.time()) # 현재 시각 구하기

background = pygame.image.load('C:/Users/ivywe/Downloads/게임 화면_3.png')
background = pygame.transform.scale(background, (1280, 720)) # 배경 이미지 받고 크기 변환

virus_image = pygame.image.load('C:/Users/ivywe/Downloads/바이러스.png')

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
        time_left = 60 - (current_time - time_start)

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

pygame.quit()

