import unittest

import pygame

from firsttrybreakout1 import (
    BLUE,
    HEIGHT,
    PINK,
    WHITE,
    WIDTH,
    Ball,
    Brick,
    Paddle,
    velocity,
)

pygame.init()


class TestBreakoutGame(unittest.TestCase):

    def setUp(self):
        self.paddle = Paddle(BLUE, 54, 20)
        self.ball = Ball(WHITE, 10, 10)
        self.brick = Brick(PINK, 55, 16)
        self.wall_width = 16

    def test_paddle_move_right(self):
        initial_x = self.paddle.rect.x
        self.paddle.moveRight(20)
        self.assertEqual(self.paddle.rect.x, initial_x + 20)

        self.paddle.rect.x = WIDTH - self.wall_width - 54
        self.paddle.moveRight(10)
        self.assertEqual(self.paddle.rect.x, WIDTH - self.wall_width - 54)

    def test_paddle_move_left(self):
        initial_x = self.paddle.rect.x
        self.paddle.moveLeft(20)

        expected_x = max(initial_x - 20, self.wall_width)
        self.assertEqual(self.paddle.rect.x, expected_x)

        self.paddle.rect.x = self.wall_width
        self.paddle.moveLeft(10)
        self.assertEqual(self.paddle.rect.x, self.wall_width)

    def test_ball_update(self):
        initial_x, initial_y = self.ball.rect.x, self.ball.rect.y
        self.ball.update()
        self.assertEqual(self.ball.rect.x, initial_x + velocity)
        self.assertEqual(self.ball.rect.y, initial_y + velocity)

    def test_ball_bounce(self):
        initial_velocity = self.ball.velocity[1]
        self.ball.bounce()
        self.assertEqual(self.ball.velocity[1], -initial_velocity)

    def test_brick_creation(self):
        self.assertEqual(self.brick.rect.width, 55)
        self.assertEqual(self.brick.rect.height, 16)

    def test_brick_group(self):
        all_bricks = pygame.sprite.Group()
        for i in range(5):
            brick = Brick(PINK, 55, 16)
            brick.rect.x = i * (55 + 5)
            brick.rect.y = 100
            all_bricks.add(brick)
        self.assertEqual(len(all_bricks), 5)


if __name__ == "__main__":
    unittest.main()
