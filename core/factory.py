from .floor import Floor
from config.config import auto_naming_floor

class Factory:
    """
    Класс Factory описывает завод
    аргументы:
        self.floors:dict[int:Floor] - Словарь хранящий уникальный id: экземпляр класса Floor
        self.floor_id:int - Счетчик для выдачи уникальных id
    методы:
        create_floor - Создает цех и добавляет его в self.floors:dict
        delete_floor - Удаляет цех из self.floors:dict по id, возвращая его.
    """
    def __init__(self) -> None:
        self.floors:dict[int:Floor] = {}
        self.floor_id:int = 0

    def create_floor(self, area:tuple[int, int], name:None|str=None) -> None:
        """
        Создает цех и добавляет его в self.floors:dict
        При недопустимых значениях области кидает ValueError
        (при включенном авто-наименовании и name = None,
        использует наименование цеха - "Floor {self.floor_id}")
        параметры:
            area:tuple[int, int] - Размер цеха в клетках
            name:None|str - Наименование цеха
        """
        if any(map(lambda x: x < 1, area)):
            raise ValueError(f"Цех не может иметь размер '{area[0]}x{area[1]}'")
        if not name and auto_naming_floor:
            name = f"Floor {self.floor_id}"
        self.floors[self.floor_id] = Floor(self.floor_id, area, name)
        self.floor_id += 1

    def delete_floor(self, floor_id:int) -> Floor:
        """
        Удаляет цех по id, возвращая его. Если id не найден - кидает KeyError
        параметры:
            floor_id:int - Уникальный идентификатор удаляемого цеха
        выход:
            Floor - Удаленный цех
        """
        if floor_id not in self.floors:
            raise KeyError(f"Цеха с id '{floor_id}' не существует!")
        return self.floors.pop(floor_id)