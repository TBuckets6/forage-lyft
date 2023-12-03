# flake8: noqa

import unittest

from engine.sternman import Sternman

class TestSternman(unittest.TestCase):
    
    def test_needs_service_true(self):
        warning_light_on = True
        engine = Sternman(warning_light_on)
        self.assertTrue(engine.needs_service())
        
    def test_needs_service_false(self):
        warning_light_on = False
        engine = Sternman(warning_light_on)
        self.assertFalse(engine.needs_service())
        
if __name__ == '__main__':
    unittest.main()