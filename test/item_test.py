import pygame
from pygame.math import Vector2
from lib.item import Item
import random


def test_init():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    return screen


def test_exit():
    pygame.quit()


def test_item():
    test_init()
    return Item(25)


def test_draw_item(mocker):
    mocker.patch('random.randint', return_value=10)
    screen = test_init()
    item = test_item()
    asset, loc = item.draw_item_util()
    assert asset == item.apple
    assert loc == pygame.Rect(250, 250, 25, 25)
    item.draw_item(screen)
    test_exit()
