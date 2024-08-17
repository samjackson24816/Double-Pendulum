from pygame import Vector2, SurfaceType, Surface, display, Color, draw
from setuptools.msvc import winreg


class Screen:

    screen_size: Vector2
    window: Surface | SurfaceType

    def __init__(self, screen_size: Vector2, window: Surface | SurfaceType):
        self.screen_size = screen_size
        self.window = window

    @staticmethod
    def flip():
        display.flip()

    def fill(self, color: Color):
        self.window.fill(color)

    def draw_circle(self, color: Color, position: Vector2, radius: float):
       draw.circle(self.window, color, self.to_pixels(position), radius)

    def draw_line(self, color: Color, start: Vector2, end: Vector2, width: int):
        draw.line(self.window, color, self.to_pixels(start), self.to_pixels(end), width)

    def draw_circle_pixel_scaled(self, color: Color, position: Vector2, radius: float):
        draw.circle(self.window, color, position, radius)

    def to_pixels(self, vec: Vector2) -> Vector2:
        return ((vec.elementwise() * Vector2(1, -1) / 100) + Vector2(1, 1)).elementwise() * self.screen_size / 2

    def to_scaled(self, vec: Vector2) -> Vector2:
        return ((vec.elementwise() / self.screen_size / 2) - Vector2(1, 1)).elementwise() * Vector2(1, -1) * 100
