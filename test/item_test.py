import pygame
from pygame.math import Vector2
from lib.item import Item, Apple, Portal
import random


def test_init():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    return screen


def test_exit():
    pygame.quit()


def test_apple():
    test_init()
    return Apple(25, 20)


def test_draw_item(mocker):
    mocker.patch('random.randint', return_value=10)
    screen = test_init()
    item = test_apple()
    asset, loc = item.draw_item_util()
    apple_asset = pygame.image.load('resources/apple.png').convert_alpha()
    assert (asset.get_parent() == apple_asset.get_parent()
            and asset.get_offset() == apple_asset.get_offset())
    assert loc == pygame.Rect(250, 250, 25, 25)
    item.draw_item(screen)
    test_exit()
