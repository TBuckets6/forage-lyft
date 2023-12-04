# flake8: noqa

import unittest

from engine.willoughby import Willoughby

class TestWilloughby(unittest.TestCase):
    
    def test_needs_service_true(self):
        last_service_mileage = 20000
        current_mileage = 90000
        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_needs_service_false(self):
        last_service_mileage = 20000
        current_mileage = 70000
        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
        
if __name__ == '__main__':
    unittest.main()