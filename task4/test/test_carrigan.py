# flake8: noqa

import unittest

from tires.carrigan import Carrigan

class TestCarrigan(unittest.TestCase):
    
    def test_needs_service_true(self):
        tire_wear = [.3, .5, .5, .91]
        tires = Carrigan(tire_wear)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        tire_wear = [.89, .5, .3, .7]
        tires = Carrigan(tire_wear)
        self.assertFalse(tires.needs_service())
        
if __name__ == '__main__':
    unittest.main()