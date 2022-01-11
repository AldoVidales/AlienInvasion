import sys
import pygame
from settings import Settings
from ship import  Ship

class AlienInvasion:

    def __init__(self):
        """Initialize the game,and create game resources"""
        pygame.init()
        self.settings=Settings()

        self.screen=pygame.display.set_mode((
            self.settings.screen_width,self.settings.screen_heigth
        ))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)

        #Set the background color.
        self.bg_color=self.settings.bg_color


    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self.ship.update()
            self._update_screen()
            #Watch for keyboard and mouse events.




    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            #What happend when the keyisDown


            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    #Move the ship to the rigth
                    self.ship.moving_right=True
                elif event.key ==pygame.K_LEFT:
                    self.ship.moving_left=True


            #What happend when the keyisUp

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
                elif event.key==pygame.K_LEFT:
                    self.ship.moving_left=False
                    #dsaf




    def _update_screen(self):
        """Update images on the screen,and flip to the new screen"""
        # Redraw the screen during each pass througth the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recently draw screen visible.
        pygame.display.flip()



if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()