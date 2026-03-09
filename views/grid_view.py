from random import randrange as rr
import pygame as pg
from engine import Camera


class GridView:
    """
    Отрисовка сетки

    В данный момент представляет собой "затычку" созданную для тестирования отрисовки и поведения камеры

    Аттрибуты:
        grid_area (tuple[int, int]): Хранит размерность сетки
    Методы:
        draw(): Отрисовывает сетку из квадратов случайных цветов размерностью grid_area, с учётом положения и масштаба камеры.
    """
    def __init__(self, grid_area) -> None:
        self.grid_area = grid_area

    def draw(self, display:pg.Surface, camera:Camera) -> None:
        cell_size = camera.cell_size
        for row_index in range(self.grid_area[0]):
            for column_index in range(self.grid_area[1]):
                rect = (pg.Rect(column_index * cell_size - camera.y, row_index * cell_size - camera.x, cell_size, cell_size))
                display.fill((rr(256), rr(256), rr(256)), rect)