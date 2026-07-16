import pygame
import sys
import random
import os

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# 경로 및 이미지 로드
current_path = os.path.dirname(__file__)
dino_image, cactus_image = None, None
try:
    # 이미지 로드를 시도합니다. (dino.png 대신 찾아오신 dino_run.gif를 적용합니다!)
    dino_image = pygame.image.load("./img/dino_run.gif")
    dino_image = pygame.transform.scale(dino_image, (50, 50))
    print("이미지 로드 성공! 캐릭터로 게임을 시작합니다.")

    # 선인장 이미지 로드 (추후 cactus.png 파일이 준비되면 자동으로 적용됩니다)
    cactus_image = pygame.image.load("./img/cactus.png")
    cactus_image = pygame.transform.scale(cactus_image, (40, 50))
    print("이미지 로드 성공! 캐릭터로 게임을 시작합니다.")
except: 
    # 폴더에 파일이 없거나 이름이 틀리면 이쪽으로 넘어옵니다.
    print("로드에 실패한 이미지가 있습니다..")

# 오브젝트 설정
player_rect = pygame.Rect(100, 250, 50, 50)
obs_rect = pygame.Rect(800, 250, 40, 50)
obs_speed = 7

# 변수 설정
is_jumping = False
jump_velocity = 15
gravity = 1
y_velocity = 0
game_over = False   

# --- [실습 6 추가: 점수 변수] ---
score = 0
font = pygame.font.SysFont("arial", 25) # 점수용 영문 폰트 안전 로드

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                is_jumping = True
                y_velocity = -jump_velocity
            
            if game_over and event.key == pygame.K_r:
                game_over = False
                player_rect.y = 250
                is_jumping = False
                y_velocity = 0
                obs_rect.x = random.randint(800, 1100)
                # --- [실습 6 추가: 재시작 시 점수 초기화] ---
                score = 0

    if not game_over:
        # --- [실습 6 추가: 살아있는 동안 점수가 누적됨] ---
        score += 1 

        if is_jumping:
            player_rect.y += y_velocity
            y_velocity += gravity
            if player_rect.y >= 250:
                player_rect.y = 250
                is_jumping = False
                y_velocity = 0

        obs_rect.x -= obs_speed
        if obs_rect.x < -40:
            obs_rect.x = random.randint(800, 1100)

        if player_rect.colliderect(obs_rect):
            game_over = True

    # 그리기
    screen.fill((255, 255, 255))
    
    if dino_image: screen.blit(dino_image, player_rect)
    else: pygame.draw.rect(screen, (0, 0, 255), player_rect)
    if cactus_image: screen.blit(cactus_image, obs_rect)
    else: pygame.draw.rect(screen, (255, 0, 0), obs_rect)
    
    # --- [실습 6 추가: 실시간 점수 화면 렌더링] ---
    score_text = font.render(f"Score: {score}", True, (50, 50, 50))
    screen.blit(score_text, (20, 20)) # 좌측 상단 (20, 20) 위치에 그리기
    
    if game_over:
        overlay = pygame.Surface((800, 400))
        overlay.fill((255, 0, 0))
        overlay.set_alpha(50)
        screen.blit(overlay, (0,0))
        
        # 시스템 한글 폰트로 다시 그리기
        ko_font = pygame.font.SysFont("malgungothic", 30)
        text = ko_font.render("게임 오버! 다시 시작하려면 'R'을 누르세요.", True, (0, 0, 0))
        screen.blit(text, (180, 180))
        
    pygame.display.flip()
    clock.tick(60)