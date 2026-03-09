import pygame as pg

class EventHandler:
    """
    Обработчик событий

    Обрабатывает события pygame.event и пользовательский ввод

    Аттрибуты:
        None
    Методы:
        process_input(): Обрабатывает ивенты pygame.event и пользовательский ввод
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
                continue

            if event.type == pg.MOUSEWHEEL:
                callback.render.camera.zoom(event.dict["y"])
                continue

        # Обработка ввода (управление камерой)
        keys = pg.key.get_pressed()
        dx = dy = 0
        if keys[pg.K_w]:
            dx = -1
        elif keys[pg.K_s]:
            dx = 1

        if keys[pg.K_d]:
            dy = 1
        elif keys[pg.K_a]:
            dy = -1

        if dx or dy:
            callback.render.camera.move(dx, dy)