import pygame
import objects 

class Quadra_Brick(objects.Objects):
    """constructor for rectangle"""
    def __init__(self, center_x, center_y, widgh, height, color_brik, special_effect=None):
        objects.Objects.__init__(self, center_x, center_y, widgh, height)
        self.color_brik = color_brik
        self.special_effect = special_effect

    def draw(self, field):
        pygame.draw.rect(field, self.color_brik, self.bounds)

class Triangle_Brick(objects.Objects):
    """constructor for triangle"""
    def __init__(self, center_x, center_y, widgh, height, color_brik, special_effect=None):
        objects.Objects.__init__(self, center_x, center_y, widgh, height)
        self.color_brik = color_brik
        self.special_effect = special_effect

    def draw(self, field):
        pygame.draw.triangle(field, self.color_brik, self.bounds)

class Geksa_Brick(objects.Objects):
    """constructor for geksagramm"""
    def __init__(self, center_x, center_y, widgh, height, color_brik, special_effect=None):
        objects.Objects.__init__(self, center_x, center_y, widgh, height)
        self.color_brik = color_brik
        self.special_effect = special_effect

    def draw(self, field):
        pygame.draw.gecta(field, self.color_brik, self.bounds)


"""also we draw ^ briks (choose by random for map (field))"""