import pygame as pg

class Render:
    """
    Менеджер отрисовки

    Инициализирует pygame дисплей, заполняет фон,
    обновляет дисплей и (в будущем) вызывает отрисовку моделей.

    Аттрибуты:
        window_size (tuple[int, int]): Хранит размер окна
        display (pygame.Surface): Дисплей pygame для отрисовки/вывода окна и объектов в окне
    Методы:
        _init_display(): Приватный метод для инициализации pygame.display, установки названия и иконки окна
        _fill_background(): Отрисовка заднего фона
        draw(): Вызов для отрисовки заднего фона, моделей (в будущем) и обновление дисплея
    """
    def __init__(self, window_size:tuple[int, int] = (640, 320)):
        self.window_size = window_size
        self._init_display()

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

    def draw(self) -> None:
        """
        Вызов отрисовок и обновление display
        """
        self._fill_background()

        pg.display.flip()
