# flake8: noqa

from engine.engine import Engine

class Capulet(Engine):
    
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000