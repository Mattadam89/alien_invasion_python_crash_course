import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        # create instance of clock class
        self.clock = pygame.time.Clock() 
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        ##initialise a ship object within the game
        self.ship = Ship(self)

    def run_game(self):
        """Start main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # try to make the loop run exactly 60 times/sec
            self.clock.tick(60) 
    
    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        # make the most recently drawn screen visible.
        pygame.display.flip()
        

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()