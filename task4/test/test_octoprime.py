# flake8: noqa

import unittest

from tires.octoprime import Octoprime

class TestCarrigan(unittest.TestCase):
    
    def test_needs_service_true(self):
        tire_wear = [.8, .8, .8, .8]
        tires = Octoprime(tire_wear)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        tire_wear = [.5, .6, .6, .9]
        tires = Octoprime(tire_wear)
        self.assertFalse(tires.needs_service())
        
if __name__ == '__main__':
    unittest.main()