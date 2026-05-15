from ecs.entity import EntityManager
import ecs.components
from ecs.components import BaseComponent
from world.map import Map
from typing import Any

class World:
    """
    World

    Хранит компонентные хранилища, организует добавление сущностей в хранилища, в будущем чтение/обновление/удаление

    Аргументы:
        entities (dict[eid, T_data]): Хранит сущности с их параметрами присущим компоненту
        self.entity_manager (type[EntityManager]): хранит ссылку на объект EntityManager
        self.components (dict[class, object]): хранит класс компонентного хранилища и объект это класса

    Методы:
        create_entity(): Регистрирует новую сущность в переданных хранилищах по eid cгенерированному в EntityManager
    """
    def __init__(self) -> None:
        self.entity_manager = EntityManager()
        self.components = dict()
        for component_class in ecs.components.COMPONENTS:
            self.components[component_class] = component_class()

        self.map = Map(0, (32, 32))

    def create_entity(self, components:dict[BaseComponent, Any]) -> None:
        eid = self.entity_manager.create_entity()
        for component_class, data in components.items():
            self.components[component_class].add_eid(eid, data)
