import random
import sys
import time

import pygame

# initialize pyGame and mixer for music
pygame.init()
pygame.mixer.init()

# screen settings
WIDTH = 893
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)
RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)

# Game variables for score, balls, and velocity
score = 0
balls = 1
velocity = 4

# Paddle settings
paddle_width = 54
paddle_height = 20

# Create a sprite group to hold all the sprites
all_sprites_list = pygame.sprite.Group()

# Load images, sounds, and music
menu_background = pygame.image.load("../assets/images/starmenu.jpg")  # Background image for menu
menu_music = "../sounds/Cocoon.mp3"  # Music for menu
game_music = "../sounds/GenerousPalmstroke.wav"  # Music for in-game
brick_sound = pygame.mixer.Sound("../sounds/brick.wav")  # Sound for brick hits
paddle_sound = pygame.mixer.Sound("../sounds/paddle.wav")  # Sound for ball hitting paddle
wall_sound = pygame.mixer.Sound("../sounds/wall.wav")  # Sound for ball hitting walls


# Brick class to create and draw bricks
class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


# Paddle class to create and control paddle
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


# Ball class to create and control ball
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface(
            [width, height]
        )  # Create a rectangular surface for the ball
        pygame.draw.rect(
            self.image, color, [0, 0, width, height]
        )  # Draw the ball with the specified color
        self.rect = self.image.get_rect()  # Get the rectangular boundary of the ball
        self.velocity = [velocity, velocity]  # Set the initial velocity of the ball

    def update(self):

        # Update the ball's position based on its velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):

        # Invert the vertical velocity to make the ball bounce
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


# Create paddle and ball objects
paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2  # Center the paddle horizontally
paddle.rect.y = HEIGHT - 65  # Position the paddle near the bottom

ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH // 2 - 5  # Center the ball horizontally
ball.rect.y = HEIGHT // 2 - 5  # Center the ball vertically

all_bricks = pygame.sprite.Group()  # Create a group to store all bricks

# Brick layout settings
brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


# Function to create bricks in the game
def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(PINK, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(PINK, brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(CYAN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(CYAN, brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = (
                        wall_width
                        + brick_width
                        + x_gap
                        + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


brick_wall = bricks()  # Initialize bricks layout

# Add paddle and ball to the sprite group
all_sprites_list.add(paddle)
all_sprites_list.add(ball)


# Function to display text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


font = pygame.font.Font(None, 36)

# Function to display Game Over Screen
def game_over_screen():
    screen.blit(menu_background, (75, 0))
    draw_text("GAME OVER", font, WHITE, screen, WIDTH // 2, HEIGHT // 4)
    draw_text("1. Retry", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 20)
    draw_text("2. Main Menu", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 20)
    draw_text("3. Exit", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Restarts the game with the initial score and balls with key 1
                if event.key == pygame.K_1:
                    waiting = False
                    main(0, 1)  
                # Returns player to main menu with key 2
                elif event.key == pygame.K_2:
                    waiting = False
                    main_menu()
                # Exits game with key 3
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()


# Main Menu
def main_menu():
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)  # Loop background music in menu
    while True:

        # Draw background image to fill the screen
        screen.blit(menu_background, (75, 0))

        # Draw menu text
        draw_text(
            "Another Breakout Game Menu", font, CYAN, screen, WIDTH // 2, HEIGHT // 4
        )
        draw_text("1. Start Game", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 20)
        draw_text("2. Quit", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 20)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    paddle_sound.play()
                    pygame.mixer.music.stop()
                    main(score, balls)
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()


# The game/physics
def main(score, balls):

    # Play game music in a loop
    pygame.mixer.music.load(game_music)
    pygame.mixer.music.play(-1)

    step = 0

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(10)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(10)

        all_sprites_list.update()

        # Ball collision with top boundary
        if ball.rect.y < 40:
            ball.velocity[1] = -ball.velocity[1]
            wall_sound.play()

        # Ball collision with right boundary
        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        # Ball collision with left boundary
        if ball.rect.x <= wall_width:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.velocity[1] = ball.velocity[1]
            balls += 1
            if balls == 4:
                font = pygame.font.Font("../yle/DSEG14Classic-Bold.ttf", 70)
                text = font.render("GAME OVER", 1, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                #Display Game Over Screen
                game_over_screen()
                run = False

        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x += ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
            paddle_sound.play()

        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()
            if len(brick_collision_list) > 0:
                step += 1
                for i in range(0, 448, 28):
                    if step == i:
                        ball.velocity[0] += 1
                        ball.velocity[1] += 1
            if 380.5 > brick.rect.y > 338.5:
                score += 1
                brick.kill()
            elif 338.5 > brick.rect.y > 294:
                score += 3
                brick.kill()
            elif 294 > brick.rect.y > 254.5:
                score += 5
                brick.kill()
            else:
                score += 7
                brick.kill()
            if len(all_bricks) == 0:
                font = pygame.font.Font("../assets/text_style/DSEG14Classic-Bold.ttf", 70)
                text = font.render("SCREEN CLEARED", 1, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                all_sprites_list.add(ball)
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        # Draw bricks, score, ball number, and high score (HS coming soon)

        screen.fill(BLACK)

        pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
        pygame.draw.line(
            screen,
            GREY,
            [(wall_width / 2) - 1, 0],
            [(wall_width / 2) - 1, HEIGHT],
            wall_width,
        )
        pygame.draw.line(
            screen,
            GREY,
            [(WIDTH - wall_width / 2) - 1, 0],
            [(WIDTH - wall_width / 2) - 1, HEIGHT],
            wall_width,
        )

        pygame.draw.line(
            screen,
            BLUE,
            [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
            [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54],
            wall_width,
        )
        pygame.draw.line(
            screen,
            BLUE,
            [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
            [
                (WIDTH - wall_width / 2) - 1,
                HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54,
            ],
            wall_width,
        )

        pygame.draw.line(
            screen,
            PINK,
            [(wall_width / 2) - 1, 212.5],
            [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            PINK,
            [(WIDTH - wall_width / 2) - 1, 212.5],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            ORANGE,
            [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            ORANGE,
            [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            CYAN,
            [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            CYAN,
            [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            YELLOW,
            [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            YELLOW,
            [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap],
            wall_width,
        )

        font = pygame.font.Font("../assets/text_style/DSEG14Classic-Bold.ttf", 70)
        text = font.render(str(f"{score:03}"), 1, WHITE)
        screen.blit(text, (80, 120))
        text = font.render("ball: " + str(balls), 1, WHITE)
        screen.blit(text, (520, 41))
        text = font.render("000", 1, WHITE)
        screen.blit(text, (580, 120))
        text = font.render("Level: 1", 1, WHITE)
        screen.blit(text, (20, 40))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


# Run the main menu at the start of the program
if __name__ == "__main__":
    main_menu()
