import pygame
import sys

# 1. 초기화
pygame.init()

# 2. 화면 설정 (가로, 세로)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame 속성 마스터 - 기본 틀")

# 3. FPS(초당 프레임 수) 설정을 위한 시계 객체
clock = pygame.time.Clock()

# 메인 루프 플래그
running = True

# 4. 메인 루프 시작
while running:
    # FPS 제한 (초당 60프레임)
    clock.tick(60)
    
    # [이벤트 처리] 사용자가 창을 닫았는지 확인
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # [화면 그리기] 배경을 검은색으로 채우기 (RGB)
    screen.fill((0, 0, 0))
    
    # [화면 업데이트] 버퍼에 그린 내용을 실제 모니터에 표시
    pygame.display.update()

# 5. 종료 처리
pygame.quit()
sys.exit()