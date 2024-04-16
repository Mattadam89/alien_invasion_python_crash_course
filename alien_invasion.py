import sys

import pygame

from settings import Settings

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

    def run_game(self):
        """Start main loop for the game."""
        while True:
            # watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_colour)

            # make the most recently drawn screen visible.
            pygame.display.flip()

            # try to make the loop run exactly 60 times/sec
            self.clock.tick(60) 

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()