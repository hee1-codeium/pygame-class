import pygame
import sys

pygame.init()
screen = pygame.size = (800, 400)
screen = pygame.display.set_mode(screen)
clock = pygame.time.Clock()

# 1. 캐릭터(공룡 역할)와 장애물 사각형 생성
player_rect = pygame.Rect(100, 250, 50, 50)
obs_rect = pygame.Rect(800, 250, 40, 50) # 오른쪽 끝(800)에서 시작
obs_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. 장애물 이동 (오른쪽에서 왼쪽으로)
    obs_rect.x -= obs_speed

    # [핵심] 3. 화면 밖으로 나가면 오른쪽 끝으로 리셋
    if obs_rect.x < -40:  # 장애물 가로 크기가 40이므로 완전히 사라졌을 때
        obs_rect.x = 800

    # 그리기
    screen.fill((255, 255, 255)) # 하얀 배경
    pygame.draw.rect(screen, (0, 0, 255), player_rect) # 파란 플레이어
    pygame.draw.rect(screen, (255, 0, 0), obs_rect)    # 빨간 장애물
    
    pygame.display.flip()
    clock.tick(60)