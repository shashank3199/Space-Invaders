# import eucledian distance formula
from math import hypot
# import randint to generate random integers
from random import randint

# import pygame modulde
import pygame

# import global variable for the game scope
from global_variables import *


# basic template for all objects in the game
class ObjectTemplate:
    # default initialization for any object in game
    def __init__(self, x: int, y: int, screen: pygame.Surface, image_path: str = None, image: pygame.Surface = None):
        self.x = x
        self.y = y
        self.screen = screen
        # load/set icon for the character
        self.image = image if (image_path is None) else pygame.image.load(image_path)
        if self.image is not None:
            self.width, self.height = self.image.get_rect().size
        else:
            self.width, self.height = (-1, -1)

    # function to display the object on the surface of the respective object
    def show(self):
        self.screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))


# player class to implement player object
class Player(ObjectTemplate):
    # default initialization, calls super class init 
    def __init__(self, x: int, y: int, screen: pygame.Surface, image_path: str = None, image: pygame.Surface = None):
        super().__init__(x, y, screen, image_path, image)

    # move the x coordinate of the player based o the input key received
    def move(self, key):
        # if input is RIGHT then increase x coordinate
        if key == pygame.K_RIGHT:
            self.x += PLAYER_CHANGE if (
                    self.x < PAGE_WIDTH - PAGE_BORDER - self.width) else 0
        # if input is LEFT then decrease x coordinate
        elif key == pygame.K_LEFT:
            self.x -= PLAYER_CHANGE if (self.x > self.width / 2) else 0


# enemy class to implement enemy object
class Enemy(ObjectTemplate):
    # default initialization, calls super class init
    def __init__(self, x: int, y: int, screen: pygame.Surface, image_path: str = None, image: pygame.Surface = None,
                 respawn_status: bool = True):
        super().__init__(x, y, screen, image_path, image)
        # set default direction as FORWARD when game begins
        self.direction = ENEMY_FORWARD
        # set whether to respawn the enemy or not
        self.respawn_status = respawn_status
        # set status of enemy as alive until shot dead
        self.alive = True

    # move the enemy object based on the direction
    def move(self):
        # move forward by incrementing x coordinate
        if self.direction is ENEMY_FORWARD:
            self.x += ENEMY_CHANGE
            # change direction and increase height of the enemy once it reaches the max x coordinate of the screen
            if self.x > PAGE_WIDTH - PAGE_BORDER - self.width:
                self.direction = ENEMY_BACKWARD
                self.y += ENEMY_HEIGHT_CHANGE
        # move forward by decrementing x coordinate
        elif self.direction is ENEMY_BACKWARD:
            self.x -= ENEMY_CHANGE
            # change direction and increase height of the enemy once it reaches the min x coordinate of the screen
            if self.x < PAGE_BORDER:
                self.direction = ENEMY_FORWARD
                self.y += ENEMY_HEIGHT_CHANGE
        # display the enemy on the screen is alive
        if self.alive:
            self.show()

    # re-display the enemy once destroyed if respawn_status is true, else do not show the object again
    def respawn(self):
        if self.respawn_status:
            # select random integer between the specified dimensions
            self.x = randint(PAGE_BORDER, PAGE_WIDTH - PAGE_BORDER)
            # start again from initial height
            self.y = ENEMY_START_HEIGHT
        else:
            # set alive status of the object to be false
            self.alive = False


#  bullet class to implement the bullet object
class Bullet(ObjectTemplate):
    # default initialization, calls super class init
    def __init__(self, x: int, y: int, screen: pygame.Surface, image_path: str = None, image: pygame.Surface = None):
        super().__init__(x, y, screen, image_path, image)
        # set default state of bullet as ready
        self.state = BULLET_READY

    def fire(self):
        # reset the bullet state once it reaches the min screen height
        if self.y < BULLET_END_HEIGHT:
            self.y = BULLET_Y
            self.state = BULLET_READY

        # display the bullet on screen if fired
        if self.state == BULLET_FIRED:
            self.y -= 1
            self.show()


# Helper Functions -

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', int(PAGE_WIDTH / 20))


# display score
def show_score(screen: pygame.Surface, score: int, score_x: int = 10, score_y: int = 10):
    score_text = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (score_x, score_y))


# detect collision between objects
def is_collision(x1: int, y1: int, x2: int, y2: int, collison_threshold: int = 25):
    distance = hypot((x2 - x1), (y2 - y1))
    if distance < collison_threshold:
        return True
    else:
        return False
