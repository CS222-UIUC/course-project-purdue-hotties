import pytest
import pygame
from pygame.math import Vector2
from lib.snake import Snake


def test_init():
    pygame.init()
    pygame.display.set_mode((1000, 1000))


def test_exit():
    pygame.quit()


def test_snake():
    """
    Returns a test snake object like this
    8   @ - T   @ - @
        |       |   |
    9   @ - @ - @   @ - @
                        |
    10          H - @   @
                    |   |
    11              @ - @
        8   9   10  11  12
    """
    test_init()
    snake = Snake(25)
    snake.body = [
        Vector2(10, 10),
        Vector2(11, 10),
        Vector2(11, 11),
        Vector2(12, 11),
        Vector2(12, 10),
        Vector2(12, 9),
        Vector2(11, 9),
        Vector2(11, 8),
        Vector2(10, 8),
        Vector2(10, 9),
        Vector2(9, 9),
        Vector2(8, 9),
        Vector2(8, 8),
        Vector2(9, 8),
    ]
    snake.direction = Vector2(-1, 0)
    return snake


def test_draw_snake_util():
    """
    Test the draw_snake_util implementation by testing 
    using the test snake object
    """
    test_init()
    snake = test_snake()
    components = snake.draw_snake_util()
    locations = [snake.get_rect(b) for b in snake.body]
    assets = [
        snake.head_left,
        snake.body_bl,
        snake.body_tr,
        snake.body_tl,
        snake.body_vertical,
        snake.body_bl,
        snake.body_tr,
        snake.body_bl,
        snake.body_br,
        snake.body_tl,
        snake.body_horizontal,
        snake.body_tr,
        snake.body_br,
        snake.tail_right,
    ]
    components_ans = [(assets[ind], loc) for ind, loc in enumerate(locations)]
    assert components == components_ans
    test_exit()


def test_move_snake():
    test_init()
    snake = test_snake()
    snake.move_snake()
    move_ans = [
        Vector2(9, 10),
        Vector2(10, 10),
        Vector2(11, 10),
        Vector2(11, 11),
        Vector2(12, 11),
        Vector2(12, 10),
        Vector2(12, 9),
        Vector2(11, 9),
        Vector2(11, 8),
        Vector2(10, 8),
        Vector2(10, 9),
        Vector2(9, 9),
        Vector2(8, 9),
        Vector2(8, 8),
    ]
    assert snake.body == move_ans
    test_exit()
