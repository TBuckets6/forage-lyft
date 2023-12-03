# flake8: noqa

import unittest
from datetime import datetime

from battery.spindler import Spindler

class TestSpindler(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = 'Dec 2 2023'
        last_service_date = 'Jun 13 2020'
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = 'Dec 2 2023'
        last_service_date = 'Dec 3 2021'
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()