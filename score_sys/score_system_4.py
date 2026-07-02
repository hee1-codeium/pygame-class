import pygame
import sys
import random  # 💡 목표물의 랜덤 위치 지정을 위해 추가

# 1. 초기화 및 기본 세팅
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("시현이의 목표물 사냥 게임")
clock = pygame.time.Clock()

# 2. 플레이어(메인 오브젝트) 설정
rect_x, rect_y = 400, 200
rect_speed = 5

# 3. 목표 오브젝트들을 담을 '보관함(리스트)' 만들기
targets = []

# 4. 시간 측정 및 점수 변수 설정
# pygame.time.get_ticks()는 게임이 시작된 후 흘러간 시간을 밀리초(1초=1000ms)로 알려줍니다.
last_spawn_time = pygame.time.get_ticks() 
spawn_delay = 1000  # 1초 간격 (1000밀리초)
score = 0

# 5. 폰트 세팅
game_font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)
    screen.fill((255, 255, 255))  # 바탕을 하얗게 지우기
    
    # [현재 시간 체크]
    current_time = pygame.time.get_ticks()
    
    # ⏱️ 1초(1000ms)가 지났다면? 새로운 목표물을 화면 전체 범위 중 랜덤으로 생성!
    if current_time - last_spawn_time > spawn_delay:
        # 화면 안쪽(여백을 조금 둠)에 생성되도록 범위 지정
        random_x = random.randint(20, SCREEN_WIDTH - 60)
        random_y = random.randint(20, SCREEN_HEIGHT - 60)
        
        # 새 목표물 사각형을 만들어서 보관함(리스트)에 쏙 집어넣기
        new_target = pygame.Rect(random_x, random_y, 40, 40)
        targets.append(new_target)
        
        # 마지막 생성 시간을 현재 시간으로 갱신!
        last_spawn_time = current_time

    # [플레이어 이동 제어 (WASD)]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: rect_x -= rect_speed
    if keys[pygame.K_d]: rect_x += rect_speed
    if keys[pygame.K_w]: rect_y -= rect_speed
    if keys[pygame.K_s]: rect_y += rect_speed
    
    player_rect = pygame.Rect(rect_x, rect_y, 50, 50)

    # 🎯 [충돌 감지 및 사라지기 처리]
    # 리스트에서 항목을 지울 때는 뒤에서부터 검사하거나 복사본을 쓰는 것이 안전합니다.
    for target in targets[:]:
        if player_rect.colliderect(target):
            targets.remove(target)  # 충돌한 목표물은 보관함에서 삭제!
            score += 1             # 점수 1점 획득!

    # 🖌️ [오브젝트 그리기]
    # 1. 모든 목표물(파란색) 그리기
    for target in targets:
        pygame.draw.rect(screen, (0, 0, 255), target)
        
    # 2. 플레이어(빨간색) 그리기
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    
    # 3. 점수 텍스트 화면에 그리기
    score_surface = game_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    # [이벤트 처리 및 화면 새로고침]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()
sys.exit()