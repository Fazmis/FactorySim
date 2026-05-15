from .base_component import BaseComponent

class PlaceableEntityComponent(BaseComponent[tuple[int,int]]):
    """
    Заглушка для тестирования, возможно, в будущем класс компонентного хранилища.
    """
    def __init__(self) -> None:
        super().__init__()
