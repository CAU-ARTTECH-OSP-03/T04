import pygame 
import random 

pygame.init() # 초기화

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기
pygame.display.set_caption("바이러스 피하기")
clock = pygame.time.Clock() # FPS(초 당 프레임 수)

# 전역변수 선언

result_font = pygame.font.Font('C:/Users/ivywe/Downloads/neodgm.ttf', 80)
setting_font = pygame.font.Font('C:/Users/ivywe/Downloads/neodgm.ttf', 40) # 결과, 기능 폰트

score = 0 # 스코어
heart = 3 # 생명

background = pygame.image.load('C:/Users/ivywe/Downloads/화면.png')
background = pygame.transform.scale(background, (1280, 720)) # 배경 이미지 받고 크기 변환

item_image = pygame.image.load('C:/Users/ivywe/Downloads/아이템.png')
item_image = pygame.transform.scale(item_image, (100, 100)) # 아이템 이미지 받고 크기 변환
items = []

# 아이템 rect 정보 받고 위치, 속도 설정

for i in range(4):
    item = item_image.get_rect()
    item.left = random.randint(0, screen_width - item.width)
    item.top = -100
    ds = random.randint(6, 12)
    items.append({'item': item, 'ds': ds})

    
virus1_image = pygame.image.load('C:/Users/ivywe/Downloads/바이러스.png')
virus1_image = pygame.transform.scale(virus1_image, (60, 60)) # 바이러스 이미지 받고 크기 변환
viruses1 = []

virus2_image = pygame.image.load('C:/Users/ivywe/Downloads/바이러스 4.png')
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

character_image = pygame.image.load('C:/Users/ivywe/Downloads/캐릭터.png')
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
            
    if score > 30:
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

pygame.quit()


