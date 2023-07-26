
from unittest.mock import patch
from unittest import TestCase
import app
import task_01

class TaskTest(TestCase):

    def test_get_product_name(self):
        self.assertEqual('CPU', app.all_cpu[1].get_product_name())

    def test_get_cpu_core_count(self):
        self.assertEqual('16', app.all_cpu[1].get_cpu_core_count())

    def test_(self):
        self.assertEqual('1320 MHz', app.all_gpu[1].get_gpu_core_clock())

if __name__ == '__main__':
    pass
