import random
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
background = pygame.image.load('background.png')
statek = pygame.image.load(']statek.png')
scaled_statek = pygame.transform.scale(statek, (100,100))
wrogi_statek = pygame.image.load('wrogi_statek.png')
scaled_wrogi_statek = pygame.transform.scale(wrogi_statek, (100,100))

bullet_img = pygame.image.load('bullet.png')
scaled_bullet_img = pygame.transform.scale(bullet_img, (50,50))

points = 0
running = True
velocity_x = 0
velocity_y = 0
speed = 5
rect_color = (0, 255, 0)
rect_position = [100, 100]
rect_size = [50, 50]

waves_spawn_interval = 1000
current_time = 0
last_time_spawn = 0
enemies = []
current_wave = 0

clock = pygame.time.Clock()
bullets = []

pygame.display.set_caption(str(points))
def strike(cords):
    bullets.append(cords)


def draw_bullet():
    i = 0
    bullet_speed = 10
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        screen.blit(scaled_bullet_img,bullet)





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    velocity_y = -1
                elif event.key == pygame.K_s:
                    velocity_y = 1
                elif event.key == pygame.K_a:
                    velocity_x = -1
                elif event.key == pygame.K_d:
                    velocity_x = 1
                elif event.key == pygame.K_SPACE:
                    x = rect_position[0] + 25
                    y = rect_position[1]
                    bullet_cord = [x,y]
                    strike(bullet_cord)

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                velocity_y = 0
            if event.key in (pygame.K_a, pygame.K_d):
                velocity_x = 0

    rect_position[0] += (speed * velocity_x)
    rect_position[1] += (speed * velocity_y)

    current_time = pygame.time.get_ticks()
    if current_time - last_time_spawn > waves_spawn_interval:
        if len(enemies) == 0:
            for i in range(5):
                enemy = [random.randint(0, 800), random.randint(-150, 0)]
                enemies.append(enemy)
            current_wave += 1
        last_time_spawn = current_time

    for enemy in enemies:
        enemy[1] += 2
        if enemy[1] > 800:
            enemies.remove(enemy)

    screen.blit(background, (0, 0))

    for enemy in enemies:
        screen.blit(scaled_wrogi_statek, enemy)

    for enemy in enemies:
        for bullet in bullets:
            if bullet[1] < enemy[1] + 100 and bullet[0] > enemy[0]:
                bullets.remove(bullet)
                enemies.remove(enemy)
                points += 100

    draw_bullet()
    screen.blit(scaled_statek, rect_position)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()