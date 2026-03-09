class SimulationsManager:
    """
    Заготовка для SimulationsManager

    Выполняет роль заготовки и в данный момент "пробки" для менеджера симуляций

    Аргументы:
        simulations (list[Simulation]): Хранит симуляции для их цикличной обработки

    Методы:
        simulate(): Проходит по всем симуляциям вызывая симуляцию.
    """
    def __init__(self) -> None:
        self.simulations = []

    def simulate(self) -> None:
        for simulation in self.simulations:
            simulation.simulate()