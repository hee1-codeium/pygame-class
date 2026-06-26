import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# 플레이어(사각형) 및 목표물 설정
rect_x, rect_y = 200, 100
target_rect = pygame.Rect(500, 200, 40, 40)

score = 0

game_font  = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    screen.fill((255, 255, 255))
    
    # 플레이어 이동 로직 (WASD)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: rect_x -= 5
    if keys[pygame.K_d]: rect_x += 5
    if keys[pygame.K_w]: rect_y -= 5
    if keys[pygame.K_s]: rect_y += 5
        
    player_rect = pygame.Rect(rect_x, rect_y, 50, 50)
    
    # 오브젝트 그리기
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    pygame.draw.rect(screen, (0, 0, 255), target_rect)

    score_surface = game_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    if player_rect.colliderect(target_rect):
        score += 10  # 충돌할 때마다 10점씩 추가!
        # 목표물을 다른 랜덤 위치로 옮기는 로직 등이 여기에 들어갈 수 있음
        target_rect.x, target_rect.y = 999, 999 # 임시로 화면 밖으로 치우기

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
            
    pygame.display.flip()

pygame.quit()