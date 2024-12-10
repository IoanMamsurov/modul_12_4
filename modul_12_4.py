import logging
from rt_with_exceptions import Runner
import unittest


class TestRunner(unittest.TestCase):

    def test_walk(self):
        try:
            a = Runner('name', speed=-5)
            for i in range(10):
                a.walk()
                self.assertEqual(a.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.error('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            a = Runner(name=54, speed=10)
            for i in range(10):
                a.run()
            self.assertEqual(a.distance, 100)
            logging.info('"test_run" выполнен успешно"')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        a = Runner('name')
        b = Runner('name_2')
        for i in range(10):
            a.walk()
        for i in range(10):
            b.run()
        self.assertNotEqual(a.distance, b.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
