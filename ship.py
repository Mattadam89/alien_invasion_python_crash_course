import pygame

class Ship:
    """a class to manage the ship."""

    # takes a reference to the current instance of the game so that it has
    # access to all the game resources defined in the instance of alien
    # invasion
    def __init__(self, ai_game):
        """initialise the ship and set its starting position"""

        # assign screen to an attribute of a ship so it can be accessed in
        # methods of the this class
        self.screen = ai_game.screen

        # pygame treats all objects as a rectangle even if they actually arent
        # so this gives us the rect attributes of the screen so we can place
        # the ship in the correct position on the screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    # in the pygame documentation the blit method
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
