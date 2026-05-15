class BaseComponent[T_data]:
    """
    Базовый компонент - каркас для классов-хранилищ компонентов

    Хранит [id, data] для описания сущностей, имеет CRUD-методы

    Аргументы:
        entities (dict[eid, T_data]): Хранит сущности с их параметрами присущим компоненту

    Методы:
        add_eid(): Добавляет eid + data в хранилище, если eid уже есть в хранилище - KeyError
        get(): Возвращает значение по ключу (eid), если ключа нет в хранилище - None
        update(): Обновляет значение по ключу (eid), если ключа нет в хранилище - KeyError
        remove_eid(): Удаляет значение по ключу (eid), если ключа нет в хранилище - KeyError
    """
    def __init__(self) -> None:
        self.entities = dict()

    def add_eid(self, eid:int, data:T_data) -> None:
        if eid in self.entities:
            raise KeyError(f"Идентификатор сущности [{eid}] уже хранится в компоненте")
        self.entities[eid] = data

    def get(self, eid:int) -> None | T_data:
        return self.entities.get(eid)

    def update(self, eid:int, data:T_data) -> None:
        if eid not in self.entities:
            raise KeyError(f"Идентификатор сущности [{eid}] отсутствует в компоненте")
        self.entities[eid] = data

    def remove_eid(self, eid:int) -> T_data:
        if eid not in self.entities:
            raise KeyError(f"Идентификатор сущности [{eid}] отсутствует в компоненте")
        return self.entities.pop(eid)
