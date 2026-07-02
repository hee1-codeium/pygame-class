import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

rect_x, rect_y = 200, 100
target_rect = pygame.Rect(500, 200, 40, 40)
score = 0
game_font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    
    # 💡 주의: 배경을 먼저 지워야 글자가 안 묻힙니다!
    screen.fill((255, 255, 255)) 
    
    # 플레이어 이동 제어
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: rect_x -= 5
    if keys[pygame.K_d]: rect_x += 5
    if keys[pygame.K_w]: rect_y -= 5
    if keys[pygame.K_s]: rect_y += 5
        
    player_rect = pygame.Rect(rect_x, rect_y, 50, 50)
    
    # 충돌하면 점수 상승
    if player_rect.colliderect(target_rect):
        score += 10
        target_rect.x, target_rect.y = 999, 999
        
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    pygame.draw.rect(screen, (0, 0, 255), target_rect)
    
    # 글자 도화지 생성
    score_surface = game_font.render(f"Score: {score}", True, (0, 0, 0))
    
    # -------------------------------------------------------------
    # [3단계 추가] 메인 화면 왼쪽 위 (10, 10) 자리에 점수판 붙이기
    # -------------------------------------------------------------
    screen.blit(score_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
            
    pygame.display.flip()

pygame.quit()
sys.exit()