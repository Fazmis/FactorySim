from config import resolution
from engine import *

if __name__ == '__main__':
    # Обработчик ввода пользователя
    handler_user_input = EventHandler()
    # Рендер графики
    render = Render(window_size=resolution)
    # Основной цикл движка
    loop = MainEngineLoop(60, EventHandler(), render)
    # Запуск основного цикла движка
    loop.start()