# FactoryError (BaseError)
class FactoryError(Exception):
    """Фундамент для самописных исключений в рамках модели"""
    pass

# Grid Section
class GridError(FactoryError):
    """Базовое исключение для ошибок сетки"""
    pass

class OutOfBoundsError(GridError):
    """Выход за границы сетки"""
    pass

class PlacementError(GridError):
    """Ошибка размещения объекта"""
    pass

class DeterminingBoundsError(GridError):
    """Ошибка определения границ сетки"""
    pass