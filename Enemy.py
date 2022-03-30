import pygame

class Enemy():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('Images/character_0024.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.black_rect = (self.x, self.y, 50, 50)
        self.dead = False
        self.images = [pygame.image.load('Images/pngwing1.png'), pygame.image.load('Images/pngwing2.png'),
                       pygame.image.load('Images/pngwing3.png'), pygame.image.load('Images/pngwing4.png'),
                       pygame.image.load('Images/pngwing5.png'), pygame.image.load('Images/pngwing6.png'),
                       pygame.image.load('Images/pngwing7.png'), pygame.image.load('Images/pngwing8.png'),
                       pygame.image.load('Images/pngwing9.png'), pygame.image.load('Images/pngwing10.png')]

    def output_Enemy(self):
        self.screen.blit(self.image, self.rect)

    def update_enemy(self):
        self.rect.y += 1

    def death(self):

        for i in range(0, 9, 1):
            pygame.draw.rect(self.screen, (0, 0, 0), self.black_rect)
            self.screen.blit(self.images[i], (600, 800))