class Camera:
    """
    Камера игрового мира

    Определяет положение и масштаб отображения мира на экране.
    Используется при отрисовке для преобразования координат мира
    в экранные координаты.

    Аттрибуты:
        scope (float): Масштаб отрисовки
        base_cell_size (int): Базовый размер для клеток
        cell_size (float): Размер клеток с учётом scope
        x (int): Позиция камеры относительно оси x
        y (int): Позиция камеры относительно оси y
        base_speed (int): Базовая скорость движения камеры
    Методы:
        move(dx, dy): Переместить камеру по направлению (-1 <= dx|dy <= 1)
        zoom(dzoom): Увеличить (dzoom = 1)/Уменьшить (dzoom = -1) scope
    """
    def __init__(self, position=(0, 0), base_cell_size=50, scope=1):
        self.scope = scope
        self.base_cell_size = base_cell_size
        self.cell_size = base_cell_size
        self.x, self.y = position
        self.base_speed = 10

    def move(self, dx:int, dy:int):
        """
        Перемещение камеры
        """
        self.x += int(dx * self.base_speed // self.scope)
        self.y += int(dy * self.base_speed // self.scope)

    def zoom(self, dzoom:int):
        """
        Изменение масштаба
        """
        self.scope = round(self.scope + dzoom * 0.1, 1)
        self.scope = max(0.1, min(self.scope, 10))
        self.cell_size = self.base_cell_size * self.scope