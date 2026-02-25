import pygame as pg


class EventHandler:
    """
    Обработчик событий

    Обрабатывает события pygame.event

    Аттрибуты:
        None
    Методы:
        process_input(): Обрабатывает ивенты pygame.event (На данный момент только ивент выхода!)
    """

    def __init__(self) -> None:
        pass

    def process_input(self, callback) -> None:
        """
        Обработка событий

        Аргументы:
            callback: объект с атрибутом `running` (обычно главный цикл движка MainEngineLoop),
                  который будет остановлен при событии выхода (QUIT).
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                callback.running = False