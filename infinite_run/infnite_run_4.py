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
    dino_image = pygame.image.load(os.path.join(current_path, "dino.png"))
    dino_image = pygame.transform.scale(dino_image, (50, 50))
    cactus_image = pygame.image.load(os.path.join(current_path, "cactus.png"))
    cactus_image = pygame.transform.scale(cactus_image, (40, 50))
except:
    print("이미지가 없어 사각형으로 대체합니다.")

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
        
        # --- [실습 4 추가: 스페이스바 누르면 점프 시작] ---
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                y_velocity = -jump_velocity  # 위쪽 방향(-)으로 힘을 줌

    # --- [실습 4 추가: 물리 및 이동 계산 (게임 중일 때만 작동)] ---
    if not game_over:
        # 점프 및 중력 계산
        if is_jumping:
            player_rect.y += y_velocity
            y_velocity += gravity  # 중력 때문에 속도가 서서히 아래(+)로 내려감
            
            # 바닥(Y=250)에 닿으면 착지 완료
            if player_rect.y >= 250:
                player_rect.y = 250
                is_jumping = False
                y_velocity = 0

        # 장애물 이동 및 리셋 (기존 코드)
        obs_rect.x -= obs_speed
        if obs_rect.x < -40:
            obs_rect.x = random.randint(800, 1100)

        # --- [실습 4 추가: 충돌 감지] ---
        if player_rect.colliderect(obs_rect):
            game_over = True  # 부딪히는 순간 플래그를 True로!

    # 그리기
    screen.fill((255, 255, 255))
    
    # 오브젝트 그리기 (이미지 or 사각형)
    if dino_image: screen.blit(dino_image, player_rect)
    else: pygame.draw.rect(screen, (0, 0, 255), player_rect)

    if cactus_image: screen.blit(cactus_image, obs_rect)
    else: pygame.draw.rect(screen, (255, 0, 0), obs_rect)
    
    # --- [실습 4 추가: 게임오버 시 화면을 붉은색 톤으로] ---
    if game_over:
        # 간단하게 화면을 흐리게 하거나 붉은 상자를 띄워 시각적 효과 줌
        overlay = pygame.Surface((800, 400))
        overlay.fill((255, 0, 0))
        overlay.set_alpha(50)  # 반투명 효과
        screen.blit(overlay, (0,0))
        
    pygame.display.flip()
    clock.tick(60)