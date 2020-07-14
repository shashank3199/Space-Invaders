# import pygame module
import pygame

# import characters and helper functions for the game
from characters import Player, Enemy, Bullet, is_collision, show_score, font
# import global variable for the game scope
from global_variables import *

# initialize pygame
pygame.init()

# initialize game window
screen = pygame.display.set_mode(size=(PAGE_WIDTH, PAGE_HEIGHT))
# set caption of game window
pygame.display.set_caption('Space Invaders')
# load icon for game
icon = pygame.image.load('./images/ufo.png')
# set icon for the game
pygame.display.set_icon(icon)

# player -
p1 = Player(x=PLAYER_X,
            y=PLAYER_Y,
            screen=screen,
            image_path="./images/space-invaders.png")

# list of enemies -
enemies = list()
# make 2 rows
for j in range(2):
    # of 10 enemies each
    for i in range(10):
        enemy = Enemy(x=((PAGE_WIDTH - 2 * PAGE_BORDER) // 11) * (i + 1),
                      y=ENEMY_Y + j * ENEMY_START_HEIGHT,
                      screen=screen,
                      image_path="./images/spaceship.png",
                      respawn_status=False)
        enemies.append(enemy)

# bullet -
b = Bullet(x=BULLET_X,
           y=BULLET_Y,
           screen=screen,
           image_path="./images/bullet.png")


# main function -
def main():
    # score variable
    score = 0
    # to kill game if ESC is pressed or windows is closed
    game_running = True
    # to kill game if player destroyed or all enemies killed
    game_over = False

    # game loop
    while game_running and not game_over:
        # fill background for game
        screen.fill(color=(100, 100, 100))
        # input all the keys pressed at an instant
        keys = pygame.key.get_pressed()
        # if right arrow key is pressed move player forward
        if keys[pygame.K_RIGHT]:
            p1.move(pygame.K_RIGHT)
        # if left arrow key is pressed move player backward
        elif keys[pygame.K_LEFT]:
            p1.move(pygame.K_LEFT)
        # if escape key is pressed kill game
        elif keys[pygame.K_ESCAPE]:
            game_running = False

        """
        Note: Here, the keys.get_pressed and event.type == pygame.KEY_DOWN are different
              because the former accounts for press and hold key as multiple input strokes
              but the later registers press and hold of a key as one input stroke. 
        """

        # to check for event cases
        for event in pygame.event.get():
            # kill game, if game window is closed
            if event.type == pygame.QUIT:
                game_running = False
            # fire bullet when space bar is pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and b.state == BULLET_READY:
                    b.state = BULLET_FIRED
                    b.x = p1.x

        # loop to check for all enemies
        for e in enemies:
            # bullet and enemy collision
            if is_collision(e.x, e.y, b.x, b.y):
                # reset bullet y coordinate as that of player
                b.y = p1.y + 16
                # reset state of bullet as ready
                b.state = BULLET_READY
                # increase score
                score += 10
                # respawn the enemy if possible, else set enemy as not alive
                e.respawn()
                # if enemy not alive remove from list of enemies
                if not e.respawn_status:
                    enemies.remove(e)

            # enemy and player collision
            if is_collision(p1.x, p1.y, e.x, e.y, 40):
                game_over = True
                game_running = False

        # check number of alive enemies
        enemy_alive = 0
        for e in enemies:
            enemy_alive += 1 if e.alive else 0
            # move the enemy objects that are alive
            e.move()

        # if all the enemies are dead then game over
        if enemy_alive == 0:
            game_over = True
            game_running = False

        # show player object
        p1.show()
        # show bullet object if state is FIRED
        b.fire()
        # display score on screen
        show_score(screen, score)
        # update the screen after each iteration
        pygame.display.update()

    # if game is over and not closed midway
    while game_over:
        # fill background
        screen.fill(color=(100, 100, 100))
        # add and display game over text
        game_over_text = font.render("GAME OVER", True, (200, 0, 0))
        game_over_len, game_over_height = game_over_text.get_rect().size
        screen.blit(game_over_text,
                    (PAGE_WIDTH / 2 - game_over_len / 2,
                     PAGE_HEIGHT / 3 + game_over_height / 2))

        # add and display final score text
        final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
        final_score_len, final_score_height = final_score_text.get_rect().size
        screen.blit(final_score_text,
                    (PAGE_WIDTH / 2 - final_score_len / 2,
                     2 * PAGE_HEIGHT / 3 + final_score_height / 2))

        pygame.display.update()
        # wait till user presses a key
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                game_over = False

    # end game and close window
    pygame.quit()


if __name__ == '__main__':
    main()
