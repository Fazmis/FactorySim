from .map_grid import MapGrid


class Map:
    """
    Класс Map описывает карту
    атрибуты:
        id:int - Уникальный идентификатор карты
        name:None|str - Наименование карты
        area:MapGrid - Сетка карты
        objects:list[PlaceableObject] - Содержит список размещённых объектов на карте
    методы:
        pass
    """
    def __init__(self, floor_id:int, area:tuple[int, int], name:None|str=None):
        self.id = floor_id
        self.name = name
        self.area = MapGrid(area)
        self.objects = []

    def place_object(self, obj) -> None:
        """
        Временная заглушка
        """
        pass