from .placeable_object import PlaceableObject


class PlaceableObjectWithInventory(PlaceableObject):
    """
    Класс PlaceableObjectWithInventory наследуется от PlaceableObject, добавляя механику инвентаря
    """
    def __init__(self, size:tuple[int, int], inventory_size:int=5):
        super().__init__(size)
        self.inventory_size = inventory_size
        self.inventory = Queue()
        self.remaining_space = inventory_size

    def add_in_inventory(self, obj: object) -> None:
        if self.remaining_space >= 1:
            self.inventory.add(obj)
            self.remaining_space -= 1

    def take_from_inventory(self, i:int=0) -> object | None:
        if self.inventory:
            self.remaining_space += 1
            return self.inventory.pop(i)
        else:
            return None