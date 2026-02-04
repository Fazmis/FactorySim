import time
from threading import Thread, Event

class MainEngineLoop:
    """
    Класс MainEngineLoop - Главный цикл движка, который будет вызывать расчёт симуляции и рендер
    GUI/UI, а также использован для сбора ввода пользователя.
    аттрибуты:
        running - флаг цикла
        running_event - флаг события потока (для паузы/возобновления)
        thread - поток-исполнитель цикла
        fps - ограничение количества кадров/итераций в секунду
    методы:
        _loop - Приватный метод запускающий цикл
        resume - возобновить работу цикла
        pause - приостановить работу цикла
        terminate - завершить работу цикла
    """
    def __init__(self, fps:int):
        self.running = True
        self.running_event = Event()
        self.thread = Thread(target=self._loop)
        self.fps = abs(fps)
        self.thread.start()

    def _loop(self):
        """
        При запуске "крутится" пока не получит команду
        Соблюдает ограничение по итерациям (self.fps)
        """
        while self.running:
            self.running_event.wait()
            last_frame_time = time.time()

            # user_input()
            user_input_data = "bip"
            # simulation()
            super_sim = "bip" + "!"
            # render()
            print(super_sim)
            time.sleep(max([0, 1/self.fps - (time.time() - last_frame_time)]))

    def resume(self):
        """
        Возобновляет работу цикла
        """
        self.running_event.set()

    def pause(self):
        """
        Приостанавливает работу цикла
        """
        self.running_event.clear()

    def terminate(self):
        """
        Останавливает работу цикла (и потока!)
        """
        self.running = False
        self.running_event.set()
        self.thread.join()