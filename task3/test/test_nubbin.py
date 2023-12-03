#When trying to import a package from a sibling directory,
#to avoid the "ImportError: attempted relative import with no known parent package",
#run the file with the command "python -m test.test_nubbin" from the root directory
# rather than the usual way to run a program: python test_nubbin.py.

# flake8: noqa

import unittest
from datetime import datetime

from battery.nubbin import Nubbin

class TestNubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = 'Dec 2 2023'
        last_service_date = 'Oct 4 2018'
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = 'Dec 2 2023'
        last_service_date = 'Oct 4 2021'
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()