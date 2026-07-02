import pygame
import sys
import random

# 1. 초기화 및 기본 세팅
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("시현이의 마우스 클릭 사냥 게임")
clock = pygame.time.Clock()

# 2. 목표 오브젝트들을 담을 '보관함(리스트)' 만들기
targets = []

# 3. 시간 측정 및 점수 변수 설정
last_spawn_time = pygame.time.get_ticks() 
spawn_delay = 1000  # 1초 간격
score = 0

# 4. 폰트 세팅
game_font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    screen.fill((255, 255, 255))  # 바탕을 하얗게 지우기
    
    # [현재 시간 체크 및 1초 간격 랜덤 생성]
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_delay:
        random_x = random.randint(20, SCREEN_WIDTH - 60)
        random_y = random.randint(20, SCREEN_HEIGHT - 60)
        
        new_target = pygame.Rect(random_x, random_y, 40, 40)
        targets.append(new_target)
        last_spawn_time = current_time

    # 🖌️ [오브젝트 그리기]
    # 모든 목표물(파란색) 그리기
    for target in targets:
        pygame.draw.rect(screen, (0, 0, 255), target)
        
    # 점수 텍스트 화면에 그리기
    score_surface = game_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    # 📥 [이벤트 처리 및 마우스 클릭 감지]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # 🖱️ 사용자가 마우스 버튼을 딱 누른 순간을 감지!
        if event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos는 클릭한 마우스의 (X, Y) 좌표를 가지고 있습니다.
            
            # 보관함(리스트)에 있는 모든 목표물을 하나씩 검사
            for target in targets[:]:
                # 🎯 클릭한 마우스 좌표가 이 목표물 사각형 안에 들어가 있다면?
                if target.collidepoint(event.pos):
                    targets.remove(target)  # 목표물 제거!
                    score += 1             # 점수 1점 증가!
                    break                  # 한 번 클릭에 사각형 하나만 지우도록 브레이크

    # 화면 새로고침
    pygame.display.flip()

pygame.quit()
sys.exit()