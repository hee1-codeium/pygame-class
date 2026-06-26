import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("키보드로 사각형 움직이기")
clock = pygame.time.Clock()

# 플레이어 속성 정의 (x좌표, y좌표, 가로, 세로)
player_x = 400
player_y = 300
player_size = 50
player_speed = 5

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # [연속적인 키 입력 처리] 누르고 있는 상태를 체크
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 화면 지우기 (흰색 배경)
    screen.fill((255, 255, 255))
    
    # [도형 그리기] screen에 빨간색(255,0,0)으로 사각형 그리기
    # pygame.draw.rect(그릴곳, 색상, (x, y, 가로, 세로))
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))
    
    pygame.display.update()

pygame.quit()
sys.exit()