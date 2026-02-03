from core import Factory
from objects import PlaceableObject

if __name__ == '__main__':
    factory = Factory()
    factory.create_floor(area=(3, 4))
    factory.floors[0].place_object(PlaceableObject((2,3)), (0, 0))
    for row in factory.floors[0].area.grid:
        print(*row)