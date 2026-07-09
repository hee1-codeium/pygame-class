import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# --- [안전한 이미지 로드 및 체크 시스템] ---
# 처음에는 이미지가 없는 상태(None)로 시작합니다.
dino_image = None
cactus_image = None

try:
    # 이미지 로드를 시도합니다. (파일명이나 경로가 맞으면 성공!)
    dino_image = pygame.image.load("dino.png")
    dino_image = pygame.transform.scale(dino_image, (50, 50))

    cactus_image = pygame.image.load("cactus.png")
    cactus_image = pygame.transform.scale(cactus_image, (40, 50))
    print("이미지 로드 성공! 캐릭터로 게임을 시작합니다.")
except pygame.error:
    # 폴더에 파일이 없거나 이름이 틀리면 이쪽으로 넘어옵니다.
    # 프로그램이 튕기지 않고, 이미지 변수들은 None 상태를 유지합니다.
    print("이미지 파일을 찾을 수 없습니다! 기본 사각형으로 대체하여 게임을 실행합니다.")

# 오브젝트의 위치와 크기를 담당할 '사각형(Rect)' 생성
player_rect = pygame.Rect(100, 250, 50, 50)
obs_rect = pygame.Rect(800, 250, 40, 50)
obs_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 장애물 이동 및 리셋
    obs_rect.x -= obs_speed
    if obs_rect.x < -40:
        obs_rect.x = random.randint(800, 1100)

    # 화면 그리기
    screen.fill((255, 255, 255)) 

    # --- [핵심] 이미지가 있으면 이미지로, 없으면 사각형으로 그리기 ---
    # 조건문으로 dino_image가 변수에 잘 담겨있는지(None이 아닌지) 체크합니다.
    if dino_image:
        screen.blit(dino_image, player_rect)   # 공룡 이미지 그리기
    else:
        pygame.draw.rect(screen, (0, 0, 255), player_rect)  # 없으면 파란 사각형

    if cactus_image:
        screen.blit(cactus_image, obs_rect)     # 선인장 이미지 그리기
    else:
        pygame.draw.rect(screen, (255, 0, 0), obs_rect)    # 없으면 빨간 사각형
    
    pygame.display.flip()
    clock.tick(60)