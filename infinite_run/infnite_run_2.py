import pygame
import sys

pygame.init()
screen = pygame.size = (800, 400)
screen = pygame.display.set_mode(screen)
clock = pygame.time.Clock()

player_rect = pygame.Rect(100, 250, 50, 50)
obs_rect = pygame.Rect(800, 250, 40, 50) 
obs_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    obs_rect.x -= obs_speed

    # 화면 밖으로 나가면 오른쪽 끝으로 리셋
    # + 2단계 핵심: 무작위 위치로 리셋하기
    if obs_rect.x < -40:
        import random # (보통 맨 위에 쓰지만 흐름상 표기)
        obs_rect.x = random.randint(800, 1200) # 등장 타이밍을 랜덤하게 만듦

    screen.fill((255, 255, 255)) 
    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    pygame.draw.rect(screen, (255, 0, 0), obs_rect)  
    
    pygame.display.flip()
    clock.tick(60)