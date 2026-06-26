import pygame
import sys

# 1. 초기화 및 화면 설정
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rect 객체를 활용한 충돌 감지")
clock = pygame.time.Clock()

# 2. pygame.Rect(x, y, 가로, 세로) 객체 직접 생성
# 이미지 없이도 사각형의 위치와 크기 정보를 독립된 객체로 관리합니다.
player_rect = pygame.Rect(0, 0, 50, 50)
player_rect.center = (400, 500)  # 시작 위치를 화면 하단 중앙으로 설정
player_speed = 5

enemy_rect = pygame.Rect(0, 0, 60, 60)
enemy_rect.center = (400, 200)   # 적의 위치를 화면 상단에 고정

running = True
while running:
    clock.tick(60)
    
    # [이벤트 처리]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # [키 입력 처리] Rect 객체의 좌표를 직접 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]: player_rect.x += player_speed
    if keys[pygame.K_UP]:    player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:  player_rect.y += player_speed

    # [충돌 감지 및 상태 변경]
    # 두 사각형(Rect)이 겹치면 충돌 상태로 판단하여 색상을 바꿀 준비를 합니다.
    if player_rect.colliderect(enemy_rect):
        enemy_color = (255, 0, 0)      # 충돌 시 적을 빨간색으로 변경
        print("충돌 중!")
    else:
        enemy_color = (0, 0, 255)      # 평소에는 파란색

    # [화면 그리기]
    screen.fill((240, 240, 240))  # 배경은 밝은 회색
    
    # pygame.draw.rect에 변수로 생성해 둔 Rect 객체를 그대로 전달하면 됩니다.
    pygame.draw.rect(screen, (0, 255, 0), player_rect)  # 플레이어: 초록색 사각형
    pygame.draw.rect(screen, enemy_color, enemy_rect)   # 적: 파란색/빨간색 사각형
    
    pygame.display.update()

pygame.quit()
sys.exit()