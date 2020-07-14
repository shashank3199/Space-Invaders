# width of game screen
PAGE_WIDTH = 800
# height of game screen
PAGE_HEIGHT = 600
# width of space around the border
PAGE_BORDER = 32

# starting coordinates of player
PLAYER_X = PAGE_WIDTH / 2
PLAYER_Y = PAGE_HEIGHT - 120
# change in x coordinate of player when left/right key is pressed
PLAYER_CHANGE = 0.6

# initial height of the enemy
ENEMY_START_HEIGHT = 85
# change in x coordinate of enemy
ENEMY_CHANGE = 0.2
# change in y coordinate of enemy to move towards the player
ENEMY_HEIGHT_CHANGE = 40
# x direction of the enemy
ENEMY_FORWARD = True
ENEMY_BACKWARD = False
# starting coordinates of enemy
ENEMY_X = PLAYER_X
ENEMY_Y = ENEMY_START_HEIGHT

# starting coordinates of the bullet
BULLET_X = PLAYER_X
BULLET_Y = PLAYER_Y + 16
# change in bullet y coordinate when fired
BULLET_CHANGE = 1
# bullet state, in order to enable only single bullet at a time
BULLET_READY = True
BULLET_FIRED = False
# height at which bullet disappears and state is changed back
BULLET_END_HEIGHT = ENEMY_START_HEIGHT
