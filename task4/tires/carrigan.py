# flake8: noqa

from tires.tires import Tires

class Carrigan(Tires):
    
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self) -> bool:
        count = 0
        
        for tire in self.tire_wear:
            if tire >= .9:
                count = count + 1
        
        if count >= 1:
            return True
        
        return False