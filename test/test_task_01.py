
from unittest.mock import patch
from unittest import TestCase
import task_01

class TaskTest(TestCase):

    def test_get_product_name(self):
        self.assertEqual('CPU', task_01.cpu1.get_product_name())

    def test_get_cpu_core_count(self):
        self.assertEqual('16', task_01.cpu1.get_cpu_core_count())

    def test_(self):
        self.assertEqual('1320 MHz', task_01.gpu1.get_gpu_core_clock())