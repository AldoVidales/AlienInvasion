import sys
import pygame
from settings import Settings
from ship import  Ship
from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        """Initialize the game,and create game resources"""
        pygame.init()
        self.settings=Settings()

        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_heigth=self.screen.get_rect().height


        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()

        #Set the background color.
        self.bg_color=self.settings.bg_color


    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self.ship.update()
            self._update_bullets()
            #Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            self._update_screen()
            #Watch for keyboard and mouse events.




    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#This elif call the events types keydown
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:#This call the events type keyup
                self._check_keyup_events(event)


            #What happend when the keyisDown

    def _check_keydown_events(self,event):
        """Respond to key releases"""

        if event.key==pygame.K_RIGHT:
                    #Move the ship to the rigth
            self.ship.moving_right=True
        elif event.key ==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_q:#Close the game
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()


            #What happend when the keyisUp
    def _check_keyup_events(self,event):

        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullet_allowed:
            """Create a new bullet and add it to the bullets group"""
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)




    def _update_screen(self):
        """Update images on the screen,and flip to the new screen"""
        # Redraw the screen during each pass througth the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently draw screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()


        #Get rid of bullets that have disappeared

        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)



if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()