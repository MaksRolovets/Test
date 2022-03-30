import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Images/tile_0000.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.rect.width = 45
    def update(self):
        self.rect.y -= 8
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
