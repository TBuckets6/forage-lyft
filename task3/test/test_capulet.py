# flake8: noqa

import unittest

from engine.capulet import Capulet

class TestCapulet(unittest.TestCase):
    
    def test_needs_service_true(self):
        last_service_mileage = 30000
        current_mileage = 60000
        engine = Capulet(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_needs_service_false(self):
        last_service_mileage = 30000
        current_mileage = 59999
        engine = Capulet(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
        
if __name__ == '__main__':
    unittest.main()