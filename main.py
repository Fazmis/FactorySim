from config import resolution
from engine import *
from engine.simulations_manager import SimulationsManager

if __name__ == '__main__':
    # Обработчик ввода пользователя
    handler_user_input = EventHandler()
    # Менеджер симуляций
    simulation_manager = SimulationsManager()
    # Рендер графики
    render = Render(window_size=resolution)
    # Основной цикл движка
    loop = MainEngineLoop(60, handler_user_input, simulation_manager, render)
    # Запуск основного цикла движка
    loop.start()