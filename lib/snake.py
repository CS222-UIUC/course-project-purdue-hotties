from lib.map import Map

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(0, 1)

        self.head_up = pygame.image.load(
            'resources/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'resources/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'resources/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'resources/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load(
            'resources/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'resources/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'resources/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'resources/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(
            'resources/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'resources/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(
            'resources/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'resources/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'resources/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'resources/body_bl.png').convert_alpha()

    