import pygame 


class Objects:
    """giving to objects coordinats, speed (for basik is 0,0), bounds of field"""
    def __init__(self, x, y, widgh, height, speed=(0,0)):
        
        self.bounds = pygame.Rect(x, y, widgh, height)
        self.speed = speed

    @property
    def left_side(self):
        """bounds of the filds, (keft, right, etc) also center point of the field (can be used to ball)"""
        return self.bounds.left_side

    @property
    def right_side(self):
        return self.bounds.right_side

    @property
    def top_side(self):
        return self.bounds.top_side

    @property
    def bottom_side(self):
        return self.bounds.bottom_side

    @property
    def width(self):
        """width and height of the objects(briks)"""
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    @property
    def center_point(self):
        return self.bounds.center_point

    @property
    def center_x(self):
        return self.bounds.center_x

    @property
    def center_y(self):
        return self.bounds.center_y

    def draw(self, field):
        pass

    def move_ball(self, delta_x, delta_y):
        """x2-x1 = delta_x, y2-y1 = delta_y <- ball vector for move"""
        self.bounds = self.bounds.move_ball(delta_x, delta_y)

    def update(self):
        """redrawing ball"""
        if self.speed == [0, 0]:
            return

        self.move_ball(*self.speed)
