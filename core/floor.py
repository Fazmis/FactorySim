from .floor_area import FloorArea
from objects import PlaceableObject


class Floor:
    """
    Класс Floor описывает цех
    атрибуты:
        id:int - Уникальный идентификатор цеха
        name:None|str - Наименование цеха
        area:FloorArea - Сетка цеха
        objects:list[PlaceableObject] - Содержит список размещённых объектов в цеху
    методы:
        pass
    """
    def __init__(self, floor_id:int, area:tuple[int, int], name:None|str=None):
        self.id = floor_id
        self.name = name
        self.area = FloorArea(area)
        self.objects = []

    def place_object(self, obj:PlaceableObject, top_left: tuple[int, int]):
        self.area.place_object(obj, top_left)
        self.objects.append(obj)