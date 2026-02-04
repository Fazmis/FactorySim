import time

from core import Factory
from engine.loop import MainEngineLoop
from objects import PlaceableObject
from engine import MainEngineLoop

if __name__ == '__main__':
    print("Фабрика с одним цехом и одним объектом:")
    factory = Factory()
    factory.create_floor(area=(3, 4))
    factory.floors[0].place_object(PlaceableObject((2,3)), (0, 0))
    for row in factory.floors[0].area.grid:
        print(*row)
    print()

    print("Пример работы цикла:")
    loop = MainEngineLoop(2)
    for _ in range(5):
        loop.resume()
        time.sleep(1)
        loop.pause()
        print("Цикл остановлен")
    print()