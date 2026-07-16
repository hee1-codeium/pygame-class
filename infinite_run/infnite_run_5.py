import pygame
import sys
import random
import os

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# 경로 설정 및 이미지 로드
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

# --- [실습 4 추가: 변수 설정] ---
is_jumping = False
jump_velocity = 15  # 점프 힘
gravity = 1         # 중력 무게
y_velocity = 0

game_over = False   # 게임 상태 관리 변수

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                is_jumping = True
                y_velocity = -jump_velocity
            
            # --- [실습 5 추가: 게임오버 상황에서 R을 누르면 초기화] ---
            if game_over and event.key == pygame.K_R:
                game_over = False
                player_rect.y = 250
                is_jumping = False
                y_velocity = 0
                obs_rect.x = 800  # 장애물도 오른쪽 끝으로 리셋
                obs_rect.x = random.randint(800, 1100)

    # 이동 및 물리 (실습 4와 동일)
    if not game_over:
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
    
    if game_over:
        overlay = pygame.Surface((800, 400))
        overlay.fill((255, 0, 0))
        overlay.set_alpha(50)
        screen.blit(overlay, (0,0))
        
        # --- [실습 5 추가: 화면에 안내 문구 띄우기] ---
        font = pygame.font.SysFont("malgungothic", 30) # 맑은고딕 폰트 안전 로드
        text = font.render("게임 오버! 다시 시작하려면 'R'을 누르세요.", True, (0, 0, 0))
        screen.blit(text, (180, 180))
        
    pygame.display.flip()
    clock.tick(60)