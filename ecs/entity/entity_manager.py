class EntityManager:
    """
    Менеджер сущностей

    Создаёт идентификаторы для сущностей, гарантируя их уникальность. Хранит все созданные идентификаторы.
    Позволяет удалять переданный идентификатор из хранимых идентификаторов.

    Аргументы:
        _next_id (int): Счётчик идентификаторов
        entities (set[int]): Множество для хранения созданных идентификаторов
    Методы:
        is_exists(eid): Проверяет уникальность переданного eid
        create_entity(): Добавляет новый уникальный идентификатор в множество entities и возвращает его
        delete_entity(eid): Удаляет передаваемый eid (идентификатор сущности) из entities
        clear(): Сброс менеджера, обнуление счётчика и удаление всех хранимых entities
    """
    def __init__(self) -> None:
        self._next_id = 0
        self.entities = set()

    def is_exists(self, eid:int) -> bool:
        return eid in self.entities

    def create_entity(self) -> int:
        eid = self._next_id
        self.entities.add(eid)
        self._next_id += 1
        return eid

    def delete_entity(self, eid:int) -> None:
        self.entities.discard(eid)

    def clear(self) -> None:
        self.entities.clear()
        self._next_id = 0
