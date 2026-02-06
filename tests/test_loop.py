import unittest
import time
from engine import MainEngineLoop


class TestMainEngineLoop(unittest.TestCase):

    def setUp(self):
        # небольшой fps, чтобы тесты шли быстро
        self.loop = MainEngineLoop(fps=10)

    def tearDown(self):
        # гарантируем остановку потока после каждого теста
        if self.loop.running:
            self.loop.terminate()

    # ---------- INIT ----------

    def test_init_running_true(self):
        self.assertTrue(self.loop.running)

    def test_init_fps_positive(self):
        self.assertGreaterEqual(self.loop.fps, 0)

    def test_thread_is_alive_after_init(self):
        self.assertTrue(self.loop.thread.is_alive())

    # ---------- RESUME / PAUSE ----------

    def test_resume_sets_event(self):
        self.loop.resume()
        self.assertTrue(self.loop.running_event.is_set())

    def test_pause_clears_event(self):
        self.loop.resume()
        self.loop.pause()
        self.assertFalse(self.loop.running_event.is_set())

    # ---------- TERMINATE ----------

    def test_terminate_stops_loop(self):
        time.sleep(0.05)
        self.loop.terminate()

        self.assertFalse(self.loop.running)
        self.assertFalse(self.loop.thread.is_alive())

    def test_terminate_can_be_called_without_resume(self):
        # поток ещё не запущен логически, но terminate всё равно должен сработать
        self.loop.terminate()
        self.assertFalse(self.loop.thread.is_alive())


if __name__ == "__main__":
    unittest.main()