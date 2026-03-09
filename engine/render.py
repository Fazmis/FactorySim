import pygame as pg
from .camera import Camera
from views import GridView

class Render:
    """
    Менеджер отрисовки

    Инициализирует pygame дисплей, заполняет фон,
    обновляет дисплей и (в будущем) вызывает отрисовку моделей.

    Аттрибуты:
        window_size (tuple[int, int]): Хранит размер окна
        display (pygame.Surface): Дисплей pygame для отрисовки/вывода окна и объектов в окне
        camera (Camera): Хранит и передаёт, в вызываемые views, объект камеры для адаптивной отрисовки views
        views (list[View]): Хранит views для цикличного вызова их отрисовки
    Методы:
        _init_display(): Приватный метод для инициализации pygame.display, установки названия и иконки окна
        _fill_background(): Отрисовка заднего фона
        draw(): Вызов для отрисовки заднего фона, моделей (в будущем) и обновление дисплея
        show_fps(fps): Отрисовка показателя fps
    """
    def __init__(self, window_size:tuple[int, int] = (640, 320)):
        self.window_size = window_size
        self._init_display()
        self.camera = Camera()
        self.views = [GridView((10, 10))]

    def _init_display(self) -> None:
        """
        Инициализация display
        """
        pg.init()
        self.display = pg.display.set_mode(self.window_size)
        pg.display.set_caption("FactorySim")
        pg.display.set_icon(pg.image.load("textures/others/icon.png"))

    def _fill_background(self) -> None:
        """
        Отрисовка заднего фона
        """
        self.display.fill((255, 0, 0))

    def show_fps(self, fps:float):
        """
        Отрисовывает переданное значение fps
        """
        text = pg.font.SysFont(name="Segoe UI Black", size=15).render(f"{fps} fps", 0, (200,50,30))
        self.display.blit(text, (0, 0))

    def draw(self, fps_link=None) -> None:
        """
        Вызывает отрисовки заднего фона, отрисовок views,
        отрисовки fps (если передано fps_link) и обновляет display
        """
        # отрисовка заднего фона
        self._fill_background()

        # отрисовка всех хранимых views
        for view in self.views:
            view.draw(self.display, self.camera)

        # отрисовка fps (если передано)
        if fps_link:
            self.show_fps(fps_link)

        pg.display.flip()
