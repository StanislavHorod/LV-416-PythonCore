import pygame
import objects


class Stryker_Ball(objects.Objects):
    def __init__(self, center_x, center_y, ball_radius, color_ball, ball_speed):
        objects.Objects.__init__(self, center_x - ball_radius, center_y - ball_radius, ball_radius * 2, ball_radius * 2, ball_speed)
        self.ball_radius = ball_radius
        self.diameter = ball_radius * 2
        self.color_ball = color_ball

    def draw(self, surface):
        ball_radius = pygame.draw.circle(surface, self.color_ball, self.center_point, self.ball_radius)

    def update(self):
        super().update()
