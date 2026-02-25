import time
import pygame as pg
from .render import Render
from .event_handler import EventHandler

class MainEngineLoop:
    """
    Главный цикл движка

    Вызывает обработку ввода пользователя, расчёт симуляции, рендер
    GUI/UI. Держит frame-rate. Имеет возможность остановки/возобновления расчёта симуляции.

    Аттрибуты:
        fps (int): Ограничение количества кадров/итераций в секунду
        handler_user_input (EventHandler): Класс обработчик ввода
        render (Render): Класс для управления отрисовкой pygame
        running (bool): Флаг цикла
        running_sim (bool): Флаг симуляции (для паузы/возобновления симуляции)
        pg_clock (pygame.time.Clock): Менеджер времени pygame
    Методы:
        _loop(): Приватный метод цикла (для запуска start())
        resume_sim(): Возобновить расчёт симуляции
        pause(): Приостановить расчёт симуляции
        start(): Запустить работу цикла
        terminate(): Завершить работу цикла
    """
    def __init__(self, fps:int, handler_user_input:EventHandler, render:Render) -> None:
        self.fps = abs(fps)
        self.handler_user_input = handler_user_input
        self.render = render
        self.running = True
        self.running_sim = True

        pg.init()
        self.pg_clock = pg.time.Clock()

    def _loop(self) -> None:
        """
        При запуске "крутится" пока не получит команду.
        Соблюдает ограничение по итерациям (self.fps)
        """
        while self.running:

            # user_input
            self.handler_user_input.process_input(self)

            # simulation
            if self.running_sim:
                super_sim = "bip" + "!"

            # render
            self.render.draw()

            self.pg_clock.tick(self.fps)

    def resume_sim(self) -> None:
        """
        Возобновляет работу симуляции
        """
        self.running_sim = True

    def pause_sim(self) -> None:
        """
        Приостанавливает работу симуляции
        """
        self.running_sim = False

    def start(self) -> None:
        """
        Запускает работу цикла
        """
        self.running = True
        self._loop()

    def terminate(self) -> None:
        """
        Останавливает работу цикла
        """
        self.running = False