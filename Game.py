import pygame
import control
from Gun import Gun
from pygame.sprite import Group
from Enemy import Enemy

def run():

    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Игра')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    x = 0
    y = -300

    enemys = []

    for a in range(42):
        new_enemy = Enemy(screen, x, y)
        enemys.append(new_enemy)
        x += 50
        if new_enemy.rect.right > 650:
            x = 0
            y += 50

    while True:
        clock.tick(110)
        control.control(gun, screen, bullets)
        gun.update_gun()
        for i in enemys:
            i.update_enemy()
        control.position_check(enemys)
        control.update(bg_color, screen, gun, bullets, enemys)
        #control.collision(bullets, enemys)
        control.bullet_update(bullets)
run()