import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

rect_x, rect_y = 200, 100
target_rect = pygame.Rect(500, 200, 40, 40)
score = 0

# -------------------------------------------------------------
# [2단계 추가] 글씨체와 크기 설정하기 (루프 밖)
# -------------------------------------------------------------
# 기본 폰트(None), 크기는 40으로 설정
game_font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    screen.fill((255, 255, 255))
    
    # (이동 및 충돌 로직 생략 - 1단계와 동일)
    player_rect = pygame.Rect(rect_x, rect_y, 50, 50)
    if player_rect.colliderect(target_rect):
        score += 10
        target_rect.x, target_rect.y = 999, 999
        
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    pygame.draw.rect(screen, (0, 0, 255), target_rect)
    
    # -------------------------------------------------------------
    # [2단계 추가] 실시간 점수 숫자를 '글자 도화지'로 구워내기
    # -------------------------------------------------------------
    # font.render(텍스트내용, 부드럽게하기여부, 검은색RGB)
    score_surface = game_font.render(f"Score: {score}", True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    pygame.display.flip()

pygame.quit()