from config.config import min_area_for_floor_area, max_area_for_floor_area
from errors.exceptions import DeterminingBoundsError, PlacementError, OutOfBoundsError
from objects import PlaceableObject

class FloorArea:
    """
    Класс FloorArea описывает сетку цеха
    атрибуты:
        area:tuple[int, int] - Размер сетки цеха в клетках
        grid:list[list] - Сетка цеха предназначенная для размещения объектов в цеху размерностью "area"
    методы:
        is_cell_free - Проверка пуста ли клетка
        is_area_free - Проверка пуста ли область
        place_object - Разместить объект на сетку
    """
    def __init__(self, area:tuple[int, int]):
        #area validation
        # Валидация на правильную упаковку входных параметров
        if not(isinstance(area, tuple)):
            raise TypeError(f"Ожидался tuple, получен {type(area)}..")
        # Валидация на количество входных параметров
        if len(area) != 2:
            raise ValueError(f"Ожидалось 2 элемента в area, получено {len(area)}..")
        # Валидация на тип входных параметров
        if any(not(isinstance(x, int)) for x in area):
            raise TypeError(f"Ожидался tuple(int, int), получен tuple({type(area[0])}, {type(area[1])})..")
        # Проверка на нереальные значения сетки
        if any(map(lambda x: x <= 0, area)):
            raise DeterminingBoundsError(f"Границы сетки не могут быть меньше нуля или отрицательными!")
        # Заданы допустимые границы сетки (определяемые в config)
        if any(map(lambda x: not(min_area_for_floor_area <= x <= max_area_for_floor_area), area)):
            raise DeterminingBoundsError(f"Недопустимые границы сетки {area[0]}x{area[1]}!")
        height, width = area
        self.area = (width, height)
        self.grid = [[None for _ in range(self.area[0])] for _ in range(self.area[1])]

    def is_cell_free(self, x:int, y:int):
        return not(bool(self.grid[x][y]))

    def is_area_free(self, x0:int, x1:int, y0:int, y1:int):
        """
        Пробегает по области используя is_cell_free,
        при найденной непустой клетке кидает False, иначе True по окончанию проверки
        """
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if not self.is_cell_free(x, y):
                    return False
        return True

    def place_object(self, obj: PlaceableObject, top_left: tuple[int, int]):
        """
        Размещает объект по координатам
        Гарантирует:
            1 Объект размещён в пустой зоне
            2 Объект размещён в границах сетки
        Кидает:
            1 PlacementError
            2 OutOfBoundsError
        """
        x0, y0 = top_left
        x1 = x0 + obj.size[0] - 1
        y1 = y0 + obj.size[1] - 1
        if (
            x0 < 0 or
            x1 > self.area[0] or
            y0 < 0 or
            y1 > self.area[1]
        ):
            raise OutOfBoundsError("Выход за границы сетки!")

        if not self.is_area_free(x0, x1, y0, y1):
            raise PlacementError("Объект не может быть размещён в несвободной зоне!")

        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                self.grid[x][y] = obj
