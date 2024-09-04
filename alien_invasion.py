import sys
import pygame

from setting import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        pygame.display.set_caption("Alien Invasion")
        self.screen = pygame.display.set_mode(
            (0, 0) , pygame.FULLSCREEN
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if(bullet.rect.bottom <= 0):
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key ==pygame.K_q:
            sys.exit()
        

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            #每次循环时重绘屏幕
            pygame.display.flip()
            self.clock.tick(60)
    
#if __name__ == '_main_':
ai = AlienInvasion()
ai.run_game()
