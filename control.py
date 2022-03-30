import pygame, sys
from bullet import Bullet

def control(gun, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            if event.key == pygame.K_a:
                gun.mleft = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, bullets, enemys):

    screen.fill(bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()

    for b in enemys:
        b.output_Enemy()

    for i in bullets:
        for b in enemys:
            if i.rect.collidepoint(b.rect.centerx, b.rect.centery):
                bullets.remove(i)
                enemys.remove(b)
                b.death()
    pygame.display.flip()



'''def collision(bullets, enemys):
    for i in bullets:
        for b in enemys:
            if i.rect.collidepoint(b.rect.centerx, b.rect.centery):
                bullets.remove(i)
                b.death()
                enemys.remove(b)
    pygame.display.flip()'''


def bullet_update(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def position_check(enemys):
    for i in enemys:
        if i.rect.bottom > 800:
            sys.exit()


